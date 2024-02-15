from fastapi import HTTPException, APIRouter, status, UploadFile, Depends, Query, Path, Body
from fastapi.responses import ORJSONResponse, StreamingResponse
from typing import Annotated
from dependencies.oauth import oauth_check
from config.database_mongodb import AsyncIOMotorDatabase, get_db
from models.mongodb import convert_object_id_to_str
from schemas.song import ModifieSongSchema
from bson import ObjectId
from datetime import datetime, timezone, timedelta
from mutagen.mp3 import MP3
from io import BytesIO

router = APIRouter(
    prefix='/file',
    tags=['file']
)

@router.post('/song', status_code=status.HTTP_201_CREATED)
async def upload_file(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], file: UploadFile, token: Annotated[dict, Depends(oauth_check)]):
    userId = ObjectId(token['userId'])
    # save file
    if file.content_type != 'audio/mpeg':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{'msg': 'File content error.'}]
        )
    elif file.size > 10*1024*1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{'msg': 'File size too large.'}]
            
        )
    else:
        contents = await file.read()

        audio = MP3(BytesIO(contents))
        duration_seconds = audio.info.length

        file_data = {
            "userId": userId,
            "originalName": file.filename,
            "modifiedName": file.filename,
            "size": file.size,
            "duration": duration_seconds,
            "content": contents,
            "contentType": file.content_type,
            "commentCount": 0,
            "createdAt": datetime.now(timezone.utc),
            "updatedAt": datetime.now(timezone.utc),
            "expireAt": datetime.now(timezone.utc) + timedelta(days=7)
        }
        result = await db.files.insert_one(file_data)
    doc = await db.files.find_one({'_id': result.inserted_id}, {'content': 0})
    return await convert_object_id_to_str(doc)

@router.get('/userSongs')
async def list_user_files(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], token: Annotated[dict, Depends(oauth_check)], limit: Annotated[int, Query(ge=1, le=100)] =20, skip: Annotated[int, Query(ge=0)] =0):
    userId = ObjectId(token['userId'])
    
    cursor = db.files.find({'userId': userId}, {'content': 0}).sort({'createdAt': 1}).skip(skip).limit(limit)
    result = await cursor.to_list(limit)
    return await convert_object_id_to_str(result)

@router.get('/songs')
async def list_files(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], limit: Annotated[int, Query(ge=1, le=100)] =20, skip: Annotated[int, Query(ge=0)] =0):
    pipeline = [
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
            '$sort': {'createdAt': 1}
        },
        {
            '$skip': skip
        },
        {
            '$limit': limit
        },
        {
            '$project': {
                'content': 0,
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
    cursor = db.files.aggregate(pipeline)
    result = await cursor.to_list(limit)
    return await convert_object_id_to_str(result)

@router.get('/song/{song_id}')
async def get_file(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], song_id: Annotated[str, Path()]):
    song_id = ObjectId(song_id)
    # result = await db.files.find_one({'_id': song_id}, {'content': 0})
    pipeline = [
        {
            '$match': {'_id': song_id}
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
            '$project': {
                'content': 0,
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
    result = await db.files.aggregate(pipeline).next()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{'msg': 'File no found.'}]
        )
    return await convert_object_id_to_str(result)

@router.patch('/song/{song_id}')
async def update_file(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], token: Annotated[dict, Depends(oauth_check)], song_id: Annotated[str, Path()], data: Annotated[ModifieSongSchema, Body()]):
    userId = ObjectId(token['userId'])

    result = await db.files.find_one_and_update({'userId': userId, '_id': ObjectId(song_id)}, {"$set": data.model_dump()})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{'msg': 'File no found.'}]
        )
    return {
        'detail': [{
            'success': True,
            'msg': 'File updated.'
        }]
    }

@router.delete('/song/{song_id}')
async def delete_file(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], token: Annotated[dict, Depends(oauth_check)], song_id: Annotated[str, Path()]):
    userId = ObjectId(token['userId'])

    result = await db.files.find_one_and_delete({'userId': userId, '_id': ObjectId(song_id)})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{'msg': 'File no found.'}]
        )
    return {
        'detail': [{
            'success': True,
            'msg': 'File deleted.'
        }]
    }

@router.get('/song/{song_id}/play')
async def get_music_file(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)], song_id: Annotated[str, Path()]):
    result = await db.files.find_one({'_id': ObjectId(song_id)})
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{'msg': 'File no found.'}]
        )
    content = result.get('content')
    content_type = result.get('contentType', 'audio/mpeg')

    return StreamingResponse(iter([content]), media_type=content_type)