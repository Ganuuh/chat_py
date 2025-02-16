from .get_user_info import get_user_info
import requests
from app.config import settings
class FacebookRequest:
    async def get_user_info(sender_id :str):
     await   get_user_info(sender_id)

    async def send_message_request(self,body :object):
       base_url = f"{settings.GRAPH_BASE_URL}/me/messages?access_token={settings.PAGE_ACCESS_TOKEN}"
       await  requests.post(base_url , json=body)
    
    async def send_plain_text(self,text:str ,  sender_id  :str):
       request_body={
          "recipient": {
            "id": sender_id
          },
          "message": {
            "text": text
          }
       }    
       await self.send_message_request(request_body)
