import requests

async def get_access_token():
    request_body = {"test" : "test"}
    response  =  await  requests.post("test" , json=request_body)
    response.json()
    return response.get("token")