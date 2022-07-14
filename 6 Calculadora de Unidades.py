from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Cores usadas no projeto
cor1 = "#121111"  # Preto
cor2 = "#fafafa"  # Branco
cor3 = "#fcba03"  # Amarelo/Dourado
cor4 = "#08018f"  # Azul

janela = Tk()
janela.title("Conversor")
janela.geometry("650x260")
janela.configure(bg=cor2)
#janela.attributes('-alpha', 0.9)


# Dicionário

unidades = {
    'Massa': [{'kg': 1000}, {'hg': 100}, {'dag': 10}, {'g': 1}, {'dg': 0.1}, {'cg': 0.01}, {'mg': 0.001}],
    'Comprimento': [{'km': 1000}, {'hec': 100}, {'dec': 10}, {'m': 1}, {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001}],
    'Tempo': [{'ano': 31557600}, {'mes': 2629800}, {'sem': 604800}, {'dia': 86400}, {'h': 3600}, {'min': 60}, {'seg': 1}],
    'Área': [{'acre': 247.105}, {'hect': 100}, {'km²': 1}, {'m²': 1000000}, {'cm²': 10000000000}, {'mm²': 1000000000000}],
    'Quantidade': [{'m³': 0.0010000008}, {'L': 1}, {'ml': 1000}, {'copo': 4.16667}, {'xícara': 3.51951109807}, {'colher': 56.312149346710782538}, {'onça': 35.195107883963160589}],
    'Velocidade': [{'milhas/h': 2.2369363636364}, {'pes/s': 3.28084}, {'m/s': 1}, {'km/h': 3.6}, {'nós': 1.94384}],
    'Temperatura': [{'celcius': 0}, {'fahrenheit': 32}, {'kelvin': 273.15}],
    'Energia': [{'MW': 1000000}, {'KW': 1000}, {'W': 1}, {'mW': 0.001}, {'uW': 0.000001}],
    'Pressão': [{'bar': 1}, {'atm': 3.28084}, {'pascal': 100000}, {'psi': 14.5}, {'torr': 750.062}],
}

# Função


def mostrar_menu(i):

    unidade_de = []
    unidade_para = []
    unidade_valores = []

    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    combobox_de['values'] = unidade_de
    combobox_para['values'] = unidade_para
    label_titulo_mostrador['text'] = i

    def calcular():
        a = combobox_de.get()
        b = combobox_para.get()

        numero_para_converter = float(entrada_numero.get())
        distancia = unidade_para.index(b) - unidade_de.index(a)

        if unidade_para.index(a) <= unidade_de.index(b):
            distancia = unidade_para.index(b) - unidade_de.index(a)
            resutlado = numero_para_converter * (10**distancia)
            print(resutlado)

        else:
            distancia = unidade_de.index(a) - unidade_para.index(b)
            resutlado = numero_para_converter / (10**distancia)

        if unidade_para.index(a) > unidade_de.index(b):
            distancia = unidade_para.index(b) - unidade_de.index(a)
            resutlado = numero_para_converter / (10**distancia)
            print(resutlado)

        else:
            distancia = unidade_de.index(a) - unidade_para.index(b)
            resutlado = numero_para_converter * (10**distancia)

    # Label, botão e entrada
    label_info = Label(frame_lateral, text="Valor à converter:",
                       width=15, height=1, padx=0, pady=3, relief=FLAT, anchor="center", font="Raleway 10 bold", bg=cor2, fg=cor1)
    label_info.place(x=0, y=110)

    entrada_numero = Entry(frame_lateral, width=9,
                           font='Raleway 10', justify="center", relief=SOLID)
    entrada_numero.place(x=8, y=137)

    botao_calcular = Button(frame_lateral, command=calcular, text="Calcular", width=20, height=1, overrelief=RIDGE,
                            relief=RAISED, anchor="center", font="Raleway 10 ", bg=cor3, fg=cor2)
    botao_calcular.place(x=8, y=220)

    label_resultado = Label(frame_lateral, text="---",
                            width=10, height=1, padx=0, pady=3, relief=FLAT, anchor=W, font="Raleway 18 bold", bg=cor2, fg=cor1)
    label_resultado.place(x=7, y=170)


# Frame superior (títulos)
frame_titulos = Frame(janela, width=450, height=50, pady=0, padx=0, relief=FLAT,
                      bg=cor2)
frame_titulos.place(x=2, y=2)


# Frame inferior (unidades)

frame_unidades = Frame(janela, width=450, height=205, pady=0, padx=0, relief=FLAT,
                       bg=cor2)
frame_unidades.place(x=2, y=53)


# Frame lateral (conversor)

frame_lateral = Frame(janela, width=196, height=256,
                      pady=0, padx=3, relief=FLAT, bg=cor2)
frame_lateral.place(x=453, y=2)


# Estilo da janela

estilo = ttk.Style(janela)
estilo.theme_use("clam")


# Labels frame superior

label_tituloapp = Label(frame_titulos, text="Conversor de Unidades",
                        height=1, padx=0, relief=FLAT, anchor="center", font="Raleway 16 bold", bg=cor2, fg=cor1)
label_tituloapp.place(x=100, y=10)


# Botões de opções de unidades de medida
img_massa = Image.open('icons/iconmass.png')
img_massa = img_massa.resize((50, 50), Image.LANCZOS)
img_massa = ImageTk.PhotoImage(img_massa)
botao_massa = Button(frame_unidades, command=lambda: mostrar_menu('Massa'), text="     Massa", image=img_massa, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_massa.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)


img_tempo = Image.open('icons/icontempo.png')
img_tempo = img_tempo.resize((50, 50), Image.LANCZOS)
img_tempo = ImageTk.PhotoImage(img_tempo)
botao_tempo = Button(frame_unidades, command=lambda: mostrar_menu('Tempo'), text="     Tempo", image=img_tempo, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_tempo.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)


img_compr = Image.open('icons/iconcompr.png')
img_compr = img_compr.resize((50, 50), Image.LANCZOS)
img_compr = ImageTk.PhotoImage(img_compr)
botao_compr = Button(frame_unidades, command=lambda: mostrar_menu('Comprimento'), text="Comprimento", image=img_compr, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_compr.grid(row=0, column=3, sticky=NSEW, pady=5, padx=5)


img_area = Image.open('icons/iconarea.png')
img_area = img_area.resize((50, 50), Image.LANCZOS)
img_area = ImageTk.PhotoImage(img_area)
botao_area = Button(frame_unidades, command=lambda: mostrar_menu('Área'), text="      Área", image=img_area, compound=LEFT, width=130, height=50, overrelief=SOLID,
                    relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_area.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)


img_quant = Image.open('icons/iconquan.png')
img_quant = img_quant.resize((50, 50), Image.LANCZOS)
img_quant = ImageTk.PhotoImage(img_quant)
botao_quant = Button(frame_unidades, command=lambda: mostrar_menu('Quantidade'),  text=" Quantidade", image=img_quant, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_quant.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)


img_vel = Image.open('icons/iconvel.png')
img_vel = img_vel.resize((50, 50), Image.LANCZOS)
img_vel = ImageTk.PhotoImage(img_vel)
botao_compr = Button(frame_unidades, command=lambda: mostrar_menu('Velocidade'), text="   Velocidade", image=img_vel, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_compr.grid(row=1, column=3, sticky=NSEW, pady=5, padx=5)


img_tempe = Image.open('icons/icontempera.png')
img_tempe = img_tempe.resize((50, 50), Image.LANCZOS)
img_tempe = ImageTk.PhotoImage(img_tempe)
botao_tempe = Button(frame_unidades, command=lambda: mostrar_menu('Temperatura'), text="Temperatura", image=img_tempe, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_tempe.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)


img_energ = Image.open('icons/iconener.png')
img_energ = img_energ.resize((50, 50), Image.LANCZOS)
img_energ = ImageTk.PhotoImage(img_energ)
botao_energ = Button(frame_unidades, command=lambda: mostrar_menu('Energia'),  text="    Energia", image=img_energ, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_energ.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)


img_press = Image.open('icons/iconpress.png')
img_press = img_press.resize((50, 50), Image.LANCZOS)
img_press = ImageTk.PhotoImage(img_press)
botao_press = Button(frame_unidades, command=lambda: mostrar_menu('Pressão'), text="     Pressão", image=img_press, compound=LEFT, width=130, height=50, overrelief=SOLID,
                     relief=SOLID, anchor=NW, font="Raleway 9 ", bg=cor3, fg=cor2)
botao_press.grid(row=2, column=3, sticky=NSEW, pady=5, padx=5)

# Mostrador da direita

label_titulo_mostrador = Label(frame_lateral, text="Unidades",
                               width=15, height=1, pady=5, relief=FLAT, anchor="center", font="Raleway 16 bold", bg=cor2, fg=cor1)
label_titulo_mostrador.place(x=0, y=10)


label_de = Label(frame_lateral, text="De",
                 height=1, padx=3, relief=FLAT, anchor="center", font="Raleway 10 italic", bg=cor2, fg=cor1)
label_de.place(x=0, y=70)

combobox_de = ttk.Combobox(frame_lateral, width=5,
                           justify=CENTER, font="Raleway 8")
combobox_de.place(x=26, y=71)


label_para = Label(frame_lateral, text="Para",
                   height=1, padx=3, relief=FLAT, anchor="center", font="Raleway 10", bg=cor2, fg=cor1)
label_para.place(x=90, y=70)

combobox_para = ttk.Combobox(frame_lateral, width=5,
                             justify=CENTER, font="Raleway 8")
combobox_para.place(x=125, y=71)


janela.mainloop()
