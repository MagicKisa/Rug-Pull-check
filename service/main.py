from fastapi import FastAPI, Depends
from predictor import ScamPredictor
from pydantic import BaseModel
from cryptoapi import get_source_code
from typing import Literal
import requests

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis


base_address = "0x9f589e3eabe42ebc94a44727b3f3531c0c877809"
base_platform = 'BNB'

class CodeItem(BaseModel):
    code: str


class FindItem(BaseModel):
    platform: Literal['BNB', 'Ethereum', 'Fantom', 'Polygon', 'Base', 'Arbitrum', 'Core'] = 'BNB'
    address: str = "0x9f589e3eabe42ebc94a44727b3f3531c0c877809"


app = FastAPI()
model = ScamPredictor()

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


@app.get("/")
async def root():
    """tell if app is up and running"""
    return {"message": "It's up"}


@app.post("/code_predict/")
# @cache(expire=30)
async def predict_by_code(item: CodeItem):
    """predict the activity of crypto project by its code"""

    predicted_label = model.predict(item.code)

    if predicted_label:
        return {"message": f"Данная криптовалюта будет активна"}

    return {"message": f"Данная криптовалюта инактивна"}


@app.post("/predict/")
@cache(expire=30)
async def predict_by_address_and_platform(item: FindItem = Depends()):
    """predict the activity of crypto project based on machine learning model"""
    code = get_source_code(item.address, item.platform)
    predicted_label = model.predict(code)

    if predicted_label:
        return {"message": f"Данная криптовалюта будет активна"}

    return {"message": f"Данная криптовалюта будет инактивна"}

@app.post("/code/")
@cache(expire=30)
async def get_code_by_address_and_platform(item: FindItem = Depends()):
    """requests the contract code by platform and contract address of token"""
    code = get_source_code(item.address, item.platform)
    return {"code": f"{code}"}


#@app.get("/model/")
#async def get_model():
#    """requests the contract code by platform and contract address of token"""
#    code = get_source_code(address, platform)
#    return {"code": f"{code}"}


@app.get("/secret/")
@cache(expire=5)
async def get_secret():
    """requests the compliment"""
    url = "https://tools-api.robolatoriya.com/compliment"
    compliment = requests.get(url).json()['text']

    return {"very importrant message": f"{compliment}"}