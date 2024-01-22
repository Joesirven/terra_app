from fastapi import FastAPI, Depends, Request, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
import httpx
import os
from dotenv import load_dotenv
import workos
from workos import client as workos_client

app = FastAPI()

load_dotenv()

workos_client_id = os.getenv('WORKOS_CLIENT_ID')
workos_api_key = os.getenv('WORKOS_API_KEY')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/itmes/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/api")
async def root():
    return {"message": "Hello World"}


@app.get("/api/callback")
async def callback(request: Request):
    auth_code = request.query_params.get("code")
    if not auth_code:
        raise HTTPException(
            status_code=400,
            detail="Authorization code is missing"
        )

    try:
        user_info = workos_client.user_management.get_profile_and_token(
            auth_code, workos_client.client_id
        )
        # Further processing with user_info like creating user session, etc.

        return RedirectResponse(url='http://localhost:3000/home')
    except Exception as e:
        print(f"Error during authentication: {e}")
        raise HTTPException(status_code=500, detail="Failed to authenticate user")


@app.get("/auth/login")
async def login():
    authorization_url = client.user_management.get_authorization_url(
        connection_id="conn_01E4ZCR3C56J083X43JQXF3JK5",
        redirect_uri="https://your-app.com/callback",
        state="dj1kUXc0dzlXZ1hjUQ==",
    )

    return RedirectResponse(
        url=authorization_url
    )
