from app.config import settings
import requests
async def get_user_info(sender_id  :str) -> object:
    end_point =   f"{settings.GRAPH_BASE_URL}/{sender_id}?fields=first_name,last_name,name,picture&access_token={settings.PAGE_ACCESS_TOKEN}"
    response = await  requests.get(end_point) 
    if response.status_code == 200:
        return response.json()
    else:
        print("Error in getting user information !")
        return {}