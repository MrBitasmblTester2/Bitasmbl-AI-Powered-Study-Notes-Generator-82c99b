from fastapi import FastAPI
from .routers import notes
from .middleware import add_cors

def create_app() -> FastAPI:
    app = FastAPI()
    add_cors(app)
    app.include_router(notes.router)
    return app