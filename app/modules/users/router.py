from fastapi import APIRouter,status,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService
from app.modules.users.schema import UserCreate

router = APIRouter(prefix="/users", tags=["users"])

def _get_service(db:AsyncSession = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db))

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary= "a new user"
)
async def register(
    payload : UserCreate,service : UserService = Depends(_get_service)
):
    user = await service.register(payload)
    if user:
        return {
            "message":"Check email for verify your account"
        }