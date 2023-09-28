import customtkinter as tk
from Modulos import *
tk.set_appearance_mode("Light")
def Clicar():
    # lb_Tela1.configure(text=Slider_Tela1.get())
    #Tela1.withdraw()
    #Tela2.deiconify()
    if Caixa_Tela1.get() == "alex@gmail.com" and CaixaSenha.get() == "12":
        Tela2.deiconify()
        Tela1.withdraw()
    else:
        print("E-mail ínvalido")

def Voltar():
    Tela1.withdraw()
    Tela1.deiconify()

def Cadastro():
    pass

Tela1 = CriarJanelaP("revisão","600x600+500+50",1)

lb_Tela1 = CriarLabel(Tela1, "TELA LOGIN", 1, 6)
lb_Tela1.configure(text_color="red", font=("arial",18, "bold"))
Caixa_Tela1 = CriarCaixaTexto(Tela1, 200, 30, 3, 6, "Digite o E-mail")
btn_Tela1 = CriarBotao(Tela1, "Logar", Clicar,6,30,5,6)
btn_Tela1.configure(fg_color="gray", hover_color="green")
btn_Tela1 = CriarBotao(Tela1, "Cadastro", Cadastro,6,30,6,6)
btn_Tela1.configure(fg_color="gray", hover_color="green")

CaixaSenha = CriarCaixaTexto(Tela1, 200, 30, 4, 6, "Digite a sua Senha", Modo="Senha")

Tela2 = CriarJanelaP("Logado","600x600+500+50",2 )
Tela2.withdraw()
lb_Tela2 = CriarLabel(Tela2, "Logado", 1, 6)
lb_Tela2.configure(text_color="red", font=("arial",18, "bold"))
btn_Tela1 = CriarBotao(Tela2, "Voltar", Voltar,6,30,6,6)
btn_Tela1.configure(fg_color="gray", hover_color="green")

Tela3 = CriarJanelaP("Logado","600x600+500+50",2 )
Tela3.withdraw()
lb_Tela3 = CriarLabel(Tela3, "Cadastro", 1, 6)
lb_Tela3.configure(text_color="red", font=("arial",18, "bold"))
CaixaNome = CriarCaixaTexto(Tela3, 200, 30, 2, 6, "Digite seu Nome", Modo="")
CaixaSenha2 = CriarCaixaTexto(Tela3, 200, 30, 3, 6, "Digite sua Senha", Modo="Senha")
CaixaLogin = CriarCaixaTexto(Tela3, 200, 30, 4, 6, "Digite o login que voce deseja", Modo="")
btn_Tela1 = CriarBotao(Tela3, "Cadastro", Cadastro,6,30,5,6)
btn_Tela1.configure(fg_color="gray", hover_color="green")

btn_Tela1 = CriarBotao(Tela3, "Voltar", Voltar,6,30,6,6)
btn_Tela1.configure(fg_color="gray", hover_color="green")


Tela1.mainloop()