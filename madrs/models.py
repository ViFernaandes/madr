from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]


@table_registry.mapped_as_dataclass
class Livro:
    __tablename__ = 'livros'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    ano: Mapped[str]
    titulo: Mapped[str] = mapped_column(unique=True)
    id_romancista: Mapped[int] = mapped_column(ForeignKey('romancistas.id'))
    autoria: Mapped['Romancista'] = relationship(
        init=False, back_populates='livros'
    )


@table_registry.mapped_as_dataclass
class Romancista:
    __tablename__ = 'romancistas'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    livros: Mapped[list['Livro']] = relationship(
        init=False, back_populates='romancista', cascade='all, delete-orphan'
    )
