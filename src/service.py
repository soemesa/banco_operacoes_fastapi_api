from sqlalchemy.exc import IntegrityError

from src.models import Conta
from src.schemas import TransacaoSaida, Transacao


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
            return TransacaoSaida(status='error', message='Número de conta existente')
        except Exception as err:
            return TransacaoSaida(status='error', message=f'{err}')

        return TransacaoSaida(status='created', message='Número de conta adicionado com sucesso!')

    @staticmethod
    def buscar_transacao(numero_de_conta, response, session):
        conta = session.query(Conta).filter(Conta.numero_de_conta == numero_de_conta).first()

        if not conta:
            response.status_code = 404
            return TransacaoSaida(status='error', message=f'Número de conta {numero_de_conta} não encontrado')

        return Transacao(id=conta.id, numero_de_conta=conta.numero_de_conta, valor=conta.valor)

    @staticmethod
    def atualizar_transacao(numero_de_conta, response, transacao, session):
        conta = session.query(Conta).filter(Conta.numero_de_conta == numero_de_conta).first()

        if not conta:
            response.status_code = 404
            return TransacaoSaida(status='error', message=f'Número de conta {numero_de_conta} não encontrado')

        conta.numero_de_conta = transacao.numero_de_conta
        conta.valor = transacao.valor

        session.commit()
        session.refresh(conta)

        return TransacaoSaida(status='modified', message='Conta atualizada com sucesso!')

    @staticmethod
    def apagar_transacao(numero_de_conta, response, session):
        conta = session.query(Conta).filter(Conta.numero_de_conta == numero_de_conta).first()

        if not conta:
            response.status_code = 404
            return TransacaoSaida(status='error', message=f'Número de conta {numero_de_conta} não encontrado')

        session.delete(conta)
        session.commit()

        return TransacaoSaida(status='deleted', message=f'Conta deletada')
