from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

products_list = [
        {"id": 1, "name": "Product 1", "price": 10.99},
        {"id": 2, "name": "Product 2", "price": 19.99},
        {"id": 3, "name": "Product 3", "price": 5.99}
    ]

@router.get("/")
async def products():
    return products_list    

@router.get("/{id}")
async def product(id: int):
    for product in products_list:
        if product["id"] == id:
            return product
    return {"error": "Product not found"}

@router.post("/")
async def create_product(product: dict):
    products_list.append(product)
    return product  

@router.put("/{id}")
async def update_product(id: int, updated_product: dict):
    for index, product in enumerate(products_list):
        if product["id"] == id:
            products_list[index] = updated_product
            return updated_product
    return {"error": "Product not found"}   

@router.delete("/{id}")
async def delete_product(id: int):
    for index, product in enumerate(products_list):
        if product["id"] == id:
            deleted_product = products_list.pop(index)
            return deleted_product
    return {"error": "Product not found"}