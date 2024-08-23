import reflex as rx
import python_reflex_linkbio.styles.styles as styles
from python_reflex_linkbio.styles.colors import Color as Color
from python_reflex_linkbio.styles.colors import TextColor as TextColor


def navbar() -> rx.Component:
    rx_hstack = rx.hstack(rx.chakra.box(
                        rx.chakra.span("A",color=Color.PRIMARY.value),
                        rx.chakra.span("MD",color=Color.SECONDARY.value),
                        rx.chakra.span("17",color=Color.PRIMARY.value),
                        style = styles.navbar_title_style
                        ),
                position="sticky",
                bg = Color.BACKGROUND.value,
                padding_x= styles.Size.DEFAULT.value,
                padding_y= styles.Size.SMALL.value,
                z_index = "999"
                )
    
    return rx_hstack
    
    