import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import Response

from src.database import get_session
from src.schemas import TransacaoEntrada, TransacaoSalida, TransacaoList
from src.service import Service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/', summary='Welcome world')
def welcome() -> str:
    return 'Hello world'

# @router.get('/transacoes', response_model=TransacaoList)
# def read_transacoes():
#     return {'transacoes': transacoes}
#
#
# db_transacao = session.scalar(
#             select(Conta).where(Conta.numero_de_conta == transacao.numero_de_conta)
#         )

@router.post('/transacoes', response_model=TransacaoSalida, status_code=201)
def create_transacao(response: Response, transacao: TransacaoEntrada, session: Session = Depends(get_session)):
    service = Service()
    nova_transacao = service.inserir_transacao(response, transacao, session)

    return nova_transacao

