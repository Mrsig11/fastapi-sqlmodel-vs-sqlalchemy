from pydantic import BaseModel, ConfigDict

class TodoCreate(BaseModel):
    title: str

class TodoRead(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)
