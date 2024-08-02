import reflex as rx
import pandas as pd
from python_reflex_linkbio.components.navbar import navbar
from python_reflex_linkbio.components.footer import footer
from python_reflex_linkbio.views.headers.header import header
from python_reflex_linkbio.views.links.links import links
import python_reflex_linkbio.styles.styles as styles
from python_reflex_linkbio.styles.styles import Size as Size


nba_data = pd.read_excel(
    "C:/Users/jmoscoso04/Downloads/maestros.xlsx"
)
rx.data_table(
    data=nba_data,
    pagination=True,
    search=True,
    sort=True,
)
class State(rx.State):
    pass

def index() -> rx.Component:
    rx_box = rx.box( navbar(),
                rx.center(
                    rx.vstack(header(),  links(),  footer(), max_width =styles.MAX_WIDTH, width="700PX%", margin_y= Size.BIG.value)))
    
    rx_title = rx.text("Hello Reflex!", color_scheme = "yellow")
    
    rx_table = rx.data_table(
    data=nba_data,
    pagination=True,
    search=True,
    sort=True,
)
    return rx_box
        
app = rx.App(
    style=styles.BASE_STYLES
)
app.add_page(index)

# 3:08