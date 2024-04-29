#!/usr/bin/env python3
# File: base_model.py
# Author: Oluwatobiloba Light
"""Base Model"""


from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime, Uuid, func
from sqlmodel import SQLModel, Field

from app.core.database import Base


class BaseModel(SQLModel):
    __abstract__ = True

    id: UUID = Field(primary_key=True, default=uuid4())

    created_at: datetime = Field(default=datetime.now())

    updated_at: datetime = Field(default=datetime.now())

    # updated_at: datetime = Field(sa_column=Column(
    #     DateTime, onupdate=datetime.now()), default=datetime.now())
