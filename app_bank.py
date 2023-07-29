# app2.py
import base64

from fastapi import FastAPI, HTTPException, Request

import ecdsa

app2 = FastAPI(openapi_prefix="/bank")


def verify_ecdsa_signature(signature, data, pk):
    try:
        pk.verify(signature, data)  # Encode data as bytes
        return True  # Signature is valid
    except ecdsa.BadSignatureError:
        return False  # Signature is invalid


# @app2.middleware("http")
# async def verify_signature(request: Request, call_next):
#     signature = request.headers.get("X-Signature")
#     user_id = request.headers.get("X-User-ID")
#
#     if not signature or not user_id:
#         raise HTTPException(status_code=401, detail="Missing X-Signature or X-User-ID header")
#
#     with open(f'keys/{user_id}.pem', 'rb') as f:
#         pk = ecdsa.VerifyingKey.from_pem(f.read().decode('utf-8'))
#
#     data = await request.body()
#
#     signature = signature.encode()
#
#     signature = base64.b64decode(signature)
#
#     # Verify the signature using the ECDSA public key
#     if not verify_ecdsa_signature(signature, data, pk):
#         raise HTTPException(status_code=401, detail="Invalid signature")
#
#     response = await call_next(request)
#     return response


@app2.get("/")
async def root():
    return {"message": "Secure Hello World"}


@app2.get("/get_client_ip/")
def get_client_ip(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}
