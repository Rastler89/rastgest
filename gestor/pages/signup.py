"""Sign up page. Uses auth_layout to render UI shared with the login page."""

import reflex as rx
from gestor.layouts import auth_layout
from gestor.state.auth import AuthState


def signup():
    """The sign up page."""
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
                    color="black"
                ),
                rx.text(
                    "Password",
                    color="black",
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
                rx.text(
                    "Repita Password",
                    color="black",
                    ),
                rx.input(
                    type="password",
                    placeholder="Confirm password",
                    on_blur=AuthState.set_confirm_password,
                    size="3",
                    radius="large",
                    variant="soft",
                    color_scheme="violet",
                    color="black"
                ),
                rx.button(
                    "Sign up",
                    on_click=AuthState.signup,
                    size="3",
                    width="6em",
                    background_color="darkviolet",
                ),
                spacing="4",
                align_items="center",
            ),
            align_items="center",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Already have an account? ",
            rx.link("Sign in here.", href="/",color="darkviolet"),
            color="gray",
        ),
    )