import os
from faststream.rabbit import RabbitBroker

RABBIT_URL = os.getenv("RABBIT_URL", "amqp://guest:guest@localhost:5672/")
broker = RabbitBroker(RABBIT_URL)

QUEUE_NAME = "corridas_finalizadas"

async def publicar_evento_corrida(dados_corrida: dict):
    await broker.connect()
    await broker.publish(dados_corrida, queue=QUEUE_NAME)
    await broker.close()
