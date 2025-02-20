import requests
from typing import List 
from app.config import settings



class Utils:
    async def upload_to_file_server(self, image_url: str) -> str:
        """Uploads an image to the file server."""
        client = httpx.AsyncClient()

        image_bytes = await self.download_bytes_from_image(image_url)
        if image_bytes is None:
            return None

        token = await self.get_los_token()
        if token is None:
            return None

        form_data = {
            "folder_name": (None, "facebook"),
            "file": ("facebook_image.jpg", image_bytes, "image/jpeg")
        }

        try:
            response = await client.post(
                settings.file_server_url,
                headers={"Authorization": f"Bearer {token}"},
                files=form_data,
            )
            response.raise_for_status()

            file_response = response.json()
            return file_response.get("path")
        except httpx.HTTPError as e:
            print(f"Error in uploading file to the server: {e}")
            return None
        finally:
            await client.aclose()
            
            
            
    async def download_bytes_from_image(self, image_url: str) -> bytes:
        """Downloads image bytes from the given URL."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(image_url)
                response.raise_for_status()
                return response.content
        except httpx.HTTPError as e:
            print(f"Failed to download image: {e}")
            return None
        
    async def get_los_token(self) -> str:
        payload = {
            "username": "buyandelger.s@invescore.mn",
            "password": "1234crm",
            "deviceName": "iPhone X",
            "platformName": "iPhone",  # iPhone or Android
            "serial": "ac:ac:qk",
            "systemCode": "CRM"
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(settings.CRM_END_POINT, json=payload)
                response.raise_for_status()

                token = response.json().get("token")
                return token if token else None
        except httpx.HTTPError as e:
             print(f"Error fetching LOS token: {e}")
             return None
        
    async def get_json_body(self,payload : str ,  sender_id : str ) -> List[object]:
        response  =  requests.post(settings.chat_body_url  ,json={
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