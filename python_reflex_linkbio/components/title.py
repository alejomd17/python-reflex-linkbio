import reflex as rx
import python_reflex_linkbio.styles.styles as styles


def tittle(text:str) -> rx.Component:
    rx_title = rx.heading(text, style=styles.tittle_style)
    
    return rx_title