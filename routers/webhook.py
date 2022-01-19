from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Webhook"]
)

@router.get(path="/")
async def index():
    return "hola soy el webhook"
