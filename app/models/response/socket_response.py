class ResponseFromSocket:
    def __init__(self , data):
        self.facebook_id = data.get("facebook_id")
        self.content_type = data.get("content_type")
        self.text_conversation = data.get("text_conversation")