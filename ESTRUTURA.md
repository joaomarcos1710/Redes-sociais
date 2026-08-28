# Estrutura do Repositório — Multi-Projeto Social Hub

## 📁 Organização

```
redes-sociais/
│
├── projects/                          # Todos os projetos/perfis
│   ├── bomfim1710/                    # Projeto 1: João Marcos Bomfim
│   │   ├── config.json                # Configuração do projeto
│   │   ├── index.html                 # Dashboard do projeto
│   │   ├── analytics/                 # Dados de analytics
│   │   │   ├── 2026-08-28.md         # Snapshot mensal
│   │   │   ├── _template.md          # Template snapshot
│   │   │   └── [scripts .js]
│   │   ├── content/                   # Posts agendados
│   │   ├── devotionals/               # Devocionais do projeto
│   │   └── strategies/                # Planos de conteúdo
│   │
│   ├── projeto-2/                     # Projeto 2 (duplicar _project-template)
│   │   ├── config.json
│   │   ├── index.html
│   │   └── ...
│   │
│   └── _project-template/             # Template para novos projetos
│       └── config.json
│
├── content/                           # Conteúdo compartilhado
│   ├── devotionals/                   # Base de devocionais
│   │   ├── 2026-08-28.md
│   │   └── _template.md
│   ├── strategies/                    # Estratégias gerais
│   │   ├── content-pillars.md
│   │   ├── 2026-Q3-strategy.md
│   │   └── calendar-editorial.md
│   └── templates/                     # Templates Figma links
│       └── README.md
│
├── scripts/                           # Scripts de automação
│   ├── fetch-social-stats.js          # Coleta de analytics (multi-projeto)
│   ├── schedule-posts.js              # Publica posts agendados
│   ├── generate-devotionals.js        # Gera devocionais com IA
│   └── [outros scripts]
│
├── data/                              # Dados históricos
│   ├── snapshots/                     # Analytics de todos projetos
│   ├── posts-scheduled/               # Fila de publicação
│   └── devotionals/                   # Base histórica
│
├── dashboard/                         # Dashboard multi-projeto (futura)
│   ├── index.html
│   ├── project-view.html
│   └── assets/
│
├── .github/workflows/                 # Automação GitHub Actions
│   ├── monthly-snapshot.yml
│   ├── daily-devotional.yml
│   └── social-posting.yml
│
├── README.md                          # Overview
├── ESTRUTURA.md                       # Este arquivo
├── CONVERSA.md                        # Histórico da conversa
├── PORTFOLIO.md                       # Portfolio pessoal
└── .gitignore
```

---

## 🚀 Como Adicionar um Novo Projeto

### 1. Copiar template
```bash
cp -r projects/_project-template projects/seu-projeto
cd projects/seu-projeto
```

### 2. Editar config.json
```json
{
  "project": {
    "name": "Seu Nome",
    "handle": "@seu-handle",
    "description": "Descrição",
    ...
  },
  "platforms": {
    "tiktok": { "enabled": true, "handle": "@seu-tiktok" },
    ...
  },
  "contentPillars": [...]
}
```

### 3. Copiar estrutura
```bash
# Criar pastas
mkdir -p analytics content devotionals strategies

# Copiar index.html (customizar depois)
cp ../bomfim1710/index.html .

# Copiar scripts
cp ../bomfim1710/*.js ./
```

### 4. Customizar
- Editar `index.html` com cores/fonts do projeto
- Criar estratégia de conteúdo em `strategies/`
- Configurar platforms habilitadas em `config.json`

---

## 📊 Arquivos por Seção

### Analytics (`projects/[projeto]/analytics/`)
- `YYYY-MM-DD.md` — Snapshot mensal (Apify)
- Frontmatter YAML: `data`, `tipo`, `plataforma_seguidores`, `views`, etc
- Obsidian Dataview compatible

**Exemplo:**
```markdown
---
data: 2026-08-28
tipo: snapshot_mensal
tt_seguidores: 2200
tt_views: 10300
ig_seguidores: 1023
yt_inscritos: 44
---

## 📊 Dados de Agosto

### TikTok
- Seguidores: 2.200 (+90 vs julho)
```

### Content (`projects/[projeto]/content/`)
- Posts agendados (Markdown ou JSON)
- Format: titulo, plataformas, data-publicacao, status

**Exemplo:**
```markdown
---
titulo: "Corri 21km na Meia Maratona"
plataformas: [tiktok, instagram, threads]
data: 2026-09-10T18:00:00
status: scheduled
pilar: corrida
---

Conteúdo do post aqui...
```

### Devotionals (`content/devotionals/`)
- Shared entre projetos
- Format: versículo, reflexão, aplicação prática
- Agendável para auto-publicação

**Exemplo:**
```markdown
---
data: 2026-08-28
versículo: "João 3:16"
tema: fé
fonte: bíblia
---

## Porque Deus amou o mundo...

### Reflexão
...

### Aplicação
...
```

### Strategies (`content/strategies/`)
- Planos trimestrais/anuais
- Calendário editorial
- Análise de pillars
- Roadmap de crescimento

---

## 🔧 Scripts de Automação

### `fetch-social-stats.js`
**Uso:** Coleta dados de todas as plataformas para um projeto
```bash
export PROJECT=bomfim1710
export APIFY_TOKEN=seu_token
node scripts/fetch-social-stats.js

# Gera: projects/bomfim1710/analytics/YYYY-MM-DD.md
```

### `schedule-posts.js` (futura)
**Uso:** Publica posts agendados nas datas corretas
```bash
node scripts/schedule-posts.js
# Lê: data/posts-scheduled/*.md
# Publica em: TikTok, Instagram, Threads, YouTube, Substack
```

### `generate-devotionals.js` (futura)
**Uso:** Gera devocionais automáticos com IA
```bash
node scripts/generate-devotionals.js
# Lê: data/devotionals/
# Publica em: todas as plataformas
```

---

## 🤖 GitHub Actions Workflows

### `monthly-snapshot.yml`
- **Trigger:** 1º do mês, 08:00 BRT
- **Ação:** `node scripts/fetch-social-stats.js` (multi-projeto)
- **Resultado:** Novo snapshot para cada projeto

### `daily-devotional.yml` (futura)
- **Trigger:** Todos os dias, 06:00 BRT
- **Ação:** Publica devocional agendada
- **Plataformas:** Todas habilitadas no config.json

### `social-posting.yml` (futura)
- **Trigger:** Verificação a cada 2h
- **Ação:** Publica posts na data/hora agendada
- **Suporte:** Buffer API ou direto nas plataformas

---

## 📈 Workflow Típico

### 1. Planejamento
```
content/strategies/2026-Q4-strategy.md
├── Temas por mês
├── Posts por semana
└── KPIs esperados
```

### 2. Criação de Conteúdo
```
projects/bomfim1710/content/
├── post-20260910-corrida.md
├── post-20260915-fe.md
└── post-20260920-lifestyle.md
```

### 3. Agendamento
```
data/posts-scheduled/
├── 2026-09-10T18:00:00-post-corrida.md
└── 2026-09-15T12:00:00-post-fe.md
```

### 4. Publicação Automática
- `schedule-posts.js` roda a cada 2h
- Publica posts na hora certa
- Loga resultado em Git

### 5. Analytics
- `monthly-snapshot.yml` roda 1º do mês
- Coleta dados de todas as plataformas
- Gera `projects/[projeto]/analytics/YYYY-MM-DD.md`

### 6. Análise
- Abrir relatório no Obsidian
- Executar Dataview queries
- Identificar trends e oportunidades

---

## 🔐 Secrets GitHub

Configure em `Settings > Secrets > Actions`:

```
# Apify
APIFY_TOKEN=seu_token

# Meta (Instagram/Threads/Facebook)
META_ACCESS_TOKEN=seu_token
META_APP_ID=seu_id
META_APP_SECRET=seu_secret

# TikTok
TIKTOK_ACCESS_TOKEN=seu_token

# YouTube
YOUTUBE_API_KEY=seu_key

# Buffer (futuro, para agendamento)
BUFFER_ACCESS_TOKEN=seu_token

# Canais específicos de projeto
PROJECT_BOMFIM_YOUTUBE=@bomfim1710
PROJECT_BOMFIM_SUBSTACK=joaomarcosbomfim
```

---

## 📝 Exemplo: Adicionar Novo Projeto

### Passo 1: Copiar template
```bash
cp -r projects/_project-template projects/meu-negocio
cd projects/meu-negocio
```

### Passo 2: Editar config.json
```json
{
  "project": {
    "name": "Meu Negócio",
    "handle": "@meu-negocio",
    "description": "E-commerce de produtos digitais"
  },
  "platforms": {
    "tiktok": { "enabled": true, "handle": "@meu-negocio-shop" },
    "instagram": { "enabled": true, "handle": "meu-negocio-shop" },
    "youtube": { "enabled": true, "handle": "@meu-negocio" }
  },
  "contentPillars": [
    { "name": "Produtos", "percentage": 50 },
    { "name": "Dicas", "percentage": 30 },
    { "name": "Comunidade", "percentage": 20 }
  ]
}
```

### Passo 3: Estrutura
```bash
mkdir -p analytics content devotionals strategies
touch content/.gitkeep  # Criar pasta mesmo vazia
```

### Passo 4: Commit
```bash
git add projects/meu-negocio/
git commit -m "feat: add new project 'Meu Negócio'"
git push
```

---

## 🎯 Próximas Implementações

- [ ] Dashboard multi-projeto (agregador)
- [ ] Schedule posts (Buffer ou direto)
- [ ] IA para gerar devocionais
- [ ] Obsidian Dataview queries
- [ ] Previsões de growth (ML)
- [ ] Notificações (Slack/Email)
- [ ] Social listening (mentions, hashtags)
- [ ] Content calendar visual (Notion/Figma)

---

**Última atualização:** 28 de agosto de 2026  
**Versão:** 1.0 (reorganização estrutural)
