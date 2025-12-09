from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def root():
    return {'example': 'Exemplo', 'data': 0}

@app.get('/random')
async def get_random():
    rn = random.randint(0, 100)
    return {'random': rn, 'limit': 100}


@app.get('/random/{limit}')
async def get_random(limit:int):
    rn = random.randint(0, limit)
    return {'random': rn, 'limit': limit}