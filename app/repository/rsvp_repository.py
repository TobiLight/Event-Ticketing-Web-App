#!/usr/bin/env python3
# File: rsvp_repository.py
# Author: Oluwatobiloba Light
"""Event RSVP Repository"""


from typing import Callable
from uuid import uuid4
from sqlalchemy import Uuid, cast
from sqlalchemy.orm import Session
from app.model.event import Event
from app.model.rsvp import EventRSVP
from app.repository.base_repository import BaseRepository
from app.schema.rsvp_schema import CreateRSVP


class RSVPRepository(BaseRepository):
    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory
        self.model = EventRSVP

        super().__init__(session_factory, EventRSVP)

    def rsvp_for_event(self, event_rsvp_info: CreateRSVP, event_id: str, user_id: str):
        with self.session_factory() as session:
            query = self.model(
                id=uuid4(), **event_rsvp_info.model_dump())

            event_session = session.query(Event)

            event_filter_option = cast(Event.id, Uuid) == cast(event_id, Uuid)

            event = event_session.filter(event_filter_option).first()

            print(query, event)

            return {}
