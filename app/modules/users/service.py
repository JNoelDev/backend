from app.modules.users.repository import UserRepository
from app.modules.users.schema import UserCreate

class UserService:
    def __init__(self,repo:UserRepository):
        self.repo=repo

    async def register(self,data:UserCreate):
        pass