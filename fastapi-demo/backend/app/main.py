from fastapi import FastAPI
from app.api.routes.ProductRoute import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(
    router,
    prefix="/products",
    tags=["products"]
)
@app.get("/")
def root():
    return "application started successfully"
