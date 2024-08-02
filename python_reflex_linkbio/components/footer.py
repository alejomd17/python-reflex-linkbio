import reflex as rx
import datetime
from python_reflex_linkbio.components.link_button import link_button
from python_reflex_linkbio.styles.styles import Size as Size


def footer() -> rx.Component:
    rx_footer = rx.vstack(rx.image(src="favicon.ico", html_width="100px",html_height="auto"),
                rx.text(f"© 2021-{datetime.date.today().year} ",
                        rx.link('AlejoMD17', href='https://www.github.com/alejomd17', is_external=True),
                        " by ",
                        rx.link('Alejandro Moscoso-Deossa', href='https://www.linkedin.com/in/alejomd17', is_external=True)),
                rx.text("CREATING DATA SCIENCE FROM MEDELLÍN, COLOMBIA"),
    style={
            "display": "flex",
            "justify_content": "center",  # Center align the entire Box content
            "text_align": "center",       # Center align text within Box
            "margin_bottom": Size.BIG.value})
                

    return rx_footer