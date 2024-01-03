import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/', summary='Welcome world')
def welcome() -> str:
    return 'Hello world'


@router.post('/post_exemplo')
def post_exempo():
    # hacer todo lo quieras con esa entrada
    return {'post': 'testando'}
