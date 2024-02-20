from fastapi import FastAPI, HTTPException
from strenum import HttpHeaderCaseStrEnum
from .database import supabase

from api.models.user import User

app = FastAPI()

@app.post("/api/user/register")
def create_user(user: User):
    try:
        res = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password,
            "options": {
                "data": {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            }
        })
        return res
    except:
        raise HTTPException(status_code=500, detail="Failed to create user")

@app.post('/api/user/login')
def login_user(user: User):
    try:
        data = supabase.auth.sign_in_with_password({
            "email": user.email,
            "password": user.password
        })
        return data
    except:
        raise HTTPException(status_code=500, detail="failed to log in")
