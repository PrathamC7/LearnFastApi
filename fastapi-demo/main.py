from fastapi import FastAPI
from extensions import engine, sessionLocal
from models.Product import Base, Product
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",      # Keep this if you still want to test locally
    "http://15.206.90.28",        # The public IP of your deployed React frontend
    "http://15.206.90.28:3000",   # Include the port if your React app runs on a specific port (e.g., 3000)
    # "https://yourdomain.com",   # Add your domain later if you buy one
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)


@app.get("/products")
def product():

    db = sessionLocal()

    products = db.query(Product).all()

    db.close()

    return products
 

     