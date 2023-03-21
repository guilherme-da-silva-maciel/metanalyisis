from typing import Generator,Optional
from fastapi import Depends,HTTPException,status
from jose import jwt,JWTError
from sqlalchemy.future import select
from core.configs import settings
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session:AsyncSession = Session()

    try:
        yield session
    
    finally:
        await session.close()




    
