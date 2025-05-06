from fastapi import FastAPI

from madrs.routers import contas, livros, romancistas

app = FastAPI()

app.include_router(contas.router)
app.include_router(livros.router)
app.include_router(romancistas.router)
