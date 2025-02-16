from app.models.webhook.postback import Postback
from app.socket.socket_manager import ws_manager
from app.message.message_service import MessageService  

async def handle_postback(self :MessageService ,postback: Postback, sender_id: str, is_page: bool):
    ws_manager.send_message("message")
    print("Postback" + postback.title)
    pass