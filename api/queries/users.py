from fastapi import FastAPI, Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
import httpx


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user_by_id(self, user_id: str):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def get_users(self):
        return self.db.query(User).all()

    def create_user(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user):
        self.db.delete(user)
        self.db.commit()
        return user
