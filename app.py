from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from src.brands.routers import router_brands
from src.categories.routers import router_categories
from src.products.routers import router_products

app = FastAPI()

app.include_router(router_brands)
app.include_router(router_products)
app.include_router(router_categories)



@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")