#!/usr/bin/env python3
# File: event.py
# Author: Oluwatobiloba Light
"""Event Model"""


import enum
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel, Table
from app.core.database import Base
# from app.model.rsvp import EventRSVP
from app.schema.base_schema import ModelBaseInfo
from app.schema.user_schema import User
from app.util.date import format_time_with_am_pm
from typing import List, Optional
from sqlalchemy import Boolean, Column, Date, ForeignKey, String, Uuid, Enum
from app.model.base_model import BaseModel
from datetime import date as dt
from app.model.category import Category
# from app.schema.rsvp_schema import EventRSVP


class EventType(str, enum.Enum):
    """Event Type"""
    public = "public"
    private = "private"


EventTypeEnum: Enum = Enum(
    EventType,
    name="event_type_enum",
    create_constraint=True,
    metadata=Base.metadata,
    validate_strings=True,
)


# class EventCategory(BaseModel, table=True):
#     ___tablename__ = "event_categories"

#     event_id: UUID = Field(sa_column=Column(
#         Uuid, ForeignKey("events.id"), primary_key=True))

#     category_id: UUID = Field(sa_column=Column(
#         Uuid, ForeignKey("categories.id"), primary_key=True))


event_categories = Table(
    "event_categories",
    SQLModel.metadata,
    Column("event_id", Uuid, ForeignKey("events.id"), primary_key=True),
    Column("category_id", Uuid, ForeignKey(
        "categories.id"), primary_key=True)
)


class EventRSVP(ModelBaseInfo):
    ...
    name: str

    email: EmailStr

    is_attending: bool = False

    is_bringing_extra: bool = False

    extra_persons: Optional[List[str]] = []

    event_id: UUID

    event: Optional['Event_'] = None

    user_id: UUID

    user: Optional['User_'] = None

    class Config:
        orm_mode = True


class Event(BaseModel, table=True):
    __tablename__: str = 'events'

    name: str = Field(sa_column=Column(
        String(255), default=None, nullable=False))

    categories_id: Optional[List[UUID]] = Field(
        sa_column=Column(Uuid, ForeignKey('categories.id')))

    categories: List['Category'] = Relationship(
        back_populates="events",
        # sa_relationship_kwargs={"secondary": 'event_categories'}
    )

    description: str = Field(
        sa_column=Column(String(2048), default=None, nullable=False))

    date: dt = Field(sa_column=Column(
        Date, default=dt.today(), nullable=False))

    location: str = Field(sa_column=Column(
        String(255), default=None, nullable=False))

    image: str = Field(sa_column=Column(
        String(2048), default=None, nullable=False))

    evt_type: EventType = Field(default=EventType.public, nullable=False)

    hide_rsvp_list: bool = Field(sa_column=Column(Boolean, default=False))

    rsvps: Optional[List['EventRSVP']] = Relationship(back_populates="event")

    owner_id: Optional[UUID] = Field(
        sa_column=Column(Uuid, ForeignKey('users.id')))

    owner: Optional['User'] = Relationship(back_populates="events")

    @property
    def formatted_start_time(self) -> Optional[str]:
        """
        This property returns the start_time with AM/PM format.
        """
        return format_time_with_am_pm(self.start_time)

    @property
    def formatted_end_time(self) -> Optional[str]:
        """
        This property returns the end_time with AM/PM format.
        """
        return format_time_with_am_pm(self.end_time)
