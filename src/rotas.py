import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import Response

from src.database import get_session
from src.models import Conta
from src.schemas import TransacaoEntrada, TransacaoSalida, TransacaoList

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
    try:
        db_transacao = Conta(
            numero_de_conta=transacao.numero_de_conta, valor=transacao.valor
        )
        session.add(db_transacao)
        session.commit()
        session.refresh(db_transacao)
    except IntegrityError:
        return TransacaoSalida(status='error', message='Número de conta existente')
    except Exception as err:
        return TransacaoSalida(status='error', message=f'{err}')


    return TransacaoSalida(status='created', message='Número de conta adicionado com sucesso!')