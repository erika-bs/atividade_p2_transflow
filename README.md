# TransFlow – Sistema de Corridas com FastAPI, MongoDB, Redis e RabbitMQ

Este projeto implementa um protótipo de backend para gerenciamento de corridas urbanas utilizando:

- FastAPI
- MongoDB (persistência de corridas)
- Redis (saldo dos motoristas)
- RabbitMQ + FastStream (processamento assíncrono de eventos)

O objetivo é simular o fluxo completo de uma corrida sendo cadastrada, enviada como evento e processada de forma assíncrona.

## Como rodar o projeto

### 1 - Pré-requisitos: ter o Docker instalado
https://www.docker.com/products/docker-desktop/

### 2 - Abrir o Docker Desktop

### 3 - Subir os containers
dentro da pasta transflow rode:
```bash 
docker-compose up --build 
```

e aguarde até que esses serviços estejam rodando:

- transflow_app
- transflow_consumer
- transflow_rabbit
- transflow_mongo
- transflow_redis

## Principais Endpoints
Acesse o Swagger:
http://localhost:8000/docs

### 1. Cadastrar corrida

POST /corridas

Exemplo:
![screenshot do cadastro de corridas](images/cadastrar_corrida.png)
![screenshot corrida cadastrada](images/corrida_cadastrada.png)

Ao cadastrar, o sistema:

1. Salva a corrida no MongoDB
2. Publica o evento no RabbitMQ
3. O consumer recebe o evento
4. Atualiza o saldo do motorista no Redis

### 2. Listar corridas

GET /corridas

Retorna todas as corridas salvas no MongoDB.
Exemplo:
![screenshot das corridas](images/listar_corridas.png)

### 3. Filtrar por forma de pagamento

GET /corridas/{forma_pagamento}

Exemplo:
![screenshot das corridas filtradas pela forma de pagamento](images/filtrar_por_pagamento.png)

### 4. Ver saldo do motorista

GET /saldo/{motorista}

Exemplo:
![screenshot do saldo do motorista filtrado pelo nome](images/saldo.png)

## Screenshots do sistema

### Containers rodando
![screenshot dos containers rodando](images/containers.png)

### Swagger
![screenshot swagger](images/swagger.png)

### RabbitMQ
![screenshot rabbit](images/rabbit.png)

### Visualização de saldo no Redis
![screenshot saldo reddis](images/saldos.png)
