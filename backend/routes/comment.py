from fastapi import HTTPException, APIRouter, status, UploadFile, Depends, Query, Path, Body
from fastapi.responses import JSONResponse
from typing import Annotated
from dependencies.oauth import oauth_check
from dependencies.query import validate_sort_by
from config.database_mongodb import AsyncIOMotorDatabase, get_db
from models.mongodb import convert_object_id_to_str
from schemas.comment import CommentSongSchema
from bson import ObjectId
from datetime import datetime, timezone, timedelta

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('/song', status_code=status.HTTP_201_CREATED)
async def comment_song(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], comment_body: Annotated[CommentSongSchema, Body()], token: Annotated[dict, Depends(oauth_check)]):
    userId = ObjectId(token['userId'])

    comment_data = {
        'songId': ObjectId(comment_body.songId),
        'userId': userId,
        'content': comment_body.content,
        "createdAt": datetime.now(timezone.utc),
        "updatedAt": datetime.now(timezone.utc),
        "expireAt": datetime.now(timezone.utc) + timedelta(days=7)
    }
    result = await db.comments.insert_one(comment_data)
    add_comment_count = await db.files.find_one_and_update({'_id': ObjectId(comment_body.songId)}, {'$inc': {'commentCount': 1}})
    doc = await db.comments.find_one({'_id': result.inserted_id})
    return await convert_object_id_to_str(doc)

@router.get('/song/{song_id}')
async def comment_song_list(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], song_id: Annotated[str, Path()], limit: Annotated[int, Query(ge=1, le=100)] =20, skip: Annotated[int, Query(ge=0)] =0, orderBy: Annotated[str, Query()] ='createdAt', sortBy: Annotated[int, Depends(validate_sort_by)] =-1):
    pipeline = [
        {
            '$match': {'songId': ObjectId(song_id)}
        },
        {
            '$lookup': {
                'from': 'userData',
                'localField': 'userId',
                'foreignField': 'userId',
                'as': 'user'
            }
        },
        {
            '$addFields': {
                'user': { '$arrayElemAt': ['$user', 0] }
            }
        },
        {
            '$sort': {orderBy: sortBy}
        },
        {
            '$skip': skip
        },
        {
            '$limit': limit
        },
        {
            '$project': {
                'userId': 0,
                'user': {
                    '_id': 0,
                    'email': 0,
                    'age': 0,
                    'userId': 0,
                    'createdAt': 0,
                    'updatedAt': 0
                }
            }
        }
    ]
    cursor = db.comments.aggregate(pipeline)
    result = await cursor.to_list(limit)
    return await convert_object_id_to_str(result)