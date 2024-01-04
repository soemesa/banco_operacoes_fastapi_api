from pydantic import BaseModel


class TransacaoEntrada(BaseModel):
    numero_de_conta: int
    valor: float


class TransacaoSalida(BaseModel):
    status: str
    message: str


class TransacaoList(BaseModel):
    transacoes: list[TransacaoSalida]

