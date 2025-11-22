from fastapi import FastAPI
from typing import List
from .models.corrida_model import Corrida
from .database.mongo_client import corridas_collection
from .database.redis_client import redis_client
from .producer import publicar_evento_corrida

app = FastAPI(title="TransFlow - corridas urbanas")

@app.post("/corridas", tags=["Corridas"])
async def cadastrar_corrida(corrida: Corrida):
    corridas_collection.insert_one(corrida.model_dump())
  
    await publicar_evento_corrida(corrida.model_dump())

    return {"message": "Corrida cadastrada e evento publicado"}

@app.get("/corridas",tags=["Corridas"])
def listar_corridas() -> List[dict]:
    corridas = list(corridas_collection.find({}, {"_id": 0}))
    return corridas

@app.get("/corridas/{forma_pagamento}",tags=["Listar por forma de pagamento"])
def listar_corridas_por_pagamento(forma_pagamento: str) -> List[dict]:
    corridas = list(
        corridas_collection.find(
            {"forma_pagamento": forma_pagamento},
            {"_id": 0},
        )
    )
    return corridas

@app.get("/saldo/{motorista}",tags=["Ver saldo do motorista"])
def consultar_saldo(motorista: str):
    chave = f"saldo:{motorista.lower()}"
    saldo = redis_client.get(chave)
    if saldo is None:
        saldo = 0.0
    return {"motorista": motorista, "saldo": float(saldo)}
