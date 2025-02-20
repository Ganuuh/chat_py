import websockets
import asyncio
import httpx
import json
import json
from types import SimpleNamespace
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from app.config import Settings
from app.models.socket.send_message import SendMessage
from app.controller.facebook import FacebookRequest

settings = Settings()


class WebSocketManager:
    def __init__(self):
        self.token = None
        self.expiry_time = None
        self.ws = None
        self.facebook_request = FacebookRequest()

    async def get_new_token(self):
        """Fetch a new token for CRM authentication."""
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
                self.token = data.get("token")
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
                print(f"Connecting to WebSocket: {ws_url}")

                self.ws = await websockets.connect(
                    ws_url, ping_interval=30, ping_timeout=10
                )
                print("Connected to WebSocket server!")

                # Start listening for messages
                asyncio.create_task(self.listen_messages())
            except Exception as e:
                print(f"WebSocket connection error: {e}")

    async def listen_messages(self):
        """Continuously listen for messages from the WebSocket."""
        try:
            while True:
                if self.ws:
                    message = await self.ws.recv()
                    print(f"Received message: {message}")
                    json_body =  json.loads(message)
                    chat_body ={}
                    if "chat" in json_body:
                        chat_body = SimpleNamespace(**json_body["chat"])
                    if chat_body:
                         await self.facebook_request.read_message_from_crm(
                                  content_type=chat_body.content_type,  
                                  facebook_id=chat_body.facebook_id,
                                  text_conversation=chat_body.text_conversation)
                         print("There is message !")
        except websockets.exceptions.ConnectionClosed:
            print("WebSocket connection closed")
        except Exception as e:
            print(f"Error in message listening: {e}")

    async def refresh_token_and_connect(self):
        """Refresh token periodically and reconnect WebSocket."""
        while True:
            await self.get_new_token()
            await self.connect_socket()

            if self.expiry_time:
                now = datetime.now()
                sleep_duration = (self.expiry_time - now - timedelta(minutes=5)).total_seconds()
                if sleep_duration > 0:
                    await asyncio.sleep(sleep_duration)

    async def close(self):
        """Close the WebSocket connection."""
        if self.ws:
            await self.ws.close()

    async def send_message_to_crm(
        self,
        sender_id: str,
        json_body: Optional[Dict[str, Any]],
        message_content: Optional[str],
        message_id: str,
        content_type: str,
        replied_to: Optional[str],
        is_guest: bool,
        is_auto: bool,
    ) -> None:
        """Send a message to the CRM via WebSocket."""
        try:
            user_info = await self.facebook_request.get_user_info(sender_id)

            if not user_info:
                print("Error: Unable to fetch user info.")
                return

            facebook = f"{user_info.first_name} {user_info.last_name}"

            message_body = SendMessage(
                facebook_id=sender_id,
                facebook=facebook,
                first_name=user_info.first_name,
                last_name=user_info.last_name,
                text_conversation=message_content,
                conversation="Чатаар холбогдсон",
                inbox_id=message_id,
                lead_source="MESSENGER",
                content_type=content_type, 
                file_names=json_body,
                fb_reply_id=replied_to,
                is_guest=is_guest,
                lead_type="CHAT",
                lead_status="NEW",
                is_auto=is_auto,
                is_seen=False,
            )

            message_body_string = message_body.to_json()
            print(f"Message body string  : {message_body_string}")

            if self.ws:
                await self.ws.send(message_body_string)
                print("Message sent to CRM WebSocket.")
            else:
                print("WebSocket connection is not established.")
        
        except Exception as e:
            print(f"Error sending message to CRM: {e}")


# Create a single instance of WebSocketManager
ws_manager = WebSocketManager()
