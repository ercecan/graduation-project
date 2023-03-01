from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def read_root():
    return {"Hello": "ms"}


@app.post("/test")
def read_root():
    return {"Hello": "ms"}
