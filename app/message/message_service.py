from  app.message.handle_postback import handle_postback
from app.models.webhook.postback import Postback
from app.controller.facebook import FacebookRequest
from app.utils.utils import Utils
from app.config import Settings
from app.socket.socket_manager import ws_manager
from typing import List
import copy
class MessageService():
    def __init__(self):
       self.facebook_request = FacebookRequest()
       self.settings =  Settings()
       self.socket =  ws_manager
       self.utils = Utils()
    # process_received_postback
    async def get_json(self, payload : str ,  sender_id : str  ) -> List[object]:
      response  = await  self.utils.get_json_body(payload ,  sender_id)
      return response
       
    async def process_received_postback(self, postback: Postback, sender_id: str, is_page: bool):
     json  =  await self.get_json(payload=postback.payload ,  sender_id=sender_id)
     await self.send_message_jsons(jsons=json,sender_id=sender_id)
     
    #  await handle_postback(postback,sender_id , is_page ,  ws_manager=self.socket)
     pass
    
    
    async def send_message_jsons(self,jsons : List[object] ,sender_id  :str):
      for each_json in jsons:
       cloned_json = copy.deepcopy(each_json)
       fixed_josn =  self.utils.remove_json_type(cloned_json)
       response = await self.facebook_request.send_json_body(fixed_josn) 
       await self.socket.send_message_to_crm(sender_id=sender_id,  
                                       json_body=each_json, 
                                       message_content=None,
                                       message_id=response.message_id,
                                       content_type="JSON",
                                       replied_to=None,
                                       is_guest=False,
                                       is_auto=True)

                                       
        
      
      

message_service =  MessageService()