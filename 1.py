import customtkinter as tk
from Modulos import *
tk.set_appearance_mode("Light")
def Clicar():
    # lb_Tela1.configure(text=Slider_Tela1.get())
    Tela1.withdraw()
    Tela2.deiconify()

def AlterarTema():
    Tema = Switch_Tela1.get()
    if Tema == 1:
        tk.set_appearance_mode("Dark")
    else:
        tk.set_appearance_mode("Light")

Tela1 = CriarJanelaP("revisão","600x600+500+50",1)

lb_Tela1 = CriarLabel(Tela1, "texto1", 1, 6)
lb_Tela1.configure(text_color="red", font=("arial",18, "bold"))

btn_Tela1 = CriarBotao(Tela1, "gusta babão", Clicar,6,30,2,6)
btn_Tela1.configure(fg_color="gray", hover_color="green")

Caixa_Tela1 = CriarCaixaTexto(Tela1, 200, 30, 3, 6, "Digite o CPF", Modo="CPF")

Switch_Tela1 = CriarSwitch(Tela1,"alteral tema",4,6,AlterarTema)

Combo_Tela1 = CriarComboBox(Tela1, 200, 30,["Gustavo", "Élito", "mafi", "Vitin"], 5,6)

Slider_Tela1 = CriarSlider(Tela1,400,10,6,6)

BarraDeProgresso = CriarProgressBar(Tela1,500,20,8,6)

Imagem = CriarImagem(Tela1,"gojo.png",9,6,300,500)

Tela2 = CriarJanelaP("revisão","600x600+500+50",2 )

Imagem1 = CriarImagem(Tela2,"bear.png",9,6,300,500)
Tela2.withdraw()

Tela1.mainloop()