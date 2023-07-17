from fastapi import APIRouter
from models.user_model import User
from schemas.user_schema import UserBaseModel

user = APIRouter()


# Specifies a path to create users in the database for the users table, not without
# verifying that the data entered are of the requested type.
@user.post('/user/')
async def create_user(user: UserBaseModel):
    user = User.create(
        name_of_user = user.name_of_user,
        password = user.password,
        type_of_user = user.type_of_user,
        status = user.status
    )  
    return user

@user.put('/user_update/{name_of_user}')
async def update_user(user: UserBaseModel, name_of_user: str):
    User.update(
        name_of_user = user.name_of_user, 
        password = user.password, 
        type_of_user = user.type_of_user, 
        status = user.status).where(User.name_of_user == name_of_user).execute()

@user.delete('/user_delete/{name_of_user}')
async def delete_user(name_of_user: str):
    user = User.get(User.name_of_user == name_of_user)
    user.delete_instance()

@user.get('/user/{name_of_user}')
async def get_user(name_of_user:str):
    user = User.get(User.name_of_user == name_of_user)
    return user

@user.get('/users')
async def get_users():
    users = User.select()
    return list(users)
