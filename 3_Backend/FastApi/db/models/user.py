from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None # type: ignore #en mongo los ids son strings, asi crean ids mas largos con el optional no hace falta pasar str vacia
    username: str
    email: str