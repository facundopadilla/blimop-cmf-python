from settings.server import ServerService
from routers import webhook, login

app = ServerService.get_app()
app.include_router(webhook.router)
app.include_router(login.router)

