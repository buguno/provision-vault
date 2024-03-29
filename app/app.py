from http import HTTPStatus

from fastapi import FastAPI

from app.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK.value, response_model=Message)
def read_root():
    return {'message': 'Hello, prepper!'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED.value, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}
