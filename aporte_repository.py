from sqlalchemy.orm import Session
from model.aporte_model import Aporte
from rest.dto.AporteCreateDTO import AporteCreateDTO
from typing import Optional, List
import pandas as pd

def criar_aporte(db: Session, aporte_dto: AporteCreateDTO) -> Aporte:
    novo_aporte = Aporte(
        DATA=aporte_dto.DATA,
        CAMEL=aporte_dto.CAMEL,
        HECA=aporte_dto.HECA
    )
    db.add(novo_aporte)
    db.commit()
    db.refresh(novo_aporte)
    return novo_aporte

def buscar_aporte_por_id(db: Session, aporte_id: int) -> Optional[Aporte]:
    return db.query(Aporte).filter(Aporte.id == aporte_id).first()

def listar_aportes(db: Session) -> List[Aporte]:
    return db.query(Aporte).all()

def list_todos_aportes(db: Session):

    return pd.read_sql_query("SELECT * FROM aporte", db)