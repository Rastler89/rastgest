"""Pagina de login/registro """
"""Shared auth layout."""

import reflex as rx

from ..components import jumbotron


def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
        jumbotron(
            rx.vstack(
                rx.heading("Bienvenido a RastGest", size="8"),
                rx.heading("Accede a tu cuenta o crea una nueva", size="8"),
                align="center",
                color="black"
            ),
            rx.text(
                "Aplicación desarrollada por  ",
                rx.link(
                    "Rastler",
                    href="https://rastler.netlify.app/",
                    color="darkviolet",
                ),
                ".",
                color="gray",
                font_weight="medium",
            ),
            *args,
            border_radius="10px",
            box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display="flex",
            flex_direction="column",
            align_items="center",
            padding_top="36px",
            padding_bottom="24px",
            spacing="4",
        ),
        height="100vh",
        padding_top="20vh",
        padding_bottom="15vh",
        background_color="#42214b",
        background_size="cover"
    )