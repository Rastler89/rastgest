"""The home page. This file includes examples abstracting complex UI into smaller components."""

import reflex as rx
from gestor.state.base import State
from gestor.state.home import HomeState
from .. import styles
from ..templates import template

from ..components import jumbotron

@template(route="/", title="Home", on_load=State.check_login())
def home() -> rx.Component:
    return rx.vstack(
        rx.heading(f"Welcome")
    )