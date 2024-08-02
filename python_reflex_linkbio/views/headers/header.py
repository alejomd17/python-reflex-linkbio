import reflex as rx
from python_reflex_linkbio.components.link_icon import link_icon
from python_reflex_linkbio.components.info_text import info_text
import python_reflex_linkbio.styles.styles as styles


def header() -> rx.Component:
    rx_vstack = rx.vstack(
        rx.hstack(
        rx.avatar(name='JAMD', src="profile-pic.png",size="7"),
        rx.vstack(
        rx.heading("Alejandro Moscoso  Deossa", size ="7"),
        rx.text("@alejomd17", margin_top="0px !important"),
        rx.hstack(link_icon("tag","https://www.instagram.com/alejomd17"),
                  link_icon("bean","https://www.instagram.com/alejomd17"),
                  link_icon("carrot","https://www.instagram.com/alejomd17"))
        ), 
        align_items = "start",
        spacing = styles.Size.BIG.value
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
                    
                    style={
                    "white-space": "pre-line"  # This ensures that the text respects line breaks
                })        
        )
    
    return rx_vstack