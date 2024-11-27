from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.project import Project
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

class ProjectRepository:
    
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_project(self, project_data: dict, creator_id: int) -> Project:
        new_project = Project(**project_data, creator_id=creator_id)
        self.db_session.add(new_project)
        try:
            await self.db_session.commit()
            await self.db_session.refresh(new_project)
            return new_project
        except IntegrityError:
            await self.db_session.rollback()
            raise Exception("Error creating project")
    
