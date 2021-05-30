from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {1: {"nama": "muhammad iqbal", "job": "mahasiswa"}}


@app.get("/rujukan/{get_kota}")  # path parameter
def rujukan(get_kota):
    if(get_kota == "bandung"):
        return {"kota": get_kota, "rujukan": "rumah sakit muhammadiyah"}
    elif(get_kota == "surabaya"):
        return {"kota": get_kota, "rujukan": "poli surabaya"}
    else:
        return {"kota": get_kota}


@app.get("/rujukan/")  # query parameter
async def rujukan_query(number: int, text: Optional[str] = None):
    return {"number": number, "text": text}
# cara pakai http://127.0.0.1:8000/rujukan/?number=4&text=hellodunia
