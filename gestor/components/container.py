"""A container component."""

import reflex as rx


def container(*children, **props):
    """A fixed container based on a 960px grid."""
    # Enable override of default props.
    props = (
        dict(
            width="100vw",
            max_width="1920px",
            background="white",
            height="100vh",
            px="9",
            margin="0 auto",
            position="relative",
        )
        | props
    )
    return rx.stack(*children, **props)