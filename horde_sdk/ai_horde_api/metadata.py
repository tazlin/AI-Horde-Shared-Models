"""Request metadata specific to the AI-Horde API."""

from enum import auto

from horde_sdk.generic_api.metadata import GenericPathFields, GenericQueryFields


class AIHordePathData(GenericPathFields):
    """AI Horde specific path data. See parent class for more information."""

    id_ = "id"
    """A job UUID."""
    user_id = auto()
    """The horde user id."""
    filter_id = auto()
    """The ID of a content filter."""
    team_id = auto()
    """The UUID of a team."""
    worker_id = auto()
    """The UUID of a worker."""
    sharedkey_id = auto()
    """The UUID representing a shared key."""


class AIHordeQueryData(GenericQueryFields):
    """AI Horde specific query data. See parent class for more information."""

    model_state = auto()
