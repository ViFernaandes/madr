import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from madrs.schemas import (
    LivroPatch,
    LivroSchema,
    LivrosDB,
    LivrosList,
    LivrosPublic,
    Message,
)

database = []

router = APIRouter(prefix='/livro', tags=['livro'])
logging.basicConfig(level=logging.INFO)


@router.post('/', status_code=HTTPStatus.CREATED, response_model=LivrosPublic)
def create_livro(livro: LivroSchema):
    livro_with_id = LivrosDB(id=len(database) + 1, **livro.model_dump())

    database.append(livro_with_id)

    return livro_with_id


@router.get('/{id}', response_model=LivrosPublic)
def read_livro(id: int):
    if id > len(database) or id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    livros_with_id = database[id - 1]
    return livros_with_id


@router.get('/', response_model=LivrosList)
def read_livros(titulo: str | None = None, ano: int | None = None):
    livros_totais = database
    logging.info(f'Result Banco de Dados: {livros_totais}')
    if titulo:
        livros_titulo = [
            livro for livro in livros_totais if titulo in livro.titulo
        ]
        return {'livros': livros_titulo}

    if ano:
        livros_ano = [livro for livro in livros_totais if ano == livro.ano]
        return {'livros': livros_ano}


@router.patch('/{id}', response_model=LivroSchema)
def update_livro(id: int, livro_patch: LivroPatch):
    if id > len(database) or id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    livro_atual = database[id - 1]

    livro_atualizado = LivrosDB(
        id=livro_atual.id,
        ano=livro_patch.ano,
        titulo=livro_atual.titulo,
        romancista_id=livro_atual.romancista_id,
    )

    database[id - 1] = livro_atualizado

    return livro_atualizado


@router.delete('/{livro_id}', response_model=Message)
def delete_livro(livro_id: int):
    if livro_id > len(database) or livro_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    del database[livro_id - 1]

    return {'message': 'Livro deletado no MADR'}
