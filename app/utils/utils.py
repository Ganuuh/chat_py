import requests
from typing import List 


class Utils:
    async def get_json_body(self,payload : str ,  sender_id : str ) -> List[object]:
        response  =  requests.post("https://gateway.invescore.mn/chat-bot/api/webhook"  ,json={
    "object": "app",
    "entry": [
        {
            "time": 234324234324,
            "id": "",
            "messaging": [
                {
                    "sender": {
                        "id": sender_id
                    },
                    "recipient": {
                        "id": ""
                    },
                    "timestamp": 323242343,
                    "postback": {
                        "mid": "",
                        "payload": payload,
                        "title": "Link",
                        "type": ""
                    }
                }
            ]
        }
    ]
})
        if(response.status_code == 200):
            
            return response.json()
        else:
            return [{}]
    
    
    def remove_json_type(self,json: object) -> object:
        if "message" in json and isinstance(json["message"], dict):
            # Remove json_type if it exists
            json["message"].pop("json_type", None)
        
        return json    
    # # Process each element in the list
    #   for item in json:
    #     # Check if message exists and is a dictionary
    #       # Using None as default to avoid KeyError
    
    #   return json
    



utils  =  Utils()