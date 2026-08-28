from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime, timedelta
from database import get_db
from models import Task, TaskStatus, TaskPriority, TaskType
from schemas import TaskCreate, TaskUpdate, TaskResponse, TaskListResponse, StatsResponse

router = APIRouter(prefix="/tarefas", tags=["tarefas"])


@router.post("/", response_model=TaskResponse, status_code=201)
def criar_tarefa(tarefa: TaskCreate, db: Session = Depends(get_db)):
    """Criar nova tarefa"""
    nova_tarefa = Task(**tarefa.dict())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa


@router.get("/", response_model=TaskListResponse)
def listar_tarefas(
    db: Session = Depends(get_db),
    projeto: str = Query(None),
    status: TaskStatus = Query(None),
    tipo: TaskType = Query(None),
    prioridade: TaskPriority = Query(None),
    pagina: int = Query(1, ge=1),
    limite: int = Query(20, ge=1, le=100),
):
    """Listar tarefas com filtros"""
    query = db.query(Task)

    # Filtros
    if projeto:
        query = query.filter(Task.projeto == projeto)
    if status:
        query = query.filter(Task.status == status)
    if tipo:
        query = query.filter(Task.tipo == tipo)
    if prioridade:
        query = query.filter(Task.prioridade == prioridade)

    # Ordenar por prioridade + data de vencimento
    query = query.order_by(Task.prioridade.desc(), Task.data_vencimento)

    # Contar total
    total = query.count()

    # Paginação
    offset = (pagina - 1) * limite
    tarefas = query.offset(offset).limit(limite).all()

    return TaskListResponse(total=total, pagina=pagina, items=tarefas)


@router.get("/{tarefa_id}", response_model=TaskResponse)
def obter_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    """Obter tarefa por ID"""
    tarefa = db.query(Task).filter(Task.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@router.put("/{tarefa_id}", response_model=TaskResponse)
def atualizar_tarefa(
    tarefa_id: int, dados: TaskUpdate, db: Session = Depends(get_db)
):
    """Atualizar tarefa"""
    tarefa = db.query(Task).filter(Task.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # Se mudando para DONE, registrar data de conclusão
    if dados.status == TaskStatus.DONE and tarefa.status != TaskStatus.DONE:
        tarefa.data_conclusao = datetime.utcnow()

    # Atualizar campos
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(tarefa, key, value)

    db.commit()
    db.refresh(tarefa)
    return tarefa


@router.delete("/{tarefa_id}", status_code=204)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    """Deletar tarefa"""
    tarefa = db.query(Task).filter(Task.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()


@router.get("/projeto/{projeto}/stats", response_model=StatsResponse)
def stats_projeto(projeto: str, db: Session = Depends(get_db)):
    """Estatísticas de um projeto"""
    tarefas = db.query(Task).filter(Task.projeto == projeto).all()

    if not tarefas:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    # Contar por status
    por_status = {}
    for status in TaskStatus:
        por_status[status.value] = len(
            [t for t in tarefas if t.status == status]
        )

    # Contar por tipo
    por_tipo = {}
    for tipo in TaskType:
        por_tipo[tipo.value] = len([t for t in tarefas if t.tipo == tipo])

    # Contar por prioridade
    por_prioridade = {}
    for prioridade in TaskPriority:
        por_prioridade[prioridade.value] = len(
            [t for t in tarefas if t.prioridade == prioridade]
        )

    # Tarefas vencidas
    agora = datetime.utcnow()
    vencidas = len(
        [
            t
            for t in tarefas
            if t.data_vencimento and t.data_vencimento < agora and t.status != TaskStatus.DONE
        ]
    )

    # Vencimento hoje
    hoje = datetime.utcnow().date()
    vencimento_hoje = len(
        [
            t
            for t in tarefas
            if t.data_vencimento
            and t.data_vencimento.date() == hoje
            and t.status != TaskStatus.DONE
        ]
    )

    return StatsResponse(
        total_tarefas=len(tarefas),
        por_status=por_status,
        por_tipo=por_tipo,
        por_prioridade=por_prioridade,
        por_projeto={projeto: len(tarefas)},
        vencidas=vencidas,
        vencimento_hoje=vencimento_hoje,
    )


@router.patch("/{tarefa_id}/status/{novo_status}", response_model=TaskResponse)
def atualizar_status(
    tarefa_id: int,
    novo_status: TaskStatus,
    db: Session = Depends(get_db),
):
    """Atualizar apenas o status de uma tarefa"""
    tarefa = db.query(Task).filter(Task.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa.status = novo_status

    if novo_status == TaskStatus.DONE:
        tarefa.data_conclusao = datetime.utcnow()

    db.commit()
    db.refresh(tarefa)
    return tarefa


@router.get("/projeto/{projeto}/vencidas", response_model=list[TaskResponse])
def tarefas_vencidas(projeto: str, db: Session = Depends(get_db)):
    """Listar tarefas vencidas de um projeto"""
    agora = datetime.utcnow()
    tarefas = (
        db.query(Task)
        .filter(
            and_(
                Task.projeto == projeto,
                Task.data_vencimento < agora,
                Task.status != TaskStatus.DONE,
            )
        )
        .order_by(Task.data_vencimento)
        .all()
    )
    return tarefas


@router.get("/projeto/{projeto}/proximas", response_model=list[TaskResponse])
def tarefas_proximas(
    projeto: str, db: Session = Depends(get_db), dias: int = Query(7, ge=1, le=30)
):
    """Listar tarefas vencendo nos próximos N dias"""
    agora = datetime.utcnow()
    proxima_data = agora + timedelta(days=dias)

    tarefas = (
        db.query(Task)
        .filter(
            and_(
                Task.projeto == projeto,
                Task.data_vencimento >= agora,
                Task.data_vencimento <= proxima_data,
                Task.status != TaskStatus.DONE,
            )
        )
        .order_by(Task.data_vencimento)
        .all()
    )
    return tarefas
