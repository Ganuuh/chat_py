from fastapi import  HTTPException, Depends 
from  fastapi.responses import JSONResponse
from app.models.request.webhook import RequestBody
from app.message.message_service import MessageService

message_service =  MessageService()

async def webhook(
    request_body: RequestBody,
):

    print(request_body)
    
    if not request_body.entry:
        raise HTTPException(status_code=400, detail="No entries in request body")
        
    sender_id = request_body.entry[0].messaging[0].sender.id
    print(f"Sender id: {sender_id}")

    # Handle postback
    if postback := request_body.entry[0].messaging[0].postback:
        if request_body.object:
            is_page = request_body.object == "page"
            await message_service.process_received_postback(postback, sender_id, is_page)
        else:
            raise HTTPException(status_code=400, detail="Missing object field")

    # Handle message
    if message := request_body.entry[0].messaging[0].message:
    
        date = request_body.entry[0].messaging[0].timestamp

        # Handle reply with text
        if message.text and message.reply_to:
            await message_service.process_reply_with_text(
                sender_id,
                message.text,
                message.mid,
                message.reply_to.mid
            )

        # Handle reply with attachment
        if message.attachments and message.reply_to:
            await message_service.process_reply_with_attachment(
                sender_id,
                message.attachments,
                message.mid,
                message.reply_to.mid
            )

        # Handle plain text
        if message.text and not message.reply_to:
            if not request_body.object:
                raise HTTPException(status_code=400, detail="Missing object field")
                
            is_page = request_body.object == "page"
            return {}
            await message_service.process_received_message(
                message.text,
                sender_id,
                date,
                message.mid,
                is_page
            )

        # Handle attachment
        if message.attachments and not message.reply_to:
            await message_service.process_received_attachment(
                sender_id,
                message.attachments,
                message.mid
            )

    response  = {"status": "ok"}
    return JSONResponse(content=response)