import flet as ft

def main(page: ft.Page):
    page.window_width = "600"
    page.window_height = "550"
    page.horizontal_alignment = "CENTER"
    page.window_center()
    page.bgcolor = ft.colors.BLACK
    page.padding = 55


    def Facto(e):
        i = 1
        result = 1
        while(i <= int(jtx1.value)):
            result = result * i
            i = i + 1
        jtx2.value = str(result)
        page.update()

    def borrar(e):
        jtx1.value = ""
        jtx2.value = ""
        page.update()
    #Text

    Titulo = ft.Text(
        value = "Factorial",
        size = 35,
        text_align= "CENTER",
        color= ft.colors.WHITE,
        opacity= 0.5,
        weight= ft.FontWeight.W_100
    )
    page.add(Titulo)

    come1 = ft.Text(
        value = "Ingrese el numero para el factorial: ",
        size = 20,
        text_align= "CENTER",
        color= ft.colors.WHITE,
        opacity= 0.5,
        weight= ft.FontWeight.W_100
    )

    #TextField

    jtx1 = ft.TextField(
        label="Numero",
        max_length= 10,
        width= 230,
        border_color= ft.colors.GREEN_800
    )

    jtx2 = ft.TextField(
        label="Resultado",
        max_length= 10,
        width= 230,
        border_color= ft.colors.GREEN_800
    )

    #Botones

    btn1 = ft.ElevatedButton(
        text="Factorial",
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        width= 150,
        height= 30,
        on_click= Facto
    )
    btn2 = ft.ElevatedButton(
        text="Borrar",
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        width= 150,
        height= 30,
        on_click= borrar
    )

    col1 = ft.Column(controls=[come1,jtx1,jtx2],alignment=ft.MainAxisAlignment.CENTER,
                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    page.add(col1)

    fila1 = ft.Row(controls=[btn1,btn2],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    page.add(fila1)
    page.update()

ft.app(target= main)