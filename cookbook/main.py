import uvicorn
from fastapi import FastAPI

from cookbook.routers import ingredient_router, recipe_router

app = FastAPI(title="Cookbook API", version="1.0.0")


@app.get("/")
def home():
    return {"ok": True}


app.include_router(ingredient_router.router)
app.include_router(recipe_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
