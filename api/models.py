from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class TaskStatus(str, enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELED = "canceled"


class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TaskType(str, enum.Enum):
    POST = "post"
    DEVOTIONAL = "devotional"
    CONTENT_PLAN = "content_plan"
    ANALYTICS = "analytics"
    OTHER = "other"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=True)
    projeto = Column(String(50), nullable=False, index=True)  # Ex: bomfim1710, meu-negocio
    tipo = Column(SQLEnum(TaskType), default=TaskType.OTHER)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.TODO, index=True)
    prioridade = Column(SQLEnum(TaskPriority), default=TaskPriority.MEDIUM)

    # Datas
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_vencimento = Column(DateTime, nullable=True, index=True)
    data_conclusao = Column(DateTime, nullable=True)

    # Relacionado a posts
    plataformas = Column(String(255), nullable=True)  # Ex: "tiktok,instagram,threads"
    data_publicacao = Column(DateTime, nullable=True, index=True)
    conteudo_preview = Column(Text, nullable=True)

    # Relacionado a devocionais
    versículo = Column(String(255), nullable=True)
    tema = Column(String(100), nullable=True)

    # Tags
    tags = Column(String(255), nullable=True)  # Ex: "corrida,fé,lifestyle"

    # Metadata
    atribuido_a = Column(String(100), nullable=True)
    notas = Column(Text, nullable=True)
    url_figma = Column(String(500), nullable=True)
    url_github = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<Task(id={self.id}, titulo={self.titulo}, status={self.status})>"
