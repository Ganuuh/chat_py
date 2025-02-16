from fastapi import  HTTPException, Query


async def verify_webhook(
    hub_mode: str = Query(..., alias="hub.mode"),
    hub_verify_token: str = Query(..., alias="hub.verify_token"),
    hub_challenge: int = Query(..., alias="hub.challenge")
):
    verify_token = "my_verify_token"
    
    if hub_mode == "subscribe" and hub_verify_token == verify_token:
        return hub_challenge
    else:
        raise HTTPException(status_code=403, detail="Verification failed")

