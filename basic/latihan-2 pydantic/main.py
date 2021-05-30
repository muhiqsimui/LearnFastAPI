from typing import Optional
from fastapi import FastAPI

# pydantic
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
def index():
    return {"name": "iqbal"}


class Package(BaseModel):
    kota: str
    nama_rs: str
    alamat: Optional[str] = None

# http://127.0.0.1:8000/docs#/default/make_package_package__post


@app.post("/package/")
async def make_package(package: Package):
    return package
