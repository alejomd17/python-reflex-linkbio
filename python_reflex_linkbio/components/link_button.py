import reflex as rx
import python_reflex_linkbio.styles.styles as styles


def link_button(title:str,body:str, url:str, icon:str) -> rx.Component:
    rx_button = rx.link(
        rx.button(
             rx.hstack(rx.image(icon,
                #  rx.icon(tag= 'arrow-right',
                               width= styles.Size.BIG.value,
                               height= styles.Size.BIG.value,
                               margin=styles.Size.MEDIUM.value,), 
                       rx.vstack(
                        rx.text(title, style=styles.button_title_style),
                        rx.text(body, style=styles.button_body_style),
                        spaccing=  styles.Size.SMALL.value,
                        align_items="start",
                        margin =  styles.Size.ZERO.value))),
                        href=url,
                        is_external=True
                        )
    

    return rx_button