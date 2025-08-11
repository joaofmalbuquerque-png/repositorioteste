#iury

from fastapi import FastAPI
from model.aporte_model import Base
from db.session import engine
from rest.controller.aporte_controller import router as aporte_router

app = FastAPI(
    title="API de Aportes",
    description="Gerenciamento de aportes Obras Camel e seus parceiros",
    version="1.0.0"
)

# Criação das tabelas no banco (se ainda não existirem)
Base.metadata.create_all(bind=engine)

# Registro dos endpoints da API
app.include_router(aporte_router)




