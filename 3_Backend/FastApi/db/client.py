from pymongo import MongoClient

#base de datos local
db_client = MongoClient().local #al ponerlo aqui ahorramos ponerlo en cada llamada db_client.local.users

#base de datos remota
#db_client = MongoClient(URL).nombrebasdatos