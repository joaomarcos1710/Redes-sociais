from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from database import init_db
from routes import tarefas
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database
init_db()

# Create FastAPI app
app = FastAPI(
    title="Social Hub API",
    description="API REST para gerenciar tarefas, posts e devocionais de múltiplos projetos de redes sociais",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tarefas.router)


@app.get("/")
def root():
    """Endpoint raiz da API"""
    return {
        "message": "Social Hub API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    """Health check"""
    return {"status": "ok", "message": "API rodando"}


@app.get("/info")
def info():
    """Informações sobre a API"""
    return {
        "name": "Social Hub API",
        "description": "Gerenciar tarefas, posts e devocionais",
        "version": "1.0.0",
        "endpoints": {
            "tarefas": "/tarefas",
            "docs": "/docs",
            "redoc": "/redoc",
        },
        "features": [
            "CRUD de tarefas",
            "Filtros por projeto, status, tipo, prioridade",
            "Paginação",
            "Estatísticas",
            "Tarefas vencidas",
            "Próximas tarefas",
        ],
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handler global para exceções"""
    logger.error(f"Erro não tratado: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno do servidor"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
