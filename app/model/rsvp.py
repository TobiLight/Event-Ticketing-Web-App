#!/usr/bin/env python3
# File: rsvp.py
# Author: Oluwatobiloba Light
"""RSVP Model"""


from typing import List, Optional
from uuid import UUID
from pydantic import EmailStr
from app.model.base_model import BaseModel
from sqlmodel import Field, Relationship
from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, String, Uuid
# from app.schema.event_schema import Event
from app.schema.user_schema import User_, User


class EventRSVP(BaseModel, table=True):
    __tablename__: str = "rsvps"

    name: str = Field(sa_column=Column(String(255), nullable=False))

    email: EmailStr = Field(sa_column=Column(String(255), nullable=False))

    is_attending: bool = Field(sa_column=Column(
        Boolean, nullable=False), default=False)

    is_bringing_extra: bool = Field(sa_column=Column(
        Boolean, nullable=False), default=False)

    extra_persons: Optional[List[str]] = Field(sa_column=Column(ARRAY(
        String, as_tuple=False, dimensions=None, zero_indexes=False)),
        default_factory=list)

    event_id: UUID = Field(
        sa_column=Column(Uuid, ForeignKey('events.id')))

    event: Optional['Event'] = Relationship(back_populates="rsvps")

    user_id: UUID = Field(
        sa_column=Column(Uuid, ForeignKey('users.id')))

    user: Optional['User'] = Relationship(back_populates="rsvps")
