from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from typing import Annotated
from fastapi import Depends

URL_DATABASE_LINK = 'sqlite+aiosqlite:///./task.db'

task_engine = create_async_engine(url=URL_DATABASE_LINK)
task_session = async_sessionmaker(bind=task_engine, expire_on_commit=False)

async def get_session_task():
    async with task_session as session:
        yield session

SessionDep_task = Annotated[AsyncSession, Depends(get_session_task)]