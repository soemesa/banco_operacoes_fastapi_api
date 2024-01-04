from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseModel


class Conta(BaseModel):
    __tablename__ = "transacoes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    numero_de_conta: Mapped[int] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    valor: Mapped[float] = mapped_column(nullable=False)
