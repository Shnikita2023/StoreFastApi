from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from .models import Product
from .shemas import CreateProduct, GetProduct

router_products = APIRouter(
    prefix="/product",
    tags=["Products"]
)


@router_products.get("/get/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    """Получение продукта"""
    try:
        result = await session.get(Product, product_id)
        return result

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router_products.post("/add/")
async def add_product(new_product: CreateProduct, session: AsyncSession = Depends(get_async_session)):
    """Добавление нового продукта"""
    try:
        stmt = insert(Product).values(**new_product.dict())
        result = await session.execute(stmt)
        await session.commit()

        return {
            "status": "succeses",
            "data": f"product {new_product.name} added",
            "details": None
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router_products.delete("/delete/{product_id}")
async def delete_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    """Удаление продукта"""
    try:
        find_product = await session.get(Product, product_id)
        if find_product:
            stmt = delete(Product).where(Product.id == product_id)
            await session.execute(stmt)
            await session.commit()
            return {
                "status": "succeses",
                "data": f"product {find_product.name} removed",
                "details": None
            }

        return {"message": "Продукт не найден"}

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
