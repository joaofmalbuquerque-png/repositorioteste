# service/aporte_service.py
from sqlalchemy.orm import Session
from model.aporte_model import Aporte
from schemas.aporte_schema import AporteCreate
from typing import List, Optional

def criar_aporte_service(db: Session, aporte_data: AporteCreate):
    """
    Cria um novo aporte no banco de dados.
    """
    db_aporte = Aporte(**aporte_data.dict())
    db.add(db_aporte)
    db.commit()
    db.refresh(db_aporte)
    return db_aporte

def listar_aportes_service(db: Session) -> List[Aporte]:
    """
    Retorna a lista de todos os aportes.
    """
    return db.query(Aporte).all()

def obter_aporte_service(db: Session, aporte_id: int) -> Optional[Aporte]:
    """
    Retorna um aporte específico pelo ID.
    """
    return db.query(Aporte).filter(Aporte.id == aporte_id).first()
