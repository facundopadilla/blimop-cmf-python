from fastapi import APIRouter
from services.login_service import LoginService

router = APIRouter(prefix="/login", tags=["Login"])

@router.get("/")
async def login():
    asd = LoginService.logear_usuario("pepe", "pepito")
    return "soy el login"