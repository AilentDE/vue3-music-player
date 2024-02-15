from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from config.database_mongodb import connect_to_mongo, close_mongo_connection
from routes import auth, file, comment

app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PATCH', 'DELETE'],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(file.router)
app.include_router(comment.router)

app.add_event_handler('startup', connect_to_mongo)
app.add_event_handler('shutdown', close_mongo_connection)

# base
@app.get('/')
def home():
    return {'success': True}

# uvicorn main:app --reload