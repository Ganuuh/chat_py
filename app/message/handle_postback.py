from app.models.webhook.postback import Postback
from app.socket.socket_manager import   WebSocketManager
async def handle_postback(postback: Postback, sender_id: str, is_page: bool   , ws_manager  : WebSocketManager ):
    # ws_manager.send_message("message")
    print("Postback" + postback.payload)
    
    pass