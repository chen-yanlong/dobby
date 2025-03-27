from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a route for a dynamic endpoint
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}