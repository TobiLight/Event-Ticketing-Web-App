#!/usr/bin/env python3
# File: container.py
# Author: Oluwatobiloba Light
"""Container"""

from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository import *
from app.repository.category_repository import CategoryRepository
# from app.repository.event_repository import EventRepository
# from app.repository.rsvp_repository import RSVPRepository
from app.services import *
from app.services.auth_service import AuthService
from app.services.category_service import CategoryService
from app.services.event_service import EventService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.endpoints.auth",
            "app.api.endpoints.user",
            "app.api.endpoints.event",
            "app.api.endpoints.rsvp",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(
        Database, db_url=configs.DATABASE_URI)

    # Asynchronous session provider (if needed)
    # async_db = providers.Singleton(
    #     AsyncDatabase, db_url=configs.DATABASE_URI, engine_type="prisma"
    # )

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session)

    # async_user_repository = providers.Factory(
    #     UserRepository, session_factory=async_db.provided.session)

    category_repository = providers.Factory(CategoryRepository,
                                            session_factory=db.provided.session)

    event_repository = providers.Factory(EventRepository,
                                         session_factory=db.provided.session)

    rsvp_repository = providers.Factory(
        RSVPRepository, session_factory=db.provided.session)



    auth_service = providers.Factory(
        AuthService, user_repository=user_repository)

    user_service = providers.Factory(
        UserService, user_repository=user_repository)

    category_service = providers.Factory(CategoryService,
                                         category_repository=category_repository)

    event_service = providers.Factory(
        EventService, event_repository=event_repository)

    rsvp_service = providers.Factory(
        RSVPService, rsvp_repository=rsvp_repository)
