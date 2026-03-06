from fastapi import FastAPI

app = FastAPI()

# Products list
products = [
    {"id": 1, "name": "Smartphone", "price": 20000, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Headphones", "price": 1500, "category": "Accessories", "in_stock": True},
    {"id": 3, "name": "Mouse", "price": 700, "category": "Computer", "in_stock": True},
    {"id": 4, "name": "Monitor", "price": 12000, "category": "Computer", "in_stock": False},

    # Newly added products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Office", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Computer", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Computer", "in_stock": False},
]

# Task 1
@app.get("/products")
def get_products():
    return{
        "products" : products,
        "total" : len(products)
    }

# Task 2  
@app.get("/products/category/{category_name}")
def get_by_category(category_name : str):
    result = [p for p in products if p["category"] == category_name]
    
    if not result:
        return {"error" : "No products found in this category"}
    
    return{
        "category" : category_name,
        "products" : result,
        "total" : len(result)
    }

# Task 3    
@app.get("/products/instock")
def get_instock():
    
    available = [p for p in products if p["in_stock"] == True]
    
    return {
        "in_stock_products": available,
        "count": len(available)
    }

# Task 4    
@app.get("/store/summary")
def store_summary():

    in_stock_count = len([p for p in products if p["in_stock"]])

    out_stock_count = len(products) - in_stock_count

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }
 
# Task 5   
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }
    

# Bonys task    
@app.get("/products/deals")
def get_deals():

    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }