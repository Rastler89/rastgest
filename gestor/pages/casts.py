"""The casts page"""

import reflex as rx
from gestor.state.base import State
from ..templates import template

@template(route="/casts", title="Casts", on_load=State.check_login())
def casts() -> rx.Component:
    return rx.vstack(
        rx.heading(f"Casts")
    )