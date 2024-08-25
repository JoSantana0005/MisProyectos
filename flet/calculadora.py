import flet as ft

def main(page:ft.Page):
    page.padding = 45
    page.window_width = "540"
    page.window_height = "620"
    page.window_center()
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = "CENTER"
    page.title = "Calculadora"
    #Funciones
    def hover(e: ft.KeyboardEvent):
        e.control.bgcolor = "blue" if e.data == "true" else "white12"
        e.control.color = "black" if e.data == "true" else "white"
        e.control.update()
    def hoveroperador(e: ft.KeyboardEvent):
        e.control.bgcolor = "blue" if e.data == "true" else "white12"
        e.control.color = "white" if e.data == "true" else "orange"
        e.control.update()
    def borrar__datos(e):
        operacion.value = ""
        resultado.value = ""
        btnborrar.disabled = False
        page.update()
    
    def borrar_dato(e):
        operacion.value = operacion.value[:-1]
        page.update()
    
    def porcentaje__dato(e):
        result = float(operacion.value)/100
        resultado.value = str(result)
        btnborrar.disabled = True
        page.update()
    
    def agregar__dato(e:ft.KeyboardEvent):
        operacion.value = operacion.value + e.control.text
        page.update()
    
    def operar__datos(e):
        result = eval(operacion.value)
        print(result)
        resultado.value = result
        btnborrar.disabled = True
        page.update()
    #Text
    text1 = ft.Text(
        value= "Calculadora",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        size= 45,
        weight=ft.FontWeight.W_200,
        font_family= "Tahoma",
        overflow= None
    )
    page.add(text1)
    #TextField
    operacion = ft.TextField(
        width= 250,
        label= "Operación",
        color= ft.colors.WHITE,
        text_align= "RIGHT",
        border_color= ft.colors.BLACK,
        border_radius= 15,
        text_size= 20,
        disabled= True
    )
    resultado = ft.TextField(
        width= 250,
        label= "Resultado",
        color= ft.colors.WHITE,
        text_align= "RIGHT",
        border_color= ft.colors.BLACK,
        border_radius= 15,
        text_size= 20,
        disabled= True
    )
    #Botones
    btnAC = ft.ElevatedButton(
        text= "AC",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height= 40,
        on_click= borrar__datos,
        on_hover= hoveroperador
        
    )
    btnborrar = ft.ElevatedButton(
        text= "X",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height = 40,
        on_click=borrar_dato,
        on_hover= hoveroperador
    )
    btnporc = ft.ElevatedButton(
        text= "%",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height= 40,
        on_click= porcentaje__dato,
        on_hover= hoveroperador
    )
    btnDiv = ft.ElevatedButton(
        text= "/",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hoveroperador
    )
    btn7 = ft.ElevatedButton(
        text= "7",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click=agregar__dato,
        on_hover= hover
    )
    btn8 = ft.ElevatedButton(
        text= "8",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btn9 = ft.ElevatedButton(
        text= "9",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btnX = ft.ElevatedButton(
        text= "*",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover=hoveroperador
    )
    btn4 = ft.ElevatedButton(
        text= "4",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btn5 = ft.ElevatedButton(
        text= "5",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btn6 = ft.ElevatedButton(
        text= "6",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btnresta = ft.ElevatedButton(
        text= "-",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hoveroperador
    )
    btn1 = ft.ElevatedButton(
        text= "1",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click=agregar__dato,
        on_hover= hover
    )
    btn2 = ft.ElevatedButton(
        text= "2",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btn3 = ft.ElevatedButton(
        text= "3",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btnsuma = ft.ElevatedButton(
        text= "+",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.ORANGE_300,
        width= 70,
        height= 40,
        on_click=agregar__dato,
        on_hover= hoveroperador
    )
    btn0 = ft.ElevatedButton(
        text= "0",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btnpunto = ft.ElevatedButton(
        text= ".",
        bgcolor= ft.colors.WHITE12,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= agregar__dato,
        on_hover= hover
    )
    btnresultado = ft.ElevatedButton(
        text= "=",
        bgcolor= ft.colors.ORANGE,
        color= ft.colors.WHITE,
        width= 70,
        height= 40,
        on_click= operar__datos,
        on_hover= hoveroperador
    )
    #Filas y columnas
    columna1 = ft.Column([operacion,resultado],alignment=ft.MainAxisAlignment.CENTER,
                         horizontal_alignment= ft.CrossAxisAlignment.CENTER)
    page.add(columna1)
    
    fila1 = ft.Row([btnAC,btnborrar,btnporc,btnDiv],alignment= ft.MainAxisAlignment.CENTER,
                  vertical_alignment=ft.CrossAxisAlignment.CENTER)
    fila2 = ft.Row([btn7,btn8,btn9,btnX], alignment= ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    fila3 = ft.Row([btn4,btn5,btn6,btnresta],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    fila4 = ft.Row([btn1,btn2,btn3,btnsuma],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER)
    fila5 = ft.Row([btn0,btnpunto,btnresultado],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER)
    #Contenedor
    cont = ft.Container(
        content= ft.Column(
            [fila1,fila2,fila3,fila4,fila5],alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ),
        padding= 15,
        margin= 0,
    )
    page.add(cont)
    page.update()
    

ft.app(target= main)