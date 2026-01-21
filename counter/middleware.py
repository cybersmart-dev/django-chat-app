

from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser, User
from channels.db import database_sync_to_async

@database_sync_to_async
def get_user(id):
    try:
        return User.objects.get(id=id)
    except Exception:
        return AnonymousUser()

class JWTAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        scope["user"] = get_user(1)
        return await self.app(scope, receive, send)
