from logging import getLogger
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from dbinterface import core
from dbinterface import errors
from dbinterface import models
from dbinterface import schemas

logger = getLogger("uvicorn")


def transactions_create(
    db: Session,
    transaction: schemas.TransactionsCreate
):
    transaction_i = models.Transactions(**transaction.dict())
    logger.warning("insert a transaction")
    db.add(transaction_i)
    logger.warning("temporary flush transaction")
    db.flush()

    amount_total = amount_total_get_by_user(db, transaction.user_id)
    logger.warning(f"total amount of {transaction.user_id}: {amount_total}")

    if amount_total > core.AMOUNT_LIMIT:
        db.close()
        raise errors.AmountExceedError("Transaction amount reached limit")

    logger.warning("transaction is applicable")
    db.commit()
    db.refresh(transaction_i)

    return transaction_i


def amount_total_get_by_user(db: Session, user_id: int):
    amount_total = (
        db
        .query(func.sum(models.Transactions.amount)
            .label("sum_amount"))
        .filter(models.Transactions.user_id == user_id)
        .first()
        .sum_amount
    )
    return amount_total


def users_get(db: Session):
    return db.query(models.Users).limit(100).all()
