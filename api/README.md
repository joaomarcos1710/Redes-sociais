# Social Hub API

API REST com **FastAPI** para gerenciar tarefas, posts e devocionais de múltiplos projetos de redes sociais.

🚀 **Status:** Pronto para desenvolvimento  
📚 **Docs:** http://localhost:8000/docs (Swagger)  
🔧 **Framework:** FastAPI + SQLAlchemy + SQLite

---

## ⚡ Quick Start

### 1. Instalar dependências
```bash
cd api
pip install -r requirements.txt
```

### 2. Rodar servidor
```bash
python main.py
# ou
uvicorn main:app --reload
```

Acesse:
- **API:** http://localhost:8000
- **Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 📋 Endpoints Principais

### Criar Tarefa
```bash
POST /tarefas
Content-Type: application/json

{
  "titulo": "Postar sobre corrida",
  "descricao": "Post sobre 21km da Meia Maratona",
  "projeto": "bomfim1710",
  "tipo": "post",
  "status": "todo",
  "prioridade": "high",
  "data_vencimento": "2026-09-10T18:00:00",
  "plataformas": "tiktok,instagram,threads",
  "data_publicacao": "2026-09-10T18:00:00",
  "conteudo_preview": "Corri 21km! 🏃",
  "tags": "corrida,maratona"
}
```

### Listar Tarefas
```bash
GET /tarefas?projeto=bomfim1710&status=todo&pagina=1&limite=20
```

### Obter Tarefa
```bash
GET /tarefas/1
```

### Atualizar Tarefa
```bash
PUT /tarefas/1
Content-Type: application/json

{
  "status": "in_progress",
  "notas": "Editando no Figma"
}
```

### Atualizar Status
```bash
PATCH /tarefas/1/status/done
```

### Deletar Tarefa
```bash
DELETE /tarefas/1
```

### Estatísticas
```bash
GET /tarefas/projeto/bomfim1710/stats
```

Retorna:
```json
{
  "total_tarefas": 15,
  "por_status": {
    "todo": 8,
    "in_progress": 4,
    "done": 3,
    "canceled": 0
  },
  "por_tipo": {
    "post": 10,
    "devotional": 3,
    "content_plan": 2,
    "analytics": 0,
    "other": 0
  },
  "por_prioridade": {
    "low": 2,
    "medium": 8,
    "high": 4,
    "urgent": 1
  },
  "vencidas": 2,
  "vencimento_hoje": 1
}
```

### Tarefas Vencidas
```bash
GET /tarefas/projeto/bomfim1710/vencidas
```

### Próximas Tarefas (7 dias)
```bash
GET /tarefas/projeto/bomfim1710/proximas?dias=7
```

---

## 📊 Modelos de Dados

### Task
```python
{
  "id": 1,
  "titulo": "Postar sobre corrida",
  "descricao": "...",
  "projeto": "bomfim1710",
  "tipo": "post",           # post, devotional, content_plan, analytics, other
  "status": "todo",         # todo, in_progress, done, canceled
  "prioridade": "high",     # low, medium, high, urgent
  "data_criacao": "2026-08-28T10:00:00",
  "data_vencimento": "2026-09-10T18:00:00",
  "data_conclusao": null,
  "plataformas": "tiktok,instagram",
  "data_publicacao": "2026-09-10T18:00:00",
  "conteudo_preview": "Corri 21km! 🏃",
  "versículo": null,
  "tema": null,
  "tags": "corrida,maratona",
  "atribuido_a": "João",
  "notas": "Editando no Figma",
  "url_figma": "https://...",
  "url_github": "https://..."
}
```

---

## 🔧 Tipos de Dados

### TaskType
- `post` — Post para redes sociais
- `devotional` — Devocional
- `content_plan` — Plano de conteúdo
- `analytics` — Analytics/relatório
- `other` — Outro

### TaskStatus
- `todo` — A fazer
- `in_progress` — Em andamento
- `done` — Concluído
- `canceled` — Cancelado

### TaskPriority
- `low` — Baixa
- `medium` — Média
- `high` — Alta
- `urgent` — Urgente

---

## 📁 Estrutura

```
api/
├── main.py              # App FastAPI
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── database.py          # Database setup
├── routes/
│   ├── __init__.py
│   └── tarefas.py       # CRUD endpoints
├── requirements.txt
├── tarefas.db          # SQLite database (auto-criado)
└── README.md
```

---

## 🚀 Exemplos de Uso

### Python (requests)
```python
import requests

BASE_URL = "http://localhost:8000"

# Criar tarefa
response = requests.post(
    f"{BASE_URL}/tarefas",
    json={
        "titulo": "Novo post",
        "projeto": "bomfim1710",
        "tipo": "post",
        "plataformas": "tiktok,instagram"
    }
)
tarefa = response.json()
print(f"Tarefa criada: {tarefa['id']}")

# Listar
tarefas = requests.get(
    f"{BASE_URL}/tarefas",
    params={"projeto": "bomfim1710", "status": "todo"}
).json()

# Atualizar status
requests.patch(
    f"{BASE_URL}/tarefas/{tarefa['id']}/status/done"
)
```

### cURL
```bash
# Criar
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Novo post",
    "projeto": "bomfim1710",
    "tipo": "post"
  }'

# Listar
curl "http://localhost:8000/tarefas?projeto=bomfim1710&status=todo"

# Stats
curl "http://localhost:8000/tarefas/projeto/bomfim1710/stats"
```

---

## 🔌 Integração com Repositório

### Estrutura Esperada
```
projects/bomfim1710/
├── config.json
├── content/
│   ├── posts-agendados.json  ← Sync com /tarefas
│   └── devotionals.json      ← Sync com /tarefas
└── analytics/
    └── 2026-08-28.md         ← Gerar via API
```

### Sync Posts com Git
```bash
# Exportar tarefas agendadas
python scripts/export-tasks.py --projeto bomfim1710 --tipo post

# Resultado: projects/bomfim1710/content/posts-agendados.json
```

---

## 🧪 Testes

```bash
# (Adicionar testes em breve)
pip install pytest pytest-httpx

python -m pytest tests/ -v
```

---

## 🛠️ Próximas Features

- [ ] Autenticação JWT
- [ ] Upload de arquivos (imagens, PDFs)
- [ ] Webhooks (publicar quando tarefa = done)
- [ ] Integração com GitHub Issues
- [ ] Integração com Buffer API
- [ ] Export para Notion/Obsidian
- [ ] WebSocket para atualizações real-time
- [ ] Rate limiting
- [ ] Caching (Redis)

---

## 📚 Documentação Automática

A documentação interativa está disponível em:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Todos os endpoints incluem exemplos de request/response.

---

## ⚙️ Configuração

### Variáveis de Ambiente (.env)
```bash
DATABASE_URL=sqlite:///./tarefas.db
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

### Database
SQLite é padrão (ideal para desenvolvimento).  
Para produção, use PostgreSQL:
```bash
DATABASE_URL=postgresql://user:pass@localhost/social_hub
```

---

## 📝 License

MIT — Livre para usar e modificar

---

**Última atualização:** 28 de agosto de 2026  
**Versão:** 1.0.0 (MVP)
