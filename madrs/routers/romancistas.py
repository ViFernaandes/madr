import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from madrs.schemas import (
    Message,
    RomancistaDB,
    RomancistaList,
    RomancistaPatch,
    RomancistaPublic,
    RomancistaSchema,
)

database = []

router = APIRouter(prefix='/romancistas', tags=['romancistas'])
logging.basicConfig(level=logging.INFO)


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=RomancistaPublic
)
def create_romancista(romancistas: RomancistaSchema):
    romancista_with_id = RomancistaDB(
        id=len(database) + 1, **romancistas.model_dump()
    )

    database.append(romancista_with_id)

    return romancista_with_id


@router.get('/{id}', response_model=RomancistaPublic)
def read_romancista(id: int):
    if id > len(database) or id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    livros_with_id = database[id - 1]
    return livros_with_id


@router.get('/', response_model=RomancistaList)
def read_romancistas(nome: str | None = None):
    romancista_totais = database

    if nome:
        romancista_nome = [
            romancista
            for romancista in romancista_totais
            if nome in romancista.nome
        ]

        return {'romancistas': romancista_nome}


@router.patch('/{id}', response_model=RomancistaPublic)
def update_romancista(id: int, romancista_patch: RomancistaPatch):
    if id > len(database) or id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    romancista_atual = database[id - 1]

    romancista_atualizado = RomancistaDB(
        id=romancista_atual.id,
        nome=romancista_patch.nome,
    )

    database[id - 1] = romancista_atualizado

    return romancista_atualizado


@router.delete('/{romancista_id}', response_model=Message)
def delete_romancista(romancista_id: int):
    if romancista_id > len(database) or romancista_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    del database[romancista_id - 1]

    return {'message': 'Romancista deletada no MADR'}
