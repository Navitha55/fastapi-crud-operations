from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def greet():
    return {"Status":"Welcome to FastAPI"}

products = [
    Products(id=1,name="Laptop",description="Budget Laptop", price=99, quantity=1),
    Products(id=2,name="Phone",description="Budget Phone", price=29, quantity=30),
    Products(id=3,name="Chair",description="Budget Chair", price=91, quantity=20),
    Products(id=4,name="Table",description="Budget Table", price=91, quantity=11)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product(id:int):
    for prod in products:
        if prod.id == id:
            return prod
    return {"Status":"Product Not Found"}

@app.post("/product")
def add_product(prod:Products):
    products.append(prod)
    return {"Status":"Added Succesfully"}

@app.put("/product")
def update_product(id:int,prod:Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = prod
            return {"Status":"Updated Succesfully"}
    return {"Status":"Product not found"}

from typing import Optional

@app.patch("/product/{id}")
def edit_product(id: int,name: Optional[str] = None,description: Optional[str] = None,price: Optional[float] = None,quantity: Optional[int] = None,):
    for i in range(len(products)):
        if products[i].id == id:
            if name is not None:
                products[i].name = name
            if description is not None:
                products[i].description = description
            if price is not None:
                products[i].price = price
            if quantity is not None:
                products[i].quantity = quantity
            return {"Status": "Updated Successfully"}
    return {"Status": "Product not found"}


@app.delete("/product/{id}")
def delete_product(id:int):
    for i in range(len(products)):
            if products[i].id == id:
                del products[i]
                return {"Status":"Deleted Succesfully"}
    return {"Status":"Product not found"}