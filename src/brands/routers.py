from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from .models import Brand
from .shemas import GetBrand, CreateBrand

router_brands = APIRouter(
    prefix="/brand",
    tags=["Brands"]
)


@router_brands.get("/get/{brand_id}")
async def get_brand(brand_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение бренда"""
    try:
        result = await session.get(Brand, brand_id)
        return result

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router_brands.post("/add/")
async def add_brand(new_brand: CreateBrand, session: AsyncSession = Depends(get_async_session)):
    """Добавление нового бренда"""
    try:
        stmt = insert(Brand).values(**new_brand.dict())
        result = await session.execute(stmt)
        await session.commit()

        return {
            "status": "succeses",
            "data": f"brend {new_brand.name} added",
            "details": None
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router_brands.delete("/delete/{brand_id}")
async def delete_brand(brand_id: int, session: AsyncSession = Depends(get_async_session)):
    """Удаление бренда"""
    try:
        find_brand = await session.get(Brand, brand_id)
        if find_brand:
            stmt = delete(Brand).where(Brand.id == brand_id)
            await session.execute(stmt)
            await session.commit()
            return {
                "status": "succeses",
                "data": "brand removed",
                "details": None
            }

        return {"message": "Бренд не найден"}

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
