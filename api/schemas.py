from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELED = "canceled"


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TaskType(str, Enum):
    POST = "post"
    DEVOTIONAL = "devotional"
    CONTENT_PLAN = "content_plan"
    ANALYTICS = "analytics"
    OTHER = "other"


class TaskCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=255)
    descricao: Optional[str] = None
    projeto: str = Field(..., min_length=1, max_length=50)
    tipo: TaskType = TaskType.OTHER
    status: TaskStatus = TaskStatus.TODO
    prioridade: TaskPriority = TaskPriority.MEDIUM
    data_vencimento: Optional[datetime] = None
    plataformas: Optional[str] = None
    data_publicacao: Optional[datetime] = None
    conteudo_preview: Optional[str] = None
    versículo: Optional[str] = None
    tema: Optional[str] = None
    tags: Optional[str] = None
    atribuido_a: Optional[str] = None
    notas: Optional[str] = None
    url_figma: Optional[str] = None
    url_github: Optional[str] = None


class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    tipo: Optional[TaskType] = None
    status: Optional[TaskStatus] = None
    prioridade: Optional[TaskPriority] = None
    data_vencimento: Optional[datetime] = None
    plataformas: Optional[str] = None
    data_publicacao: Optional[datetime] = None
    conteudo_preview: Optional[str] = None
    versículo: Optional[str] = None
    tema: Optional[str] = None
    tags: Optional[str] = None
    atribuido_a: Optional[str] = None
    notas: Optional[str] = None
    url_figma: Optional[str] = None
    url_github: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    projeto: str
    tipo: TaskType
    status: TaskStatus
    prioridade: TaskPriority
    data_criacao: datetime
    data_vencimento: Optional[datetime]
    data_conclusao: Optional[datetime]
    plataformas: Optional[str]
    data_publicacao: Optional[datetime]
    conteudo_preview: Optional[str]
    versículo: Optional[str]
    tema: Optional[str]
    tags: Optional[str]
    atribuido_a: Optional[str]
    notas: Optional[str]
    url_figma: Optional[str]
    url_github: Optional[str]

    class Config:
        from_attributes = True


class TaskListResponse(BaseModel):
    total: int
    pagina: int
    items: List[TaskResponse]


class StatsResponse(BaseModel):
    total_tarefas: int
    por_status: dict
    por_tipo: dict
    por_prioridade: dict
    por_projeto: dict
    vencidas: int
    vencimento_hoje: int
