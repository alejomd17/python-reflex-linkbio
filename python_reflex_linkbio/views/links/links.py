import reflex as rx
from python_reflex_linkbio.components.link_button import link_button
from python_reflex_linkbio.components.title import tittle

def links() -> rx.Component:
    rx_button = rx.vstack(
        tittle("Información y contacto"),
        link_button("LinkedIn","Contactame","https://www.linkedin.com/in/alejomd17"),
        tittle("Proyectos"),
        
        link_button("GitHub","Proyectos personales","https://www.github.com/alejomd17"),
        link_button("Proyectos", "Portafolio","https://www.instagram.com/alejomd17"),
        )

    
    return rx_button