from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from typing import Annotated
from fastapi import Depends

URL_DATABASE_LINK = 'sqlite+aiosqlite:///./user.db'

user_engine = create_async_engine(url=URL_DATABASE_LINK)
user_session = async_sessionmaker(bind=user_engine, expire_on_commit=False)

async def get_session_user():
    async with user_session as session:
        yield session

SessionDep_task = Annotated[AsyncSession, Depends(get_session_user)]