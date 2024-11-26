"""A jumbotron component."""

import reflex as rx


def jumbotron(*children, **props):
    """A fixed jumbotron based on a 960px grid."""
    # Enable override of default props.
    props = (
        dict(
            width="60vw",
            max_width="960px",
            background="white",
            max_height="750px",
            px="9",
            margin="0 auto",
            position="relative",
        )
        | props
    )
    return rx.stack(*children, **props)