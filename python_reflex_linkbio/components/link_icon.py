import reflex as rx


def link_icon(tag:str, url:str) -> rx.Component:
    rx_link_icon = rx.link(
                    rx.icon(tag=tag),
                    href=url,
                    is_external=True)
        
    return rx_link_icon