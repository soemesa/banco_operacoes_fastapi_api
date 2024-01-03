from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Float

from src.database import Base


class Conta(Base):
    __tablename__ = "transacoes"

    numero_de_conta: int = Column(Integer, primary_key=True, index=True, nullable=False)
    created_at: datetime = Column(DateTime, nullable=False)
    valor: float = Column(Float, nullable=False)
