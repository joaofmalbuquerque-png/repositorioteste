# model/aporte_model.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, BigInteger
from sqlalchemy.orm import relationship
from db.session import Base

class Aporte(Base):
    """
    Modelo para a tabela 'aportes'.
    Um Aporte pertence a uma Obra.
    """
    __tablename__ = "aportes"
    id = Column(BigInteger, primary_key=True, nullable=False, unique=True, index=True)
    data = Column(Date, index=True)
    observacao = Column(String, nullable=True)
    valor = Column(Float, nullable=False)
    status = Column(BigInteger, nullable=False)
    visibilidade = Column(BigInteger, nullable=False)
    tipo = Column(BigInteger, nullable=True)

    # Chaves estrangeiras para a hierarquia
    socio_id = Column(BigInteger, ForeignKey("socios.id"), nullable=False)
    obra_id = Column(BigInteger, ForeignKey("obras.id"), nullable=False)

    # Relações com as tabelas de Obra e Socio
    obra = relationship("Obra", back_populates="aportes")
    socio = relationship("Socio", back_populates="aportes")
