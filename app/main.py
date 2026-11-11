from fastapi import FastAPI

app = FastAPI(
    title= "Enterprise Management API",
    description = "API for managing enterprise",
    version = "1.0.0",
)

@app.get("/")
def start():
    return {
        "message": "Enterprise Management API",
        "status": "Working"
    }

@app.get("/health")
def check_status():
    return{
        "status": "Healthy"
    }