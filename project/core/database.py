from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncEngine,AsyncSession
from core.configs import settings

engine:AsyncEngine = create_async_engine(settings.DB_URL)

Session:AsyncSession = sessionmaker(autoflush=False,bind=engine,class_=AsyncEngine,expire_on_commit=False)

