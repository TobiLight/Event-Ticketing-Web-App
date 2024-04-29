#!/usr/bin/env python3
# File: rsvp.py
# Author: Oluwatobiloba Light
"""Event RSVP endpoint"""


from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.model.user import User
from app.schema.rsvp_schema import CreateRSVP
from app.services.rsvp_service import RSVPService


router = APIRouter(
    prefix="/rsvp", tags=["rsvp"],
    dependencies=[Depends(JWTBearer())]
)


@router.post("/{event_id}/rsvp",
             summary="RSVP for an event")
@inject
async def event_rsvp(
    event_id: str,
    event_rsvp_info: CreateRSVP,
    service: RSVPService = Depends(Provide[Container.rsvp_service]),
    current_user: User = Depends(get_current_user)
):
    """Guest RSVP for an event"""
    rsvp_event = service.rsvp_event(
        event_rsvp_info, event_id, str(current_user.id))

    # print(rsvp_event)

    return {}
