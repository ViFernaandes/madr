from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from madrs.schemas import ContaDB, ContaList, ContaPublic, ContaSchema, Message

database = []

router = APIRouter(prefix='/conta', tags=['conta'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ContaPublic)
def create_conta(conta: ContaSchema):
    conta_with_id = ContaDB(id=len(database) + 1, **conta.model_dump())

    database.append(conta_with_id)

    return conta_with_id


@router.get('/', response_model=ContaList)
def read_contas():
    return {'contas': database}


@router.put('/{conta_id}', response_model=ContaPublic)
def update_conta(conta_id: int, conta: ContaSchema):
    if conta_id > len(database) or conta_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    conta_with_id = ContaDB(id=len(database) + 1, **conta.model_dump())
    database[conta_id - 1] = conta_with_id

    return conta_with_id


@router.delete('/{conta_id}', response_model=Message)
def delet_conta(conta_id: int):
    if conta_id > len(database) or conta_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Conta not found'
        )

    del database[conta_id - 1]

    return {'message': 'Conta Deleted'}
