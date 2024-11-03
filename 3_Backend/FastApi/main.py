#Para levantar el servidor en comandos escribimos --> uvicorn main:app --reload
#Documentacion en /docs o /redoc
from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db

from fastapi.staticfiles import StaticFiles

app = FastAPI()#Lo dejamos por defecto

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="statico")

@app.get("/")#URL para acceder a la funcion
async def root():#Siempre que llamamos a un servidor la operacion tiene que ser asincrona
    return "Hola FastApi!"

@app.get("/url")
async def url():
    return {"url_curso":"https://pepe.com"}
