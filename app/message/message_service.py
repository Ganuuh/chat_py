from  app.message.handle_postback import handle_postback
from app.models.webhook.postback import Postback
from app.controller.facebook import FacebookRequest
from app.config import Settings
from app.socket.socket_manager import ws_manager   
class MessageService():
    def __init__(self):
       self.facebook_request = FacebookRequest()
       self.settings =  Settings()
       self.socket =  ws_manager
    # process_received_postback
    async def process_received_postback(self, postback: Postback, sender_id: str, is_page: bool):
     await self.facebook_request.send_plain_text("Test message" ,  sender_id)
     await handle_postback(self,postback,sender_id , is_page)
     pass