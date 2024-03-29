import logging
from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.responses import Response

from src.database import get_session
from src.models import Conta
from src.schemas import TransacaoEntrada, TransacaoSaida, Transacao, TransacoesList
from src.service import Service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/', summary='Welcome world')
def welcome() -> str:
    return 'Hello world'


@router.get('/transacoes', response_model=TransacoesList, status_code=200)
def read_transacoes(session: Session = Depends(get_session)):
    transacoes = session.scalars(select(Conta)).all()
    lista = []
    for transacao in transacoes:
        lista.append(Transacao(id=transacao.id, numero_de_conta=transacao.numero_de_conta, valor=transacao.valor))

    return TransacoesList(transacoes_list=lista)


@router.get('/transacoes/{numero_de_conta}', response_model=Transacao | TransacaoSaida, status_code=200)
def read_transacao(numero_de_conta: int, response: Response, session: Session = Depends(get_session)):
    service = Service()
    conta = service.buscar_transacao(numero_de_conta, response, session)

    return conta


@router.post('/transacoes', response_model=TransacaoSaida, status_code=201)
def create_transacao(response: Response, transacao: TransacaoEntrada, session: Session = Depends(get_session)):
    service = Service()
    nova_transacao = service.inserir_transacao(response, transacao, session)

    return nova_transacao


@router.put('/transacoes/{numero_de_conta}', response_model=TransacaoSaida, status_code=200)
def update_transacao(numero_de_conta: int, response: Response, transacao: TransacaoEntrada,
                     session: Session = Depends(get_session)):
    service = Service()
    nova_conta = service.atualizar_transacao(numero_de_conta, response, transacao, session)

    return nova_conta


@router.delete('/transacoes/{numero_de_conta}', response_model=TransacaoSaida, status_code=200)
def delete_transacao(numero_de_conta: int, response: Response, session: Session = Depends(get_session)):
    service = Service()
    transacao = service.apagar_transacao(numero_de_conta, response, session)

    return transacao
