import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "700px"

# Sizes
class Size(Enum):
    SMALL =  "0.5em"
    MEDIUM =  "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    
BASE_STYLES = {
                rx.button: {
                    "width":"700px",
                    "height":"100%",
                    "display":"block",
                    "padding":Size.SMALL.value,
                    "border_radius":Size.DEFAULT.value
 },

                rx.vstack: {
                    "width":"700px"
                },
                rx.link: {
                    "text_decoration":"none",
                    "_hover":{}
                    
                }
}

button_title_style = dict(
    font_size = Size.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

tittle_style = dict(
    size="md", width="700px", padding_top=Size.DEFAULT.value
)