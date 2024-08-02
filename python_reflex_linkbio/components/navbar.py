import reflex as rx
import python_reflex_linkbio.styles.styles as styles


def navbar() -> rx.Component:
    rx_hstack = rx.hstack(
                rx.text("AlejoMD17",
                        color_scheme="cyan"),
                position="sticky",
            bg = "lightgray",
            padding_x= styles.Size.DEFAULT.value,
            padding_y= styles.Size.SMALL.value,
            z_index = "999"
            )
    return rx_hstack