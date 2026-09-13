from fastapi import FastAPI

app = FastAPI(
    title = "Products API",
    version = "2.0.1"
)

@app.get("/")
def root() :
    return "Application is running"