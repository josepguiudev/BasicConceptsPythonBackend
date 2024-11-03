#Para levantar el servidor en comandos escribimos --> uvicorn users:app --reload
#from fastapi import FastAPI, HTTPException

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel #da la capacidad de crear una entidad

#app = FastAPI()
router = APIRouter(tags=["users"])

#EntidadUser
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id= 1, name="pepe", surname="guiuxx", url="https://pepe.com", age= 30),
         User(id= 2, name="pepe", surname="guiu", url="https://pepe.com", age= 30),
         User(id= 3, name="pepe", surname="guiu", url="https://pepe.com", age= 30),
         User(id= 4, name="pepe", surname="guiu", url="https://pepe.com", age= 30)]

@router.get("/users_json")
async def users_json():
    return [{"name":"pepe", "surname":"guiu", "url":"https://pepe.com", "age":"30"},
            {"name":"pepe", "surname":"guiu", "url":"https://pepe.com", "age":"30"},
            {"name":"pepe", "surname":"guiu", "url":"https://pepe.com", "age":"30"}]

@router.get("/users_class", status_code=201)
async def usersclass():
    raise HTTPException(status_code=204, detail="mi error")#cambiamos status code xq si XD
    return users_list

#Por Path 
@router.get("/users/{id}", response_model = User)
async def usersbyId(id: int):
    try:
        users = filter(lambda user: user.id == id, users_list)
        return list(users)[0]
    except:
        #print("Error no se ha encontrado el usuario")
        return "Error no se ha encontrado el usuario"
    
#Por query
@router.get("/users/")
async def usersbyId(id: int):
    try:
        users = filter(lambda user: user.id == id, users_list)
        return list(users)[0]
    except:
        #print("Error no se ha encontrado el usuario")
        return "Error no se ha encontrado el usuario"
    
@router.post("/postusers/", status_code=201)#crear
async def user(user: User):
    users_list.append(User)

@router.put("/user/")
async def user(user:User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
    


@router.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
    
    print(users_list)