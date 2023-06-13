from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from .models import Categorie
from .shemas import CreateCategorie, GetCategorie
from fastapi_cache.decorator import cache

router_categories = APIRouter(
    prefix="/categorie",
    tags=["Categories"]
)


@router_categories.get("/get/{categorie_id}", summary='Получение категории')
async def get_categorie(categorie_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        result = await session.get(Categorie, categorie_id)
        return result

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router_categories.get("/get_all/", summary='Получение списка всех категорий', response_model=list[GetCategorie])
@cache(expire=30)
async def get_all_categorie(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Categorie)
        result = await session.execute(query)
        return result.scalars().all()

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router_categories.post("/add/", summary='Добавление категории')
async def add_categorie(new_categorie: CreateCategorie, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Categorie).values(**new_categorie.dict())
        result = await session.execute(stmt)
        await session.commit()

        return {
            "status": "succeses",
            "data": f"product {new_categorie.name} added",
            "details": None
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router_categories.delete("/delete/{categorie_id}", summary='Удаление категории')
async def delete_categorie(categorie_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        find_categorie = await session.get(Categorie, categorie_id)
        if find_categorie:
            stmt = delete(Categorie).where(Categorie.id == categorie_id)
            await session.execute(stmt)
            await session.commit()
            return {
                "status": "succeses",
                "data": f"product {find_categorie.name} removed",
                "details": None
            }

        return {"message": "Категория не найдена"}

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
