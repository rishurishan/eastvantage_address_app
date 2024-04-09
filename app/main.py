# app/main.py
from fastapi import FastAPI
from api.address import router as address_router
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

# Include API routes
app.include_router(address_router, prefix="/api/v1")

# Define custom route for Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Address Book API")

# Define endpoint to expose OpenAPI schema
@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()
