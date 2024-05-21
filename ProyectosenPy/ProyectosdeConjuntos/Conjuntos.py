import flet as ft
import random
import Funciones
def main(page:ft.Page):
    page.window_width = "1200"
    page.window_height = "710"
    page.bgcolor = ft.colors.BLACK
    page.window_center()
    page.horizontal_alignment = "CENTER"
    page.padding = 45

    #Funciones

    def agregar_conjunto(e):
        genConj1 = Funciones.agregar()
        jtx1.value = str(genConj1)
        genConj2 = Funciones.agregar()
        jtx2.value = str(genConj2)
        genConj3 = Funciones.agregar()
        jtx3.value = str(genConj3)
        genConj4 = Funciones.agregar()
        jtx4.value = str(genConj4)
        num = random.randint(1,12)
        if(num == 1):
            checkjtx1.value = True
            checkjtx2.value = True
            page.update()
        elif(num == 2):
            checkjtx1.value = True
            checkjtx3.value = True
            page.update()
        elif(num == 3):
            checkjtx1.value = True
            checkjtx4.value = True
            page.update()
        elif(num == 4):
            checkjtx2.value = True
            checkjtx1.value = True
            page.update()
        elif(num == 5):
            checkjtx2.value = True
            checkjtx3.value = True
            page.update()
        elif(num == 6):
            checkjtx2.value = True
            checkjtx4.value = True
            page.update()
        elif(num == 7):
            checkjtx3.value = True
            checkjtx1.value = True
            page.update()
        elif(num == 8):
            checkjtx3.value= True
            checkjtx2.value = True
            page.update()
        elif(num == 9):
            checkjtx3.value = True
            checkjtx4.value = True
            page.update()
        elif(num == 10):
            checkjtx4.value = True
            checkjtx1.value = True
            page.update()
        elif(num == 11):
            checkjtx4.value = True
            checkjtx2.value = True
            page.update()
        elif(num == 12):
            checkjtx4.value = True
            checkjtx3.value = True
            page.update()
    
    def Union(e):
        """Condicionales para la Union de los conjuntos"""
        if(checkjtx1.value == True and checkjtx2.value == True):
            conju1 = set(jtx1.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.Union(conju1,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx1.value == True and checkjtx3.value == True):
            conju1 = set(jtx1.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.Union(conju1,conju3)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx1.value == True and checkjtx4.value == True):
            conju1 = set(jtx1.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.Union(conju1,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx1.value == True):
            conju2 = set(jtx2.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.Union(conju2,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx3.value == True):
            conju2 = set(jtx2.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.Union(conju2,conju3)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx4.value == True):
            conju2 = set(jtx2.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.Union(conju2,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx1.value == True):
            conju3 = set(jtx3.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.Union(conju3,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx2.value == True):
            conju3 = set(jtx3.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.Union(conju3,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx4.value == True):
            conju3 = set(jtx3.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.Union(conju3,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx1.value == True):
            conju4 = set(jtx4.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.Union(conju4,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx2.value == True):
            conju4 = set(jtx4.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.Union(conju4,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx3.value == True):
            conju4 = set(jtx4.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.Union(conju4,conju3)
            jtxResultado.value = str(resultado)
            page.update()    

    def Interseccion(e):
        """Condicionales para la Interseccion de los conjuntos"""
        if(checkjtx1.value == True and checkjtx2.value == True):
            conju1 = set(jtx1.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.intersecc(conju1,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx1.value == True and checkjtx3.value == True):
            conju1 = set(jtx1.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.intersecc(conju1,conju3)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx1.value == True and checkjtx4.value == True):
            conju1 = set(jtx1.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.intersecc(conju1,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx1.value == True):
            conju2 = set(jtx2.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.intersecc(conju2,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx3.value == True):
            conju2 = set(jtx2.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.intersecc(conju2,conju3)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx4.value == True):
            conju2 = set(jtx2.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.intersecc(conju2,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx1.value == True):
            conju3 = set(jtx3.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.intersecc(conju3,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx2.value == True):
            conju3 = set(jtx3.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.intersecc(conju3,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx4.value == True):
            conju3 = set(jtx3.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.intersecc(conju3,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx1.value == True):
            conju4 = set(jtx4.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.intersecc(conju4,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx2.value == True):
            conju4 = set(jtx4.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.intersecc(conju4,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx3.value == True):
            conju4 = set(jtx4.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.intersecc(conju4,conju3)
            jtxResultado.value = str(resultado)
            page.update()

    def Complemento(e):
        """Condicionales para el complemento de los conjuntos"""
        if(checkjtx1.value == True and checkjtx2.value == True):
            conju1 = set(jtx1.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.Comple(conju1,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx1.value == True and checkjtx3.value == True):
            conju1 = set(jtx1.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.Comple(conju1,conju3)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx1.value == True and checkjtx4.value == True):
            conju1 = set(jtx1.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.Comple(conju1,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx1.value == True):
            conju2 = set(jtx2.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.Comple(conju2,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx3.value == True):
            conju2 = set(jtx2.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.Comple(conju2,conju3)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx2.value == True and checkjtx4.value == True):
            conju2 = set(jtx2.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.Comple(conju2,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx1.value == True):
            conju3 = set(jtx3.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.Comple(conju3,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx2.value == True):
            conju3 = set(jtx3.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.Comple(conju3,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx3.value == True and checkjtx4.value == True):
            conju3 = set(jtx3.value.split())
            conju4 = set(jtx4.value.split())
            resultado = Funciones.Comple(conju3,conju4)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx1.value == True):
            conju4 = set(jtx4.value.split())
            conju1 = set(jtx1.value.split())
            resultado = Funciones.Comple(conju4,conju1)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx2.value == True):
            conju4 = set(jtx4.value.split())
            conju2 = set(jtx2.value.split())
            resultado = Funciones.Comple(conju4,conju2)
            jtxResultado.value = str(resultado)
            page.update()
        elif(checkjtx4.value == True and checkjtx3.value == True):
            conju4 = set(jtx4.value.split())
            conju3 = set(jtx3.value.split())
            resultado = Funciones.Comple(conju4,conju3)
            jtxResultado.value = str(resultado)
            page.update()

        


    def borrar(e):
        jtx1.value = ""
        jtx2.value = ""
        jtx3.value = ""
        jtx4.value = ""
        jtxResultado.value = ""
        checkjtx1.value = False
        checkjtx2.value = False
        checkjtx3.value = False
        checkjtx4.value = False
        page.update()
    #Titulo

    text = ft.Text(
        value = "Conjuntos en python",
        text_align= "CENTER",
        color= ft.colors.WHITE,
        weight= ft.FontWeight.W_100,
        size= 40,
    )
    page.add(text)

    TitulodeCont1 = ft.Text(
        value = "Conjuntos",
        text_align= "CENTER",
        color = ft.colors.WHITE,
        weight= ft.FontWeight.W_100,
        size = 30,
    )
    comentari1 = ft.Text(
        value= "Ingrese los conjuntos: ",
        text_align= "CENTER",
        size= 25,
        weight= ft.FontWeight.W_100,
        color= ft.colors.WHITE
    )
    TituloCont2 = ft.Text(
        value = "Resultado",
        color = ft.colors.WHITE,
        text_align= "CENTER",
        weight= ft.FontWeight.W_100,
        size = 30
    )
    #CheckBox
    checkjtx1 = ft.Checkbox(
        label = "Conju1",
    )
    checkjtx2 = ft.Checkbox(
        label = "Conju2",
    )
    checkjtx3 = ft.Checkbox(
        label = "Conju3",
    )
    checkjtx4 = ft.Checkbox(
        label = "Conju4",
    )
    #TextField
    jtx1 = ft.TextField(
        label= "Conjunto 1",
        width= 300,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,

    )
    jtx2 = ft.TextField(
        label= "Conjunto 2",
        width= 300,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,

    )
    jtx3 = ft.TextField(
        label= "Conjunto 3",
        width= 300,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,

    )
    jtx4 = ft.TextField(
        label= "Conjunto 4",
        width= 300,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,

    )
    jtxResultado = ft.TextField(
        hint_text= "Resultado",
        width= 300,
        border_color= ft.colors.BLUE,
        color= ft.colors.WHITE,
        max_lines= 5,
        min_lines= 5
    )
    #Botones 
    btnGenerar = ft.ElevatedButton(
        text= "Generar",
        width= 120,
        height= 30,
        bgcolor= ft.colors.BLUE,
        color = ft.colors.WHITE,
        on_click= agregar_conjunto
    )
    btnBorrar = ft.ElevatedButton(
        text= "Borrar",
        width= 120,
        height= 30,
        bgcolor= ft.colors.BLUE,
        color = ft.colors.WHITE,
        on_click= borrar
    )
    btnUnion = ft.ElevatedButton(
        text= "Union",
        width= 120,
        height= 30,
        bgcolor= ft.colors.BLUE,
        color = ft.colors.WHITE,
        on_click= Union
    )
    btnInter = ft.ElevatedButton(
        text= "Inter",
        width= 120,
        height= 30,
        bgcolor= ft.colors.BLUE,
        color = ft.colors.WHITE,
        on_click= Interseccion
    )
    btnComple = ft.ElevatedButton(
        text= "Compleme",
        width= 120,
        height= 30,
        bgcolor= ft.colors.BLUE,
        color = ft.colors.WHITE,
        on_click= Complemento
    )
    #Filas
    filaCheck = ft.Row([checkjtx1,checkjtx2,checkjtx3,checkjtx4],alignment=ft.MainAxisAlignment.CENTER,
                       vertical_alignment= ft.CrossAxisAlignment.CENTER)
    filabtn = ft.Row(
        [btnGenerar,btnBorrar],alignment= ft.MainAxisAlignment.CENTER,
        vertical_alignment= ft.CrossAxisAlignment.CENTER
    )
    fila2 = ft.Row([btnUnion,btnInter,btnComple],alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment= ft.CrossAxisAlignment.CENTER)
    #Contenedor
    cont1 = ft.Container(
        content= ft.Column([
            TitulodeCont1,comentari1,jtx1,jtx2,jtx3,jtx4,filabtn,filaCheck
            ],alignment= ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,expand=True),
        margin= 20,
        padding= 30,
        bgcolor= ft.colors.BLACK,
        width= 450,
        height= 550,
    )
    cont2 = ft.Container(
        content= ft.Column(
            [TituloCont2,jtxResultado,fila2],alignment= ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER, expand = True
        ),
        margin = 20,
        padding= 30,
        bgcolor= ft.colors.BLACK,
        width= 450,
        height = 450,
    )
    filacont = ft.Row([cont1,cont2],alignment= ft.MainAxisAlignment.CENTER,
                      vertical_alignment= ft.CrossAxisAlignment.CENTER)
    page.add(filacont)
    page.update()

ft.app(target=main)