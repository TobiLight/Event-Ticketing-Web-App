#!/usr/bin/env python3
# File: rsvp_schema.py
# Author: Oluwatobiloba Light
"""Event RSVP Schema"""


from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr
from app.schema.base_schema import FindQueryOptions, ModelBaseInfo, SearchOptions
from app.schema.event_schema import Event
from app.schema.user_schema import User_
from app.util.schema import AllOptional


class BaseRSVP(BaseModel):
    name: str

    email: EmailStr

    is_attending: bool = False

    is_bringing_extra: bool = False

    extra_persons: Optional[List[str]] = []

    event_id: UUID

    event: Optional['Event'] = None

    user_id: UUID

    user: Optional['User_'] = None

    class Config:
        orm_mode = True


class CreateRSVP(ModelBaseInfo, BaseRSVP, AllOptional):
    ...


class RSVP(ModelBaseInfo, BaseRSVP, AllOptional):
    ...


class GetRSVP(BaseModel):
    id: str
    event_id: str


class FindUserRSVPSResult(BaseModel):
    founds: Optional[List[BaseRSVP]]
    search_options: Optional[SearchOptions]


class RSVPQueryOptions(FindQueryOptions):
    ...


class EventRSVP(ModelBaseInfo, BaseRSVP):
    ...
    # name: str
    # email: EmailStr
    # is_attending: bool = False
    # is_bringing_extra: bool = False
    # extra_persons: Optional[List[str]] = None
