from fastapi import FastAPI

from madrs.routers import contas

app = FastAPI()

app.include_router(contas.router)
