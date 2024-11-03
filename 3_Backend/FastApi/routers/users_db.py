from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No"}})


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

#Por Path 
@router.get("/{id}")
async def usersbyId(id: str):
    return search_user("_id", ObjectId(id))

    
#Por query
@router.get("/")
async def usersbyId(id: str):
    return search_user("_id", ObjectId(id))
    
@router.post("/", response_model=User, status_code= status.HTTP_201_CREATED)#crear
async def user(user: User):

    #Buscar el usuario antes de añadir ya que en caso que exista no se añade
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"] #Nos lo cargamos xq ponemos que el atributo es opcional en la clase. 

    id = db_client.users.insert_one(user_dict).inserted_id#Podemos acceder al id en el momento que lo insertamos
    #para comprobar que se ha insertado el id, vaamos a comprobar si esta en bd
     #Esto nos va a devolver un json que tenemos que convetir
    new_user = user_schema(db_client.users.find_one({"_id":id}))#mongo crea el campo id como _id
   

    return User(**new_user)
    
@router.put("/")
async def user(user:User):
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict
        )
    except:
        return {"error": "No se ha actualizado el usuario"}
    
    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    print(found)
    if found == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="mi error")


def search_user(field: str, key):#generalizamos ya que la busqueda es igual pero por diferentes atributos
    try:
        user = db_client.users.find_one({field : key})
        return User(**user_schema(user))
    except:
        return {"Error":"Error"}
    
