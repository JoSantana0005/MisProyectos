import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = "Center"
    page.bgcolor = ft.colors.BLACK
    page.window_max_width = "400"
    page.window_height = "400"
    page.title = "Pasos"
    page.window_center()
    
    Titul_texto = ft.Text(
        value= "Hola mundo",
        size= 30,
        weight= ft.FontWeight.W_100,
        text_align="CENTER"
    )
    page.add(Titul_texto)
    fila = ft.Row(controls=[
        ft.Text(
        value= "Ingrese el numero que quiere: ",
        color= ft.colors.GREEN,
        text_align= "CENTER",
        ),
        ft.TextField(
            label="Entrada",
            border_color= ft.colors.ORANGE,
            width= 300,
            bgcolor= ft.colors.BLACK,
            color= ft.colors.BLACK
        ),
    ],alignment=ft.MainAxisAlignment.CENTER,
    vertical_alignment= "CENTER")
    
    page.add(fila)
    page.update()

ft.app(target=main)
