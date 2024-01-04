import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
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



@router.post('/transacoes', response_model=TransacaoSalida, status_code=201)
def create_transacao(response: Response, transacao: TransacaoEntrada, session: Session = Depends(get_session)):
    try:
        db_transacao = session.scalar(
            select(Conta).where(Conta.numero_de_conta == transacao.numero_de_conta)
        )

        if db_transacao:
            response.status_code = 400
            raise HTTPException(
                status_code=400, detail='Número de conta ja existe'
            )

        db_transacao = Conta(
            numero_de_conta=transacao.numero_de_conta, valor=transacao.valor
        )
        session.add(db_transacao)
        session.commit()
        session.refresh(db_transacao)
    except Exception as err:
        return TransacaoSalida(status='error', message=f'{err}')


    return TransacaoSalida(status='created', message='O registro foi criado com sucesso!')