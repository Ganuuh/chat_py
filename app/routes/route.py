from fastapi import APIRouter
from .default import router_default_handler
from .webhook_handler import webhook
from .favicon import favicon
from .webhook import verify_webhook  

def create_route() -> APIRouter:
    router =  APIRouter( prefix="/api" ,default=router_default_handler)
    router.add_api_route("/webhook" ,verify_webhook , methods=["GET"])
    router.add_api_route("/webhook" ,  webhook  , methods=["POST"])
    router.add_api_route("/favicon.ico" , favicon , methods=["GET"])
    return router