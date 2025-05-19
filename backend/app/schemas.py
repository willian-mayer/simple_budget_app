from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class TransactionCreate(BaseModel):
    title: str = Field(..., example="Grosery Store")
    amount: float = Field(..., example="-10")
    category: str = Field(..., exmaple="Expenses")

class Transaction(TransactionCreate):
    id: UUID

    class Config:
        orm_mode = True

class AccountCreate(BaseModel):
    title: str = Field(..., example="Saving account")
    balance: float = 0.0; Field(..., example="0.0")

class Account(BaseModel):
    id: UUID
    title: str
    balance: float
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True

class AccountUpdate(BaseModel):
    title: Optional[str] = None
    balance: Optional[float] = None

class TransactionUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None