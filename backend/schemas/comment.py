from pydantic import BaseModel

class CommentSchema(BaseModel):
    content: str

class CommentSongSchema(CommentSchema):
    songId: str