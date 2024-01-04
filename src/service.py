from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import Response

from src.database import get_session
from src.models import Conta
from src.schemas import TransacaoEntrada, TransacaoSalida

class Service:
    @staticmethod
    def inserir_transacao(response, transacao, session):
        try:
            db_transacao = Conta(
                numero_de_conta=transacao.numero_de_conta, valor=transacao.valor
            )
            session.add(db_transacao)
            session.commit()
            session.refresh(db_transacao)
        except IntegrityError:
            response.status_code = 400
            return TransacaoSalida(status='error', message='Número de conta existente')
        except Exception as err:
            return TransacaoSalida(status='error', message=f'{err}')

        return TransacaoSalida(status='created', message='Número de conta adicionado com sucesso!')


