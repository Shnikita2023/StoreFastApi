from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.staticfiles import StaticFiles

from redis import asyncio as aioredis

from src.brands.routers import router_brands
from src.categories.routers import router_categories
from src.pages.routers import router_pages
from src.products.routers import router_products
from src.tasks.routers import router_celery

app = FastAPI()

# Подключение статичных файлов
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Регистрация роутеров
app.include_router(router_brands)
app.include_router(router_products)
app.include_router(router_categories)
app.include_router(router_pages)
app.include_router(router_celery)


@app.on_event("startup")
async def startup() -> None:
    """Подключение редиса при старте"""
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
