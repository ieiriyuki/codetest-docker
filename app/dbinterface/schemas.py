from pydantic import BaseModel


class TransactionsCreate(BaseModel):
    user_id: int
    amount: int
    description: str


class TransactionsGet(TransactionsCreate):
    class Config:
        orm_mode = True


class UsersGet(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
