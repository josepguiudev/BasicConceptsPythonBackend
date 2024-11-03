from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})

#@router.get("/products")
@router.get("/")
async def products():
    return ["Product1", "Product2", "Product3", "Product4", "Product5"]

#@router.get("/products/{id}")
@router.get("/{id}")
async def products():
    return ["Product1", "Product2", "Product3", "Product4", "Product5"]