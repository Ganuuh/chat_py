from datetime import datetime 
async def router_default_handler():
    date =  datetime.now()
    return {"message": "Endpoint does not exist or wrong" ,  "time_stamp" :date }