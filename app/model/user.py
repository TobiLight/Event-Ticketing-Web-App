#!/usr/bin/env python3
# File: user.py
# Author: Oluwatobiloba Light
"""User Model"""


from typing import List, Optional
from pydantic import EmailStr
from sqlalchemy import Boolean, Column, String, text
from app.model.base_model import BaseModel
from sqlalchemy.orm import Session
from sqlmodel import Field, Relationship

# from app.schema.event_schema import Event
# from app.schema.rsvp_schema import EventRSVP


class User(BaseModel, table=True):
    __tablename__: str = 'users'

    first_name: str = Field(sa_column=Column(
        String(50), default=None, nullable=True))

    last_name: str = Field(sa_column=Column(
        String(50), default=None, nullable=True))

    email: EmailStr = Field(sa_column=Column(String(255), unique=True))

    password: str = Field(sa_column=Column(
        String(255), default=None, nullable=True))

    phone_no: str = Field(sa_column=Column(
        String(24), default=None, nullable=True))

    is_active: bool = Field(sa_column=Column(Boolean, default=True))

    is_admin: bool = Field(sa_column=Column(Boolean, default=False))

    events: Optional[List["Event"]] = Relationship(back_populates="owner")

    rsvps: Optional[List['EventRSVP']] = Relationship(back_populates="user")

    @classmethod
    def delete_user_events(cls, session: Session, user_id):
        """"""
        events = session.execute(
            text("SELECT * FROM events WHERE owner_id = '{}'"
                 .format(str(user_id)))).fetchall()

        for event in events:
            session.execute(
                text("DELETE FROM event_categories WHERE event_id = '{}'".format(str(event.id))))
            session.execute(
                text("DELETE FROM events WHERE id = '{}'".format(str(event.id))))
