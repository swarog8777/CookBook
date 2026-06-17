from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from cookbook.database import get_db
from cookbook.exceptions import AlreadyExistsError, NotFoundError
from cookbook.schemas.ingredient import IngredientCreate, IngredientRead
from cookbook.services.ingredient_service import (
    create_ingredient_service,
    delete_ingredient_service,
    get_all_ingredients,
)

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])


@router.get("", summary="Список ингридиентов", response_model=list[IngredientRead])
async def list_ingredients(db: AsyncSession = Depends(get_db)):
    return await get_all_ingredients(db)
