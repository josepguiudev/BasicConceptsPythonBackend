#trabajar con encriptacion tenemos qe instalar python-jose y luego passlib
#pip install "python-jose[cryptography]"
#pip install bcrypt
#pip install "passlib[becrypt]" 
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import timedelta, datetime

ALGORITM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "AJHSDKJAHSLDKJAHSDFLJKAHlkjaskahjsdfklajhsgd"

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes="bcrypt")

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev":{
        "username": "manu",
        "fullname": "manel",
        "email": "manel@gmail.com",
        "disabled": False,
        "password": "$2a$12$Tpyt6ZvpWgeLaJVHEkhSQ.mQviagwVy40LYrFkHGLJcvDR9wiDB16"
    },
    "pepe":{
        "username": "pepe",
        "fullname": "josep guiu",
        "email": "pepe@gmail.com",
        "disabled": True,
        "password": "$2a$12$SCRKqZAwR/WLykg6PWOEruUR9gJwGf45Y0EgLO6dw6ByzjdmXbK0W"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="La contraseña no es correcta")

    acces_token = {"sub":user.username, 
                   "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    #comenta elsecret para ver el acces token
    return {"acces_token": jwt.encode(acces_token, SECRET, algorithm=ALGORITM), "token_type": "bearer"}
    

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autentificacion invalidas",
            headers={"www.Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITM]).get("sub")
        if username is None:
            raise exception
    except JWTError as e:
        raise exception
    
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo")
    return user

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user