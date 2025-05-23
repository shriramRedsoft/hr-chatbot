from fastapi import FastAPI
from fast_api.routes.query import router

app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)