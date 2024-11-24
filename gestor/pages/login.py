"""Login page. Uses auth_layout to render UI shared with the sign up page."""

import reflex as rx
from gestor.layouts import auth_layout
from gestor.state.auth import AuthState


def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.text(
                    "Username",
                    color="black",
                    ),
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_username,
                    size="3",
                    radius="large",
                    variant="soft",
                    color_scheme="violet",
                    color="black",
                ),
                rx.text(
                    "Password",
                    color="black"
                    ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                    radius="large",
                    variant="soft",
                    color_scheme="violet",
                    color="black"
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em", background_color="darkviolet"),
                spacing="4",
                align_items="center"
            ),
            align_items="center",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup",color="darkviolet"),
            color="gray",
        ),
    )