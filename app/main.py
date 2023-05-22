from fastapi import Depends, FastAPI, HTTPException, status
from logging import getLogger
from sqlalchemy.orm import Session

from dbinterface import core, schemas
from dbinterface.crud import (
    amount_total_get_by_user,
    transactions_create,
    users_get,
)

logger = getLogger("uvicorn")
app = FastAPI()


def get_db():
    logger.info("connect db")
    db = core.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/transactions",
          response_model=schemas.TransactionsGet,
          status_code=status.HTTP_201_CREATED)
async def post_transactions(
    transaction: schemas.TransactionsCreate,
    db: Session = Depends(get_db),
):
    logger.info("transaction posted")
    try:
        res = transactions_create(db, transaction)
    except Exception:
        logger.info("transaction failed")
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Request is temporarily stopped",
        )

    return res


@app.get("/amount/{user_id}")
async def get_amount_by_user(user_id: int, db: Session = Depends(get_db)):
    amount_total = amount_total_get_by_user(db, user_id)
    return {"user_id": user_id, "sum_amount": amount_total}


@app.get("/users", response_model=list[schemas.UsersGet])
async def get_users(db: Session = Depends(get_db)):
    users = users_get(db)
    return users
