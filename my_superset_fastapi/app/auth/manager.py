from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.core.config import get_settings
from app.core.db import AsyncSessionLocal

from .models import User

settings = get_settings()

cookie_transport = CookieTransport(cookie_name="auth", cookie_max_age=3600)

# NOTE: For simplicity we use cookie auth with OAuth2; customize as needed


class UserManager(BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY


async def get_user_db() -> SQLAlchemyUserDatabase:
    async with AsyncSessionLocal() as session:
        yield SQLAlchemyUserDatabase(session, User)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=3600)


backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager=UserManager,
    auth_backends=[backend],
)

current_active_user = fastapi_users.current_user()
