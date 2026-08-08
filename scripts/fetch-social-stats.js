#!/usr/bin/env node
/**
 * Fetches social media stats via Apify and generates a monthly snapshot .md file.
 * Runs in GitHub Actions on the 1st of each month (or manually via workflow_dispatch).
 *
 * Required env vars:
 *   APIFY_TOKEN        — Apify API token
 *   YOUTUBE_CHANNEL    — YouTube channel handle or URL (optional, skip if not set)
 *
 * Outputs:
 *   data/snapshots/YYYY-MM-DD.md
 */

const https = require('https');

const APIFY_TOKEN = process.env.APIFY_TOKEN;
const YOUTUBE_CHANNEL = process.env.YOUTUBE_CHANNEL || 'https://www.youtube.com/@bomfim1710';

if (!APIFY_TOKEN) {
  console.error('Missing APIFY_TOKEN');
  process.exit(1);
}

// ── helpers ──────────────────────────────────────────────────

function apifyRequest(method, path, body, extraQuery = '') {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.apify.com',
      path: `${path}?token=${APIFY_TOKEN}${extraQuery}`,
      method,
      headers: { 'Content-Type': 'application/json' },
    };
    const req = https.request(options, res => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`JSON parse error: ${data.slice(0, 200)}`)); }
      });
    });
    req.on('error', reject);
    if (body) req.write(JSON.stringify(body));
    req.end();
  });
}

async function runActor(actorId, input, timeoutSecs = 120) {
  console.log(`[apify] running ${actorId}...`);
  // input goes directly as body; timeout is a query param
  const run = await apifyRequest(
    'POST',
    `/v2/acts/${encodeURIComponent(actorId)}/runs`,
    input,
    `&timeout=${timeoutSecs}&memory=256`
  );
  if (!run.data || !run.data.id) throw new Error(`Failed to start actor ${actorId}: ${JSON.stringify(run)}`);

  const runId = run.data.id;
  const start = Date.now();
  const deadline = timeoutSecs * 1000 + 30000;

  // poll until finished
  while (Date.now() - start < deadline) {
    await sleep(8000);
    const status = await apifyRequest('GET', `/v2/actor-runs/${runId}`);
    const s = status.data?.status;
    console.log(`[apify] ${actorId} status: ${s}`);
    if (s === 'SUCCEEDED') {
      const ds = await apifyRequest('GET', `/v2/actor-runs/${runId}/dataset/items`);
      return ds.data?.items || [];
    }
    if (s === 'FAILED' || s === 'ABORTED' || s === 'TIMED-OUT') {
      throw new Error(`Actor ${actorId} ended with status ${s}`);
    }
  }
  throw new Error(`Actor ${actorId} timed out after ${timeoutSecs}s`);
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function fmt(n) {
  if (n == null || isNaN(n)) return 0;
  return Math.round(Number(n));
}

function isoDate() {
  return new Date().toISOString().slice(0, 10);
}

// ── platform fetchers ─────────────────────────────────────────

async function fetchTikTok() {
  try {
    const items = await runActor('clockworks/tiktok-profile-scraper', {
      profiles: ['https://www.tiktok.com/@bomfim1710'],
      resultsType: 'profiles',
    });
    const p = items[0];
    if (!p) throw new Error('No TikTok data returned');
    return {
      tt_seguidores: fmt(p.followers ?? p.followerCount),
      tt_views: fmt(p.videoViews ?? p.totalVideoViews ?? 0),
      _raw_tt: p,
    };
  } catch (e) {
    console.warn('[tiktok] error:', e.message);
    return { tt_seguidores: 0, tt_views: 0 };
  }
}

async function fetchThreads() {
  try {
    const items = await runActor('futurizerush/meta-threads-scraper', {
      usernames: ['bomfim1710'],
      resultsLimit: 1,
    });
    const p = items[0];
    if (!p) throw new Error('No Threads data returned');
    return {
      threads_seguidores: fmt(p.followerCount ?? p.followers ?? 0),
      _raw_th: p,
    };
  } catch (e) {
    console.warn('[threads] error:', e.message);
    return { threads_seguidores: 0 };
  }
}

async function fetchYouTube() {
  if (!YOUTUBE_CHANNEL) {
    console.log('[youtube] YOUTUBE_CHANNEL not set, skipping');
    return { yt_inscritos: 0, yt_views: 0 };
  }
  try {
    const items = await runActor('streamers/youtube-channel-scraper', {
      startUrls: [{ url: YOUTUBE_CHANNEL }],
    });
    const p = items[0];
    if (!p) throw new Error('No YouTube data returned');
    return {
      yt_inscritos: fmt(p.subscriberCount ?? p.subscribers ?? 0),
      yt_views: fmt(p.viewCount ?? p.views ?? 0),
      _raw_yt: p,
    };
  } catch (e) {
    console.warn('[youtube] error:', e.message);
    return { yt_inscritos: 0, yt_views: 0 };
  }
}

// ── snapshot writer ───────────────────────────────────────────

function buildSnapshot(date, data) {
  const {
    tt_seguidores, tt_views,
    threads_seguidores,
    yt_inscritos, yt_views,
  } = data;

  // Instagram and Substack come from manual snapshot or future API integration
  // Leave as 0 so human can fill in (or future IG API adds them)
  return `---
data: ${date}
tipo: snapshot_mensal
ig_seguidores: 0
ig_alcance: 0
ig_interacoes: 0
tt_seguidores: ${tt_seguidores}
tt_views: ${tt_views}
threads_seguidores: ${threads_seguidores}
sub_inscritos: 0
yt_inscritos: ${yt_inscritos}
yt_views: ${yt_views}
---

## 📅 ${date} — Snapshot mensal (gerado automaticamente via Apify)

### TikTok — @bomfim1710
- Seguidores: ${tt_seguidores.toLocaleString('pt-BR')}
- Views totais de vídeo: ${tt_views.toLocaleString('pt-BR')}

### Threads — @bomfim1710
- Seguidores: ${threads_seguidores.toLocaleString('pt-BR')}

${yt_inscritos > 0 ? `### YouTube
- Inscritos: ${yt_inscritos.toLocaleString('pt-BR')}
- Views totais: ${yt_views.toLocaleString('pt-BR')}
` : ''}
### 📝 Dados manuais necessários
- Instagram: seguidores, alcance (30d), interações (30d)
- Substack: número de assinantes
`;
}

// ── main ──────────────────────────────────────────────────────

async function main() {
  const date = isoDate();
  console.log(`\n=== Snapshot ${date} ===\n`);

  const [tt, th, yt] = await Promise.all([
    fetchTikTok(),
    fetchThreads(),
    fetchYouTube(),
  ]);

  const data = { ...tt, ...th, ...yt };
  console.log('\n[results]', JSON.stringify(data, null, 2));

  const snapshot = buildSnapshot(date, data);
  const outPath = `data/snapshots/${date}.md`;

  const fs = require('fs');
  fs.mkdirSync('data/snapshots', { recursive: true });
  fs.writeFileSync(outPath, snapshot, 'utf-8');
  console.log(`\n[done] wrote ${outPath}`);
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
