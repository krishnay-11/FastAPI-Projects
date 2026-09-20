from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Food Order Service",
    description=(
        "Internal API for managing orders"
        "Handle creation, tracking of delivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    # FastAPI converts this dict into JSON
    return {"message": "Welcome to swiggy Order service", "status": "healthy"}

@app.get("/about")
def about():
    """Returns API metadata"""
    return {
        "service": "order-service",
        "team":"backend platform",
        "region": "ap-south-1",
        "version": "1.2.2"
    }

@app.get("/orders")
def list_orders():
    """List recernt orders"""
    return {
        "orders": [
            {"id": 1, "item": "Butter Chicken", "status":"delivered" },
            {"id": 2, "item": "Masala Dosa", "status":"preparing" },
            {"id": 3, "item": "Paneer Tikka", "status":"delivered" },
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get order status"""
    return {
        "total_today": 2_340_23,
        "top_city": "Bengaluru"
    }

@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspect the raw request object"""
    return {
        "method":request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }

@app.get(
    "/orders/active",
    summary="Get Active Orders",
    description=(
        "Returns all orders that are currently being prepared"
        "or are out for delivery"
    ),
    tags=["orders"],
    response_description="List of active order objects",
    deprecated=False
)
def get_active_order():
    """This docstring also apprears in docs"""
    return {
        "active_orders": [
            {"id": 1, "item": "Masala Dosa", "status":"out_for_delivery"}
        ]
    }

@app.get("/restaurants", tags=["Restaurants"])
def list_restro():
    """another docstring for another endpoint"""
    return {
        "restaurants": [
            {"test": "test"}
        ]
    }
@app.get("/restaurants/delhi", tags=["Restaurants"])
def list_restro_delhi():
    """another docstring for another endpoint"""
    return {
        "restaurants": [
            {"test": "test"}
        ]
    }


# if __name__ == "__main__":
#     uvicorn.run(
#         "01-fastapi-foundations:app",
#         host="127.0.0.1",
#         port=8000,
#         reload=True
#     )