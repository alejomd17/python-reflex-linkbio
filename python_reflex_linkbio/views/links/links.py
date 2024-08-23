import reflex as rx
from python_reflex_linkbio.components.link_button import link_button
from python_reflex_linkbio.components.title import tittle
import python_reflex_linkbio.constants as constants

def links() -> rx.Component:
    rx_button = rx.vstack(
        tittle("Información y contacto"),
        link_button("LinkedIn","Contactame",constants.LINKEDIN_URL, "linkedin-brands-solid.svg"),
        tittle("Proyectos"),
        link_button("GitHub","Proyectos personales",constants.GITHUB_URL,"github-brands-solid.svg"),
        link_button("Proyectos", "Portafolio",constants.INSTAGRAM_URL, "pen-nib-solid.svg"),
        tittle("Contacto"),
        link_button("WhatsApp","Contacto directo",constants.WHATSAPP, "whatsapp-brands-solid.svg"),
        link_button("Email", constants.EMAIL,f'mailto:{constants.EMAIL}', "envelope-solid.svg"),
        )

    
    return rx_button