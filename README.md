# Fast-API-for-Soft-AI-ML-MLOPs-Cloud
Fast API for Software Development, AI, Machine Learning, Operations, Cloud, Docker and More...


```
.\myenv\Scripts\Activate.ps1
```

### CURD
```
from fastapi import FastAPI
from models import Product
```
```
app = FastAPI()
```
```
@app.get("/")
def greet():
    return {"message": "NS  LONI"}
```

###### Items
```
products = [
    Product(1, "Phone", "Budget Phone-1", 100, 10),
    Product(1, "Phone", "Budget Phone-2", 111, 11)
]
```
## 1. GET
```
@app.get("/products")
def all_product():
    return products
    # return "ALL Products"
```
    
## Get idx[0] data    

```
@app.get("/product")
def getting_by_ID():
    return products[0]
    # return products[2] # Internal Server Error
```

## Dynamic accessing
```
@app.get("/product/{id}")
def getting_items_by_ID(id: int):
    return products[id-1]    
```
```
@app.get("/product/{id}")
def getting_item_by_ID(id: int):
    for item in products:
        if item.id == id:
            return item
    
        return "Not Getting plz add more item Bro..."    
        
```


## 2. ADD
```
@app.post("product")
def add_product(product: Product):
    products.append(product)
    return products
```



## 3. UPDATE
```
@app.put("/product")
def updating_products(id: int, product: Product): # (using: datatype)
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"
    return "Product not pound"    

```

```
@app.delete("/product")
def del_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted Successfully"
    return "Product not Found"    
```    