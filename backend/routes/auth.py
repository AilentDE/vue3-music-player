from fastapi import HTTPException, APIRouter, status, Depends, Body
from fastapi.responses import ORJSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from dependencies.oauth import oauth_check
from config.database_mongodb import AsyncIOMotorDatabase, get_db
from schemas.user import UserSchema
from utils.jwt import create_jws
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from bson import ObjectId
from datetime import datetime, timezone


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
async def register_user(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # check user
    result = await db.userAuth.find_one({'username': form_data.username})
    if result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{'msg': 'User exited.'}]
        )
    # create user
    result = await db.userAuth.insert_one({
        'username': form_data.username,
        'password': pwd_context.hash(form_data.password)
    })
    # create user JWS
    encoded_jws, expISO = create_jws({'userId': str(result.inserted_id)})
    return ORJSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "accessToken": encoded_jws,
            "tokenType": "bearer",
            "tokenExpiration": expISO
        }
    )

@router.post('/createUser')
async def create_user(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], user_data: Annotated[UserSchema, Body()], token: Annotated[dict, Depends(oauth_check)]):
    userId = ObjectId(token['userId'])
    # check tos
    if not user_data.tos:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{'msg': 'Must accept the Terms of Service.'}]
        )
    # check user
    result = await db.userData.find_one({'email': user_data.email})
    if result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{'msg': 'User exited.'}]
        )
    # create user data
    result = await db.userData.insert_one({
        **user_data.model_dump(),
        'userId': userId,           
        'createdAt': datetime.now(timezone.utc),
        'updatedAt': datetime.now(timezone.utc)
        })
    return ORJSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={**user_data.model_dump(), 'userId': str(result.inserted_id)}
    )

@router.post('/login')
async def login_user(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # check user
    result = await db.userAuth.find_one({'username': form_data.username})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{'msg': 'User not found.'}]
        )
    # check password
    if not pwd_context.verify(form_data.password, result['password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=[{'msg': 'Wrong password.'}]
        )
    # create user JWS
    encoded_jws, expISO = create_jws({'userId': str(result['_id'])})
    return {
        "accessToken": encoded_jws,
        "tokenType": "bearer",
        "tokenExpiration": expISO
    }