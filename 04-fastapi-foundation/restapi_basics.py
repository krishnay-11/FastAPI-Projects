from fastapi import FastAPI
from starlette import status
import uvicorn

app = FastAPI(
    title="Zomato Food service API",
    description="Learning HTTP methods through a food delivery context",
    version="1.0.0"
)

# in-memory data store for example

restaurants_db = {
    1: {"id": 1, "name": "Biryani Blues", "city": "Delhi", "rating": 4.3,
        "cuisine": "Hyderabadi", "is_active": True},
    2: {"id": 2, "name": "Saravana Bhavan", "city": "Chennai", "rating": 4.6,
        "cuisine": "South Indian", "is_active": True},
    3: {"id": 3, "name": "Bademiya", "city": "Mumbai", "rating": 4.1,
        "cuisine": "Mughlai", "is_active": True},
    4: {"id": 4, "name": "Karim's", "city": "Delhi", "rating": 4.5,
        "cuisine": "Mughlai", "is_active": False},
}

orders_db = {}
next_order_id = 1

@app.get(
    "/restaurants",
    tags=["Restaurants"],
    summary="List all restaurants",
    response_description="A list of restaurants objects"
)
def list_restaurants():
    """GET for listing - return a collection"""
    return {
        "restaurants": list(restaurants_db.values()),
        "count": len(restaurants_db)
    }


@app.get(
    "/restaurants/{restaurant_id}",
    tags=["Restaurants"],
    summary="Get restaurant by id",
    
)
def get_restaurant(restaurant_id: int):
    """Get for details"""
    if restaurant_id not in restaurants_db:
        return {"error": "Restaurant not found", "id": restaurant_id}
    return restaurants_db[restaurant_id]


# POST: create a new order

@app.post(
    "/orders",
    tags=["Orders"],
    summary="Place a new order",
    description="Creates a new food order",
    status_code=status.HTTP_201_CREATED,
    response_description="The newly created order"
)
def create_order(restaurant_id: int, items: str)
    """
    POST creates a new resource
    REAL App - body would be Pydantic model

    """
    global next_order_id
    order = {
        "id": next_order_id,
        "restaurant_id": restaurant_id,
        "items": items.split(","),
        "status": "placed",
        "total": 0
    }
    orders_db[next_order_id] = order
    next_order_id += 1
    return order


@app.post(
    "/restaurants",
    tags=["Restaurants"],
    status_code=201
)
def add_restaurants(name: str, city: str, cuisine: str):
    new_id = max(restaurants_db.keys()) + 1 if restaurants_db else 1
    restaurant = {
        "id": new_id,
        "name": name,
        "city": city,
        "cuisine": cuisine,
        "is_active": True
    }
    restaurants_db[new_id] = restaurant
    return restaurant

