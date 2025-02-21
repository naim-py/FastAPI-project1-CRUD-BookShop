from sqlalchemy.orm import Session
from app import models, schemas

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        return self.db.query(models.User).all()

    def get_user_by_id(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def create_user(self, user_data: schemas.UserCreate):
        new_user = models.User(**user_data.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self,user_id:int,user_data:schemas.UserUpdate):
        user=self.get_user_by_id(user_id)
        if not user:
            return None
        for key,value in user_data.dict(exclude_unset=True).items():
            setattr(user,key,value)
        self.db.commit()
        self.db.refresh(user)
        return user


    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
