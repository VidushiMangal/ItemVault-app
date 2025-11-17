from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def root():
    return ("Your Fast API server is running")