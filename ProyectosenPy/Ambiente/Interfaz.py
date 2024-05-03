import flet as ft
import random
def main(page:ft.Page):
    page.window_height = 600
    page.window_width = 600
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.WHITE
    page.window_center()
    
    """def crear_Texto(number):
        lista = []
        for _ in range(number):
            lista.append(
                ft.Text(
                    value= random.randint(1,100),
                    color= "Green",
                    text_align= "center"
                )
            )
        return lista
    col = ft.Column(controls=crear_Texto(4))
    page.add(col)"""
    Jlabel1 = ft.Text(
        value="Entrada", color= ft.colors.BLACK,
        bgcolor=ft.colors.BLUE, text_align= "CENTER"
    )
    Jtx1 = ft.TextField(
        height= 200, width= 100, bgcolor= ft.colors.WHITE,
        color= ft.colors.WHITE, text_align="center",
        border_color= ft.colors.ORANGE
    )
    page.update()
    
ft.app(target= main)