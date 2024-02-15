from pydantic import BaseModel

class ModifieSongSchema(BaseModel):
    modifiedName: str
    genre: str|None = None