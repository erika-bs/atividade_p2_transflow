import os
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue
from .database.redis_client import redis_client
from .database.mongo_client import corridas_collection

RABBIT_URL = os.getenv("RABBIT_URL", "amqp://guest:guest@rabbitmq:5672/")
broker = RabbitBroker(RABBIT_URL)
app = FastStream(broker)

QUEUE_NAME = "corridas_finalizadas"

@broker.subscriber(QUEUE_NAME)
async def processar_corrida(mensagem: dict):
    motorista_nome = mensagem["motorista"]["nome"].lower()
    valor_corrida = float(mensagem["valor_corrida"])

    chave = f"saldo:{motorista_nome}"
    redis_client.incrbyfloat(chave, valor_corrida)

    corridas_collection.update_one(
        {"id_corrida": mensagem["id_corrida"]},
        {"$set": mensagem},
        upsert=True,
    )
