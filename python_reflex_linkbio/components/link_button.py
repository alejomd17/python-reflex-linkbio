import reflex as rx
import python_reflex_linkbio.styles.styles as styles


def link_button(title:str,body:str, url:str) -> rx.Component:
    rx_button = rx.link(
        rx.button(
             rx.hstack(rx.icon(tag= 'arrow-right',
                               width= styles.Size.BIG.value,
                               height= styles.Size.BIG.value), 
                       rx.vstack(
                        rx.text(title, style=styles.button_title_style),
                        rx.text(body, style=styles.button_body_style),
                        align_items="start"))),
                        href=url,
                        is_external=True
                        )

    return rx_button