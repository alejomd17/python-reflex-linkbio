import reflex as rx
from python_reflex_linkbio.components.link_icon import link_icon
from python_reflex_linkbio.components.info_text import info_text
from python_reflex_linkbio.components.title import tittle
import python_reflex_linkbio.styles.styles as styles
from python_reflex_linkbio.styles.fonts import Font as  Font
from python_reflex_linkbio.styles.fonts import FontWeight as FontWeight
import python_reflex_linkbio.constants as constants
from python_reflex_linkbio.styles.colors import TextColor as TextColor
from python_reflex_linkbio.styles.colors import Color as Color




def header() -> rx.Component:
    rx_vstack = rx.vstack(
        rx.hstack(
        rx.avatar(name='JAMD', src="profile-pic.png",size="8", border_radius="80px 80px",
    border=f'3.7px solid {Color.PRIMARY.value}'),
        rx.vstack(
        rx.heading("Alejandro Moscoso  Deossa", size ="8", color=TextColor.HEADER.value, font_family=Font.TITLE.value, font_weight =  FontWeight.LIGHT.value,),
        rx.text("@alejomd17", margin_top=styles.Size.ZERO.value, color=TextColor.BODY.value),
        rx.hstack(link_icon("tag",constants.LINKEDIN_URL),
                  link_icon("bean",constants.LINKEDIN_URL),
                  link_icon("carrot",constants.LINKEDIN_URL),
                  spacing = styles.Size.DEFAULT.value)
        ), 
        align_items = "start",
        spacing = styles.Size.ENORM.value
        ),
        
        rx.flex(info_text("+8 ","años de experiencia en finanzas, estadística, econometría y economía"),
                rx.spacer(),
        info_text("+4 ","años de experiencia en análisis de datos y BI"),
                rx.spacer(),
        info_text("+3 ","años de experiencia en Ciencia de datos (Data Sciencie) y Machine Learning"),
                rx.spacer(),
        info_text("+1 ","años de experiencia en Ingeniería de datos (Data Engineering) e IA (Artificial Intelligence)",
        ), width="700px"),
        rx.text("""Científico de datos (Data Scientist) | Especialista en Analítica

                    Programación con Python.
                    Computación en la nube: Microsoft Azure, Microsoft Data Lake, Databricks, Data Factory y MLOps.
                    Bases de Datos: SQL
                    Herramientas de Visualización: Power BI
                    También manejo herramientas de analítica Excel Avanzado y Lenguaje de programación R.

                    De formación: Ingeniero Financiero, Especialista en estadística y Magíster en Economía.

                    Trabajo en Ciencia de Datos, Machine Learning, Data Science, Data Analysis y AI
                    con mayor experiencia en temáticas de finanzas, economía, riesgos, econometría y estadística.""", 
                    align_items="start",
                    color = TextColor.HEADER.value,
                        margin_top = styles.Size.BIG.value,
                    
                    
                    style={
                "margin_botton" : styles.Size.BIG.value,
                    "white-space": "pre-line"  # This ensures that the text respects line breaks
                    
                })        
        )
    
    return rx_vstack