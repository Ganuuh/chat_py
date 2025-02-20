from fastapi import FastAPI
from .config import settings
from app.routes.route import create_route
from app.socket.socket_manager import ws_manager
import uvicorn
import asyncio


app =  FastAPI()
router  =  create_route()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    ws_manager.refresh_task = asyncio.create_task(ws_manager.refresh_token_and_connect())
    # asyncio.create_task(ws_manager.listen_messages())

@app.on_event("shutdown")
async def shutdown_event():
    if ws_manager.refresh_task:
        ws_manager.refresh_task.cancel()
    await ws_manager.close()

if __name__ == "__main__":
    uvicorn.run("app.main:app" , host=settings.app_host , port=settings.app_port ,  reload=settings.reload)
