import httpx
from .get_user_info import get_user_info
from app.config import settings
from typing import Dict, Any
from  app.utils.utils import utils

class FacebookResponse:
    def __init__(self, data: Dict[str, Any]):
        self.recipient_id = data.get("recipient_id")  
        self.message_id = data.get("message_id")

class FacebookRequest:
    async def read_message_from_crm(self,content_type : str , facebook_id : str ,  text_conversation :str):
        json_body={}
        match content_type:
            case "TEXT": 
                json_body={"recipient": {
            "id": facebook_id
          },
          "message": {
            "text": text_conversation
          }}
            case "IMAGE":
                file_url = f"https://gateway.invescore.mn/fs-dev/file/get-file?filename={text_conversation}" 
                json_body={
          "recipient": {
            "id": facebook_id
          },
          "message": {
            "attachment": {
              "type": "image",
              "payload": {
                "url": file_url,
                "is_reusable": false
              }
            }
          }
        }
        await self.send_message_request(body=json_body)
        print("text conversation")
        pass
    async def get_user_info(self, sender_id: str):
        return await get_user_info(sender_id)

    async def send_message_request(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """Sends a message request to Facebook API and returns JSON response."""
        base_url = f"{settings.GRAPH_BASE_URL}/me/messages?access_token={settings.PAGE_ACCESS_TOKEN}"
        
        async with httpx.AsyncClient() as client:
            response = await client.post(base_url, json=body)
            return response.json()  # This returns a dictionary

    async def send_plain_text(self, text: str, sender_id: str):
        """Send a plain text message to the user."""
        request_body = {
            "recipient": {"id": sender_id},
            "message": {"text": text}
        }
        await self.send_message_request(request_body)

    async def send_json_body(self, json_body: Dict[str, Any]) -> FacebookResponse:
        response_data = await self.send_message_request(json_body)
        
        if not isinstance(response_data, dict):
            raise ValueError("Invalid response from Facebook API")
        
        return FacebookResponse(response_data)  # ✅ Properly create a response object
