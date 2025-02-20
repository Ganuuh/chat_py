from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CRM_END_POINT: str= "https://gateway.invescore.mn/oauth2-test/auth/employee"
    CRM_USER_NAME: str ="crm@invescore.mn"
    CRM_PASSWORD:str="03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    PAGE_ACCESS_TOKEN: str = "EAAIgqZAKwyagBO6iTejZBfVH7gXKQLcKFn6WCdcC1KsWMvoNrrxZBIp7azu95OCNzB4aevjhLTj7Hpl9lwdueWFJiiwZCkuK3GNbCRgC3eNARj0BufNHLgHgyRg5OMZBaAmrsfmF0PNyjXoC3vepqzmqFG0im6jTBZC0oVvLyaRQwZCWAptDbtONktqOdlMLSwrGNf9jyio7gZDZD"
    PAGE_ID:int=   370319916169635
    GRAPH_BASE_URL: str = "https://graph.facebook.com/v21.0"
    app_host : str = "0.0.0.0"
    app_port : int = 8000
    reload :  bool = False
    socket_end_point : str = "ws://203.91.116.106:9080/ws/?is_client=true&channel=MESSENGER"
    file_server_url  :str = "https://gateway.invescore.mn/fs-dev/file/upload"
    chat_body_url : str  = "https://gateway.invescore.mn/chat-bot/api/webhook"


settings =  Settings()