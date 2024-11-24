"""The home page. This file includes examples abstracting complex UI into smaller components."""

import reflex as rx
from gestor.state.base import State
from gestor.state.home import HomeState

from ..components import container

def home():
    """The home page."""
    return container(
        rx.text("Zona protegida")
    )