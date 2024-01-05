from pydantic import BaseModel


class TransacaoEntrada(BaseModel):
    numero_de_conta: int
    valor: float


class TransacaoSaida(BaseModel):
    status: str
    message: str


class Transacao(BaseModel):
    id: int
    numero_de_conta: int
    valor: float


class TransacoesList(BaseModel):
    transacoes_list: list[Transacao]
