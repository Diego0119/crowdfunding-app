from litestar import post, get, put, delete, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.di import Provide
from app.dtos.project_dto import ProjectCreate, ProjectOut, ProjectUpdate
from app.repositories.project_repository import ProjectRepository
from app.models.project import Project
from app.repositories.user_repository import UserRepository

@post("/projects/")
async def create_project(
    project_data: ProjectCreate,
    db: AsyncSession = Provide["db_session"]
):
    project_repo = ProjectRepository(db)
    user_repo = UserRepository(db)
    
    creator = await user_repo.get_user_by_id(project_data.creator_id)
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    project_dict = project_data.dict(exclude={"creator_id"})
    new_project = await project_repo.create_project(project_dict, project_data.creator_id)
    
    return ProjectOut.from_orm(new_project)
