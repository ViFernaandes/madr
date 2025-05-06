from pydantic import BaseModel, EmailStr


class ContaSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class ContaPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class ContaDB(ContaSchema):
    id: int


class ContaList(BaseModel):
    contas: list[ContaPublic]


class Message(BaseModel):
    message: str


class RomancistaSchema(BaseModel):
    nome: str


class RomancistaPublic(BaseModel):
    id: int
    nome: str


class RomancistaList(BaseModel):
    romancistas: list[RomancistaPublic]


class RomancistaDB(RomancistaSchema):
    id: int


class RomancistaPatch(BaseModel):
    nome: str


class LivroSchema(BaseModel):
    ano: int
    titulo: str
    romancista_id: int


class LivrosPublic(BaseModel):
    id: int
    ano: int
    titulo: str
    romancista_id: int


class LivrosList(BaseModel):
    livros: list[LivrosPublic]


class LivrosDB(LivroSchema):
    id: int


class LivroPatch(BaseModel):
    ano: int
