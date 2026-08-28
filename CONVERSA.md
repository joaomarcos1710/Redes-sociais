# Evolução do Projeto @bomfim1710 — Documentação da Conversa

## 📋 Resumo Executivo

Desenvolvimento completo de um **dashboard de analytics de redes sociais** + **automação mensal de snapshots** + **templates de conteúdo no Figma** para João Marcos Bomfim, atleta amador e criador de conteúdo sobre fé.

**Status:** 🟢 Pronto para produção  
**Plataformas:** Instagram, TikTok, Threads, YouTube, Substack  
**Tecnologias:** HTML/CSS/JS (GitHub Pages), Node.js (Apify), Figma Pro

---

## 🎯 Objetivos Alcançados

### 1. **Site de Portfólio com Analytics Dashboard**
- ✅ Hero social com 5 links (Instagram, TikTok, Threads, YouTube, Substack)
- ✅ Painel "Onde eu estou" mostrando seguidores por plataforma
- ✅ Dashboard interativo com KPIs, gráficos de crescimento, demographics
- ✅ Switcher de plataforma (Instagram, TikTok, Threads, YouTube)
- ✅ Dados estruturados em `PLAT` object JavaScript
- ✅ Demografics por gênero, idade, região, SO
- ✅ Top posts e insights por plataforma

**Arquivo:** `/index.html` — 1 página, sem build step, GitHub Pages

### 2. **Automação Mensal de Snapshots (Apify)**
- ✅ Script Node.js que coleta dados de TikTok, Threads, YouTube
- ✅ GitHub Actions cron job (1º do mês, 11h UTC = 8h BRT)
- ✅ Snapshots em Markdown com frontmatter YAML (Obsidian Dataview)
- ✅ Armazenamento: `/data/snapshots/YYYY-MM-DD.md`
- ✅ Erros resolvidos:
  - ✏️ Input validation (Apify API)
  - ✏️ Actor ID URL format (~separator)
  - ✏️ Dataset response parsing (direct array)
  - ✏️ Field mapping (TikTok: `authorMeta.fans`, YouTube: `numberOfSubscribers`)

**Arquivo:** `/scripts/fetch-social-stats.js`  
**Workflow:** `/.github/workflows/monthly-snapshot.yml`

### 3. **Templates de Conteúdo no Figma**
- ✅ Arquivo "Conteúdo @bomfim1710" criado (Pro team)
- ✅ 4 templates prontos:
  - **Post Feed (1080×1080)** — Instagram, Threads
  - **Story/Reel Cover (1080×1920)** — Instagram Stories, TikTok, Reels
  - **Citação de Fé (1080×1080)** — Versículos, fundo off-white
  - **Post de Corrida (1080×1080)** — Stats de treino/prova
- ✅ Identidade visual: #E5341E (vermelho), #0E0E0E (preto), #F5F4F2 (off-white)
- ✅ Fonts: League Gothic (display), Hanken Grotesk (corpo)
- ✅ Handle @bomfim1710 em todos os templates

**URL:** https://www.figma.com/design/Njx2zQji8Pc0H9uBN8KsvX

---

## 🛠️ Arquitetura Técnica

### Frontend (GitHub Pages)
```
index.html (2000+ linhas)
├── Hero + Social Icons (SimpleIcons CDN)
├── "Onde eu estou" panel (seguidores por rede)
├── Analytics Dashboard
│   ├── Platform switcher (yt, ig, tt, threads, sub)
│   ├── KPI cards (seguidores, views, interações, etc)
│   ├── Bar chart (crescimento mensal)
│   ├── Audience demographics (gênero, idade, região, SO)
│   └── Top post card com stats
├── CSS Custom Properties (--ink, --paper, --off, --accent)
└── Figma link
```

### Backend (Node.js + Apify)
```
scripts/fetch-social-stats.js
├── Apify API client (HTTPS)
├── 3 actors paralelos: TikTok, Threads, YouTube
├── Snapshot builder (Markdown)
└── data/snapshots/2026-MM-DD.md
```

### CI/CD (GitHub Actions)
```
.github/workflows/monthly-snapshot.yml
└── Cron: 0 11 1 * * (1º de cada mês, 8h BRT)
    └── node scripts/fetch-social-stats.js
        └── APIFY_TOKEN, YOUTUBE_CHANNEL (secrets)
```

### Design System (Figma)
```
Conteúdo @bomfim1710 (Pro, team "A equipe de João Marcos Bomfim")
├── Post Feed (1:1)
├── Story/Reel Cover (9:16)
├── Citação de Fé (1:1)
└── Post de Corrida (1:1)
```

---

## 📊 Dados Coletados

### TikTok (@bomfim1710)
- Seguidores: 2.200+ (tracking desde junho)
- Views: 10,3k (28 dias)
- Audience: 55,6% masculino / 44,4% feminino
- Top age: 25-34 (38%), 35-44 (21,9%), 18-24 (20%)
- Origem: Pesquisa (63,8%), Para você (30,1%), Perfil (5,4%)

### Threads (@bomfim1710)
- Seguidores: 990+
- Views: 15,5k (30 dias)
- Crescimento: +4k vs junho (+35%)
- Nota: Dados de seguidores devem ser preenchidos manualmente

### YouTube (@bomfim1710)
- Canal novo, 104 vídeos
- Inscritos: 44+
- Views totais: 24k+
- Coletado via Apify desde 2026-08-08

### Instagram (manual)
- Seguidores: 1.023
- Alcance (30d): 30.424 contas
- Interações: 4.145
- Visualizações: 59.486 (Reels 74,4% · Stories 25,5%)
- Horário pico: 15h (468 views)

### Substack
- Assinantes: 472 (new)
- Crescimento: +23.500% (launch mês anterior)

---

## 🔧 Decisões Técnicas

### Por que Figma ao invés de Ideogram?
- **Figma:** Você já paga (Pro), conectado ao Claude, templates reutilizáveis, controle total
- **Ideogram:** API requer key (pendente), menos flexibilidade, custo extra

### Por que GitHub Actions para snapshots?
- Automação sem servidor dedicado
- Integração nativa com o repo
- Histórico de commits = auditável
- Apify é a melhor API de scraping para redes sociais

### Por que Obsidian Dataview?
- Frontmatter YAML permite queries em Obsidian
- Snapshots viram banco de dados consultável
- Future: grafos, relatórios mensais, trends

---

## 📈 Próximos Passos (Futuro)

1. **Instagram insights API** — Meta `instagram_manage_insights` permission
2. **Relatórios automáticos** — Obsidian/Dataview queries
3. **Notificações** — Slack/email quando atingir milestones
4. **Previsões** — Machine learning (growth projections)
5. **Social listening** — Sentimento em mentions/hashtags
6. **Conteúdo sugerido** — IA recomenda tópicos por engagement

---

## 🚀 Como Usar

### Editar Analytics no Site
1. Abra `/index.html` no editor
2. Procure pelo objeto `PLAT` (linha ~700)
3. Atualize `kpi`, `barJun`, `barJul`, `audience`, `topPost` para cada plataforma
4. Commit & push — GitHub Pages atualiza em ~30s

### Gerar Snapshot Manual
```bash
export APIFY_TOKEN="seu_token"
export YOUTUBE_CHANNEL="https://www.youtube.com/@bomfim1710"
node scripts/fetch-social-stats.js
# Gera: data/snapshots/2026-08-28.md (data de hoje)
```

### Usar Templates no Figma
1. Acesse https://www.figma.com/design/Njx2zQji8Pc0H9uBN8KsvX
2. Duplique o frame (Cmd+D / Ctrl+D)
3. Edite textos placeholder
4. Export como PNG/SVG
5. Publique em Instagram/TikTok

---

## 📝 Secrets GitHub

Configurados em `Settings > Secrets > Actions`:
- `APIFY_TOKEN` — token da API Apify
- `YOUTUBE_CHANNEL` — URL do canal (opcional, default: @bomfim1710)

**Nota:** Apify key deve ser regenerada se exposto (foi compartilhado nesta conversa)

---

## 🎨 Identidade Visual

```css
--ink: #0E0E0E        /* Preto profundo */
--paper: #FFFFFF      /* Branco puro */
--off: #F5F4F2        /* Off-white quente */
--accent: #E5341E     /* Vermelho vibrante */
```

**Fontes:**
- Display: League Gothic (headlines, títulos grandes)
- Corpo: Hanken Grotesk (texto, UI, labels)

---

## 🔐 Segurança

- ✅ Secrets em GitHub (não commitados)
- ✅ .gitignore: `generated-images/`, `node_modules/`, `.env`
- ⚠️ Meta tokens foram compartilhados (devem ser rotacionados)
- ⚠️ Apify key foi compartilhado (regenerado)

---

## 📞 Contato & Recursos

- **GitHub:** https://github.com/joaomarcos1710/redes-sociais
- **Figma:** https://www.figma.com/design/Njx2zQji8Pc0H9uBN8KsvX
- **Site ao vivo:** https://joaomarcos1710.github.io/redes-sociais (Pages)
- **Apify:** https://apify.com/
- **YouTube:** @bomfim1710
- **Threads:** @bomfim1710
- **TikTok:** @bomfim1710

---

**Última atualização:** 28 de agosto de 2026  
**Responsável:** Claude Code AI  
**Status:** 🟢 Produção
