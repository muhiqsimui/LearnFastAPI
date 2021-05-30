from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return [
        {
            "name": "RS UMUM DAERAH  DR. ZAINOEL ABIDIN",
            "address": "JL. TGK DAUD BEUREUEH, NO. 108 B. ACEH",
            "region": "KOTA BANDA ACEH, ACEH",
            "phone": "(0651) 34565",
            "province": "Aceh"
        },
        {
            "name": "RS UMUM DAERAH CUT MEUTIA KAB. ACEH UTARA",
            "address": "JL. BANDA ACEH-MEDAN KM.6 BUKET RATA LHOKSEUMAWE",
            "region": "KOTA LHOKSEUMAWE, ACEH",
            "phone": "(0645) 46334",
            "province": "Aceh"
        },
        {
            "name": "RSUP SANGLAH",
            "address": "JL. DIPONEGORO DENPASAR BALI",
            "region": "KOTA DENPASAR, BALI",
            "phone": "(0361) 227912",
            "province": "Bali"
        }
    ]


@app.get("/items/{item_id}")
def read_item():
    return {"item_id": item_id, "q": q}
