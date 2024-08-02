import reflex as rx
from python_reflex_linkbio.styles.styles import Size as Size


def info_text(title:str, body:str) -> rx.Component:
    rx_info_text =  rx.flex(
            rx.text(title, weight="bold", color_scheme="cyan", white_space="pre"), 
                    rx.text(body, weight="regular"))
    return rx_info_text