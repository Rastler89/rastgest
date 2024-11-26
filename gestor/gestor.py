"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from . import styles

from .pages import *
from .state.base import State


app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)

app.add_page(login)
app.add_page(signup)