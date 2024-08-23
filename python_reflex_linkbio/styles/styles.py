import reflex as rx
from enum import Enum
from python_reflex_linkbio.styles.colors import Color as Color
from python_reflex_linkbio.styles.colors import TextColor as TextColor
from python_reflex_linkbio.styles.fonts import Font as Font
from python_reflex_linkbio.styles.fonts import FontWeight as FontWeight

# Constants
MAX_WIDTH = "700px"

# Sizes
class Size(Enum):
    ZERO =  "0px !important"
    SMALL =  "0.5em"
    MEDIUM =  "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    ENORM = "4em"


STYLESHEETS = ["https://fonts.googleapis.com/css?family=Montserrat:wght@300;500$display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@500$display=swap"]
BASE_STYLES = {
                "font_family":Font.DEFAULT.value,
                "font_weight": FontWeight.LIGHT.value,
                    "background_color":Color.BACKGROUND.value,
                    rx.button: {
                    "width":"700px",
                    "height":"100%",
                    "display":"block",
                    "padding":Size.SMALL.value,
                    "border_radius":Size.DEFAULT.value,
                    "color":TextColor.HEADER.value,
                    "background_color":Color.CONTENT.value,
                    "_hover":{
                        "background_color":Color.SECONDARY.value,
                        
                    }
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
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value,
    color= TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.DEFAULT.value,
    font_weight = FontWeight.LIGHT.value,
    color= TextColor.BODY.value
    
)

tittle_style = dict(
    size="7", width="700px", padding_top=Size.DEFAULT.value, 
    color= TextColor.BODY.value
    
)

navbar_title_style = dict(
    font_size = Size.LARGE.value,
    font_family = Font.LOGO.value,
    font_weight = FontWeight.MEDIUM.value,
    
    
)
