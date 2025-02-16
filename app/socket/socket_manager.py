import websockets
import asyncio
import httpx
from datetime import datetime, timedelta
from app.config import Settings

settings = Settings()

class WebSocketManager:
    def __init__(self):
        self.token = None
        self.expiry_time = None
        self.refresh_task = None
        self.ws = None

    async def get_new_token(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    settings.CRM_END_POINT,
                    json={
                        "password": settings.CRM_PASSWORD,
                        "username": settings.CRM_USER_NAME,
                        "deviceName": "Chat bot",
                        "platformName": "Chat bot",
                        "serial": "serial_number",
                        "systemCode": "CRM",
                    }
                )
                data = response.json()
                self.token = data['token']
                self.expiry_time = datetime.now() + timedelta(hours=1)
                return self.token
        except Exception as e:
            print(f"Error getting token: {e}")
            return None

    async def connect_socket(self):
        if self.token:
            try:
                if self.ws:
                    await self.ws.close()
                
                ws_url = f"{settings.socket_end_point}&token=Bearer%20{self.token}"
                print(f"Connecting to: {ws_url}")
                
                self.ws = await websockets.connect(
                    ws_url,
                    ping_interval=30,  # Keep connection alive
                    ping_timeout=10
                )
                print("Connected to WebSocket server!")
                
                # Start listening for messages
                asyncio.create_task(self.listen_messages())
            except Exception as e:
                print(f"WebSocket connection error: {e}")

    async def listen_messages(self):
        try:
            while True:
                if self.ws:
                    message = await self.ws.recv()
                    print(f"Received message: {message}")
        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed")
        except Exception as e:
            print(f"Error in message listening: {e}")

    async def refresh_token_and_connect(self):
        while True:
            await self.get_new_token()
            await self.connect_socket()
            
            if self.expiry_time:
                now = datetime.now()
                sleep_duration = (self.expiry_time - now - timedelta(minutes=5)).total_seconds()
                if sleep_duration > 0:
                    await asyncio.sleep(sleep_duration)

    async def close(self):
        if self.ws:
            await self.ws.close()


    async def send_message(self ,  message :str):
        print("message")


ws_manager = WebSocketManager()