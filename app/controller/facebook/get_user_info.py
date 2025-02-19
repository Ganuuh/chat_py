from app.config import settings
import httpx

class PictureData:
    def __init__(self, data):
        self.height = data.get("height")
        self.width = data.get("width")
        self.url = data.get("url")
        self.is_silhouette = data.get("is_silhouette")

class ProfilePicture:
    def __init__(self, data):
        self.data = PictureData(data.get("data", {}))

class User:
    def __init__(self, data):
        self.id = data.get("id")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.name = data.get("name")
        self.picture = ProfilePicture(data.get("picture", {}))

async def get_user_info(sender_id: str) -> User:
    end_point = f"{settings.GRAPH_BASE_URL}/{sender_id}?fields=first_name,last_name,name,picture&access_token={settings.PAGE_ACCESS_TOKEN}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(end_point)

        if response.status_code == 200:
            return User(response.json())  # ✅ Convert JSON to User object

        print("Error in getting user information!", response.status_code, response.text)
        return User({})  # ✅ Return an empty User object to avoid errors
