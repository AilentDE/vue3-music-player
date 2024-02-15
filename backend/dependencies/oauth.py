from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from utils.jwt import decode_jwt
from config.database_mongodb import AsyncIOMotorDatabase, get_db
from bson import ObjectId

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def oauth_check(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], token: Annotated[str, Depends(oauth2_scheme)]):
    # check token
    payload = decode_jwt(token)
    if payload['userId']:
        # check user
        userId = ObjectId(payload['userId'])
        result = await db.userAuth.find_one({'_id': userId})
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=[{'msg': 'User not found.'}]
            )
        return payload
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=[{'msg': 'Access token error.'}]
        )
    