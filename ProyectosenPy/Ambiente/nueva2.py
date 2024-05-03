import flet as ft
import math
def main(page:ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.window_width= "600"
    page.window_height = "600"
    page.title = "Pasos"
    page.horizontal_alignment = "CENTER"
    page.padding = 60
    page.window_center()

    #Funciones
    def DecimalaBinario(e):

        entrada = int(Jtx1.value)
        binario = ""
        while entrada > 0:
            if(entrada % 2 == 0):
                binario = "0" + binario
            else:
                binario = "1" + binario
            entrada = entrada // 2
        Jtx2.value = str(binario)
        page.update()
    
    def BinarioaDecimal(e):

        entrada = Jtx1.value
        pos = len(entrada)
        deci = 0
        for i in reversed(entrada):
            if i == "1":
                deci = deci + pow(2,(len(entrada) - pos))
            pos = pos - 1
        Jtx2.value = str(deci)
        page.update()
    
    def borrar(e):

        Jtx1.value = ""
        Jtx2.value = ""
        page.update()
    #Titulo

    titulo = ft.Text(
        value= "Proyecto 1",
        color= ft.colors.WHITE,
        text_align= "CENTER",
        weight= ft.FontWeight.W_100,
        size = 30,
        font_family= "Arial"
    )
    page.add(titulo)

    #Text

    entradatxt = ft.Text(
        value= "Ingrese el numero que quiere cambiar: ",
        color = ft.colors.WHITE,
        size= 15,
        text_align= "CENTER"
    )
    page.add(entradatxt)
    
    #TexTField

    Jtx1 = ft.TextField(
        label= "Entrada",
        width= 250,
        border_color= ft.colors.BLUE,
        color = ft.colors.WHITE,
        max_length= 30
    )

    Jtx2 = ft.TextField(
        label= "Salida",
        width= 250,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,
        max_length= 30
    )

    #Botones

    btn1 = ft.ElevatedButton(
        text= "Decimal/Binario",
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        width= 100,
        height=50,
        on_click= DecimalaBinario,
    )

    btn2 = ft.ElevatedButton(
        text= "Binario/Decimal",
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        width= 100,
        height=50,
        on_click= BinarioaDecimal,
    )
    btn3 = ft.ElevatedButton(
        text= "Borrar",
        bgcolor= ft.colors.BLACK,
        color= ft.colors.WHITE,
        width= 100,
        height=50,
        on_click=borrar,
    )


    #Genero una columna para los TextField
    Col1 = ft.Column(controls=[Jtx1,Jtx2],alignment= ft.MainAxisAlignment.CENTER,
                      horizontal_alignment= ft.CrossAxisAlignment.CENTER)
    page.add(Col1)
    #Genero una fila para los botones
    Fila1 = ft.Row(controls= [btn1,btn2,btn3],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    page.add(Fila1)
    


    page.update()

ft.app(target=main)