class FacebookResponse:
    def __init__(self,data):
       self.recipient_id= data.get("recipient_id")  
       self.message_id= data.get("message_id")
     