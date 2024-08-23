import reflex as rx
from python_reflex_linkbio.styles.styles import Size as Size
from python_reflex_linkbio.styles.colors import TextColor as TextColor
from python_reflex_linkbio.styles.colors import Color as Color


def info_text(title:str, body:str) -> rx.Component:
    rx_info_text =  rx.flex(
            rx.text(title,
                    weight="bold", 
                    color = Color.PRIMARY.value,
                #     color_scheme="cyan", 
                    white_space="pre"), 
                    rx.text(body, weight="regular",
                            color=TextColor.BODY.value
                            ))
    return rx_info_text