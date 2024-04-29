#!/usr/bin/env python3
# File: rsvp_service.py
# Author: Oluwatobiloba Light
"""Event RSVP Services"""


from app.repository.rsvp_repository import RSVPRepository
from app.schema.rsvp_schema import CreateRSVP
from app.services.base_service import BaseService


class RSVPService(BaseService):
    def __init__(self, rsvp_repository: RSVPRepository):
        self.rsvp_repository = rsvp_repository
        super().__init__(rsvp_repository)

    def rsvp_event(self, event_rsvp_info: CreateRSVP, event_id: str, user_id: str):
        """"""
        return self.rsvp_repository.rsvp_for_event(event_rsvp_info, event_id, user_id)
