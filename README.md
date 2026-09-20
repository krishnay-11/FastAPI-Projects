# 01 Menu API

- Built a read-only menu API using FastAPI.
- Provides chai, snacks, and combo menu items.
- Supports filtering menu items by category.
- Provides an endpoint to fetch individual items by ID.
- Uses Pydantic models for data validation and structured responses.

# 02 Pincode check API

- Built a FastAPI-based API for Indian PIN code lookup and validation.
- Validates PIN codes and returns city, state, and district details.
- Supports bulk lookup of up to 20 PIN codes in a single request.
- Uses custom exception handlers for invalid and unavailable PIN codes.
- Uses Pydantic models for data validation and structured API responses.

# 03 Theatre review API

- Built a FastAPI-based REST API for managing theatre reviews.
- Supports creating, viewing, updating, and deleting reviews.
- Allows filtering reviews by play name.
- Provides average ratings and total review counts for plays.
- Uses SQLModel with SQLite for database operations.

# 04 FastAPI foundations
- **main.py — Introduction to FastAPI with a basic application, GET endpoint, JSON response, and Uvicorn server configuration.
- **fastapi-foundations — Covers multiple API routes, request objects, path/query parameters, API metadata, tags, and automatic Swagger/OpenAPI documentation.
- **restapi-basics — Introduces REST API concepts with GET and POST methods, path parameters, query parameters, in-memory data storage, and basic resource creation and retrieval.