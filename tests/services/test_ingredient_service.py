import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from cookbook.exceptions import AlreadyExistsError, NotFoundError
from cookbook.models import Ingredient
from cookbook.repositories.ingredient_repository import IngredientRepository
from cookbook.schemas.ingredient import IngredientCreate
from cookbook.services.ingredient_service import (
    create_ingredient_service,
    delete_ingredient_service,
    get_all_ingredients,
)


# async def test_get_all_ingredients(db: AsyncSession):
#     ing1 = IngredientCreate(name="salt")