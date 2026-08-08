#!/usr/bin/env node
/**
 * Generates social media images via Ideogram API using João Marcos' brand identity.
 *
 * Usage:
 *   node scripts/generate-image.js "Corri 21km hoje na Meia Maratona do Rio 🏃‍♂️"
 *   node scripts/generate-image.js "Fé move montanhas" --style faith
 *   node scripts/generate-image.js "Treino de amanhã: 10km às 6h" --format story
 *
 * Options:
 *   --style   running | faith | lifestyle (default: auto-detect from prompt)
 *   --format  feed | story | reel-cover   (default: feed)
 *   --out     output filename (default: output-YYYY-MM-DD-HH.png)
 *
 * Required env:
 *   IDEOGRAM_API_KEY
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.IDEOGRAM_API_KEY;
if (!API_KEY) { console.error('Missing IDEOGRAM_API_KEY'); process.exit(1); }

// ── Brand identity ────────────────────────────────────────────
const BRAND = {
  colors: ['#E5341E', '#0E0E0E', '#F5F4F2', '#FFFFFF'],
  name: 'João Marcos Bomfim',
  handle: '@bomfim1710',
  tagline: 'atleta amador de corrida e falo de fé',
};

const STYLE_PRESETS = {
  running: {
    mood: 'energetic, athletic, motivational',
    visual: 'running athlete, urban São Paulo or Rio de Janeiro backdrop, early morning light, motion blur',
    typography: 'bold sans-serif, high contrast',
  },
  faith: {
    mood: 'peaceful, inspiring, spiritual',
    visual: 'warm golden light, minimalist background, subtle cross or nature elements',
    typography: 'elegant serif or clean sans-serif, soft contrast',
  },
  lifestyle: {
    mood: 'authentic, warm, personal',
    visual: 'casual everyday moments, natural light, documentary feel',
    typography: 'friendly, approachable',
  },
};

const FORMAT_SPECS = {
  feed:      { width: 1080, height: 1080, label: 'Square feed (1:1)' },
  story:     { width: 1080, height: 1920, label: 'Story/Reel (9:16)' },
  'reel-cover': { width: 1080, height: 1920, label: 'Reel cover (9:16)' },
};

// ── CLI args ──────────────────────────────────────────────────
const args = process.argv.slice(2);
const promptText = args.find(a => !a.startsWith('--')) || '';
if (!promptText) { console.error('Usage: node generate-image.js "your prompt"'); process.exit(1); }

const styleArg  = args[args.indexOf('--style')  + 1] || autoDetectStyle(promptText);
const formatArg = args[args.indexOf('--format') + 1] || 'feed';
const outArg    = args[args.indexOf('--out')    + 1] || null;

const style  = STYLE_PRESETS[styleArg]  || STYLE_PRESETS.running;
const format = FORMAT_SPECS[formatArg]  || FORMAT_SPECS.feed;

function autoDetectStyle(text) {
  const t = text.toLowerCase();
  if (/fé|deus|oração|bíblia|cristo|jesus|espírito|graça|palavra/.test(t)) return 'faith';
  if (/corri|km|treino|maratona|running|pace|strava|corrida/.test(t)) return 'running';
  return 'lifestyle';
}

// ── Build Ideogram prompt ─────────────────────────────────────
function buildPrompt(userText) {
  return `Social media post image for Brazilian fitness and faith content creator.

POST TEXT TO INCLUDE IN IMAGE: "${userText}"

VISUAL STYLE:
- ${style.mood}
- ${style.visual}
- Color palette: deep black (#0E0E0E) background, accent red (#E5341E), off-white (#F5F4F2) for text
- Clean, modern Brazilian aesthetic
- High quality, professional photography or illustration style

TYPOGRAPHY:
- Include the post text prominently in the image
- ${style.typography}
- Text must be perfectly legible
- Handle "@bomfim1710" in small text at bottom

COMPOSITION:
- ${format.label} format
- Leave breathing room, avoid cluttered layout
- No stock photo watermarks, no logos except @bomfim1710 handle`;
}

// ── API call ──────────────────────────────────────────────────
function post(path, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const options = {
      hostname: 'api.ideogram.ai',
      path,
      method: 'POST',
      headers: {
        'Api-Key': API_KEY,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data),
      },
    };
    const req = https.request(options, res => {
      let raw = '';
      res.on('data', d => raw += d);
      res.on('end', () => {
        try { resolve({ status: res.statusCode, body: JSON.parse(raw) }); }
        catch (e) { reject(new Error(`JSON parse error: ${raw.slice(0, 300)}`)); }
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

function downloadImage(url, dest) {
  return new Promise((resolve, reject) => {
    const proto = url.startsWith('https') ? require('https') : require('http');
    const file = fs.createWriteStream(dest);
    proto.get(url, res => {
      res.pipe(file);
      file.on('finish', () => { file.close(); resolve(); });
    }).on('error', err => { fs.unlink(dest, () => {}); reject(err); });
  });
}

// ── Main ──────────────────────────────────────────────────────
async function main() {
  const prompt = buildPrompt(promptText);
  console.log(`\n🎨 Gerando imagem...`);
  console.log(`   Estilo: ${styleArg} · Formato: ${formatArg} (${format.width}×${format.height})`);
  console.log(`   Prompt: "${promptText}"\n`);

  const res = await post('/generate', {
    image_request: {
      prompt,
      aspect_ratio: format.width === format.height ? 'ASPECT_1_1' : 'ASPECT_9_16',
      model: 'V_2',
      magic_prompt_option: 'AUTO',
      color_palette: {
        members: BRAND.colors.map(c => ({ color_hex: c })),
      },
      num_images: 1,
    },
  });

  if (res.status !== 200) {
    console.error('API error:', JSON.stringify(res.body, null, 2));
    process.exit(1);
  }

  const imageUrl = res.body.data?.[0]?.url;
  if (!imageUrl) { console.error('No image URL in response:', res.body); process.exit(1); }

  const ts = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 16);
  const filename = outArg || `output-${ts}.png`;
  const outDir = path.join(__dirname, '..', 'generated-images');
  fs.mkdirSync(outDir, { recursive: true });
  const dest = path.join(outDir, filename);

  console.log(`⬇️  Baixando imagem...`);
  await downloadImage(imageUrl, dest);

  console.log(`✅ Salvo em: generated-images/${filename}`);
  console.log(`\n📱 Pronto para postar em Instagram / TikTok / Threads!\n`);
}

main().catch(e => { console.error(e.message); process.exit(1); });
