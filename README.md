# Social Hub — Multi-Projeto

**Plataforma centralizada para gerenciar múltiplos perfis/projetos de redes sociais com automação, devocionais, estratégias de conteúdo e analytics em tempo real.**

🌐 **Site:** https://joaomarcos1710.github.io/redes-sociais  
📊 **Figma:** https://www.figma.com/design/Njx2zQji8Pc0H9uBN8KsvX  
📁 **Docs:** [ESTRUTURA.md](ESTRUTURA.md) — Guia completo da organização

---

## 🎯 O que é?

Um hub centralizado para:

✅ **Monitorar** múltiplos projetos/perfis de redes sociais  
✅ **Automatizar** coleta de analytics (Apify)  
✅ **Agendar** posts em múltiplas plataformas  
✅ **Criar** e publicar devocionais automáticos  
✅ **Planejar** estratégias de conteúdo  
✅ **Visualizar** dashboards por projeto  

---

## 📂 Estrutura

```
projects/
├── bomfim1710/              # Projeto existente
│   ├── config.json          # Configuração
│   ├── index.html           # Dashboard
│   ├── analytics/           # Snapshots
│   ├── content/             # Posts
│   └── devotionals/         # Devocionais
│
├── projeto-2/               # Seu próximo projeto
└── _project-template/       # Template para copiar
```

**[Ver estrutura completa →](ESTRUTURA.md)**

---

## 🚀 Quick Start

### 1. Adicionar novo projeto
```bash
cp -r projects/_project-template projects/seu-projeto
cd projects/seu-projeto
```

### 2. Editar config.json
```json
{
  "project": {
    "name": "Seu Nome",
    "handle": "@seu-handle"
  },
  "platforms": {
    "tiktok": { "enabled": true },
    "instagram": { "enabled": true }
  }
}
```

### 3. Gerar snapshot mensal
```bash
export APIFY_TOKEN=seu_token
export PROJECT=seu-projeto
node scripts/fetch-social-stats.js
```

### 4. Ver dashboard
Abra `projects/seu-projeto/index.html` no navegador.

---

## 📊 Projetos Ativos

| Projeto | Status | Plataformas | Dashboard |
|---|---|---|---|
| **bomfim1710** | ✅ Ativo | TikTok, Instagram, Threads, YouTube, Substack | [Abrir](projects/bomfim1710/index.html) |
| Seu Projeto 2 | 🔄 Em setup | — | — |
| Seu Projeto 3 | 🔄 Em setup | — | — |

---

## 🎬 Arquivos por Seção

### `/projects/[projeto]/`
- **config.json** — Configuração (plataformas, cores, fonts, pillars)
- **index.html** — Dashboard interativo
- **analytics/** — Snapshots mensais (Apify)
- **content/** — Posts agendados
- **devotionals/** — Devocionais do projeto
- **strategies/** — Planos de conteúdo

### `/content/`
- **devotionals/** — Base de devocionais compartilhada
- **strategies/** — Estratégias gerais e calendário editorial
- **templates/** — Links para Figma templates

### `/scripts/`
- **fetch-social-stats.js** — Coleta analytics (multi-projeto)
- **schedule-posts.js** (futura) — Publica posts agendados
- **generate-devotionals.js** (futura) — Gera devocionais com IA

### `/data/`
- **snapshots/** — Histórico de analytics
- **posts-scheduled/** — Fila de publicação
- **devotionals/** — Base histórica

---

## 🔄 Automação (GitHub Actions)

| Workflow | Trigger | O que faz |
|---|---|---|
| monthly-snapshot.yml | 1º do mês, 8h BRT | Coleta analytics (Apify) |
| daily-devotional.yml | Todo dia, 6h BRT | Publica devocional agendado |
| social-posting.yml | A cada 2h | Publica posts na hora certa |

---

## 🎨 Dados Estruturados

### Analytics Snapshot
```markdown
---
data: 2026-08-28
tipo: snapshot_mensal
tt_seguidores: 2200
tt_views: 10300
ig_seguidores: 1023
---

## 📊 Agosto 2026
...
```

### Post Agendado
```markdown
---
titulo: "Corri 21km!"
plataformas: [tiktok, instagram]
data: 2026-09-10T18:00:00
status: scheduled
pilar: corrida
---

Conteúdo do post...
```

### Devocional
```markdown
---
data: 2026-08-28
versículo: "João 3:16"
tema: fé
---

## Reflexão
...
```

---

## 🔐 Segurança

Secrets GitHub (Settings > Secrets > Actions):
- `APIFY_TOKEN` — Apify API
- `META_ACCESS_TOKEN` — Instagram/Threads
- `TIKTOK_ACCESS_TOKEN` — TikTok
- `YOUTUBE_API_KEY` — YouTube

**Nunca commit credenciais!** Use `.env` ou GitHub Secrets.

---

## 📚 Documentação

| Documento | Conteúdo |
|---|---|
| [ESTRUTURA.md](ESTRUTURA.md) | Guia completo da organização |
| [CONVERSA.md](CONVERSA.md) | Histórico técnico do projeto |
| [PORTFOLIO.md](PORTFOLIO.md) | Portfolio pessoal |
| **config.json** | Configuração por projeto |

---

## 🎯 Roadmap

### Curto Prazo (Próximas 2 semanas)
- [ ] Reorganizar estrutura (FEITO ✅)
- [ ] Criar config.json por projeto
- [ ] Dashboard agregador
- [ ] Estratégia de conteúdo Q4

### Médio Prazo (Próximas 8 semanas)
- [ ] Schedule posts (Buffer ou direto)
- [ ] IA para gerar devocionais
- [ ] Social listening
- [ ] Previsões de growth (ML)

### Longo Prazo (6+ meses)
- [ ] App mobile
- [ ] Integração com todas plataformas
- [ ] Community management tools
- [ ] E-learning (cursos de conteúdo)

---

## 💡 Exemplos de Uso

### Ver analytics de um projeto
```bash
cd projects/bomfim1710
cat analytics/2026-08-28.md  # Último snapshot
```

### Listar todos os posts agendados
```bash
ls -la data/posts-scheduled/
```

### Criar novo devocional
```bash
cp content/devotionals/_template.md content/devotionals/2026-09-01.md
# Editar arquivo
git add content/devotionals/2026-09-01.md
git commit -m "feat: add devotional for 2026-09-01"
```

### Adicionar novo projeto
```bash
cp -r projects/_project-template projects/meu-novo-projeto
# Editar config.json e estrutura
```

---

## 🤝 Contribuindo

1. **Crie um novo projeto:** `cp -r projects/_project-template projects/seu-projeto`
2. **Edite config.json** com suas plataformas e configurações
3. **Faça commit:** `git commit -m "feat: add project 'seu-projeto'"`
4. **Push:** `git push origin main`

---

## 📞 Suporte

- 📖 [Documentação completa](ESTRUTURA.md)
- 🎬 [Exemplo de projeto](projects/bomfim1710/)
- 💬 Issues no GitHub

---

## 📄 Licença

MIT — Livre para usar e modificar

---

**Última atualização:** 28 de agosto de 2026  
**Versão:** 1.0 (reorganização estrutural)  
**Mantido por:** Claude Code + João Marcos Bomfim
