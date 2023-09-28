import customtkinter as tk
from PIL import Image

def CriarJanelaP(Titulo,Tamanho,Tipo,Redimensionar=False):
    if Tipo ==1:
        janela = tk.CTk()
    elif Tipo ==2:
        janela = tk.CTkToplevel()
    elif Tipo ==3:
        janela = tk.CTkInputDialog()
    janela.title(Titulo)
    janela.geometry(Tamanho)
    if Redimensionar !=False:
        janela.resizable(width=True, height=True)
    else:
        janela.resizable(width=False, height=False)
    colunas = list(range(13))
    linhas = list(range(13))
    janela.grid_columnconfigure(colunas, weight=1)
    janela.grid_rowconfigure(linhas, weight=1)
    return janela

def CriarLabel(Local,Texto,Linha,Coluna):
    label = tk.CTkLabel(Local,text=Texto)
    label.grid(row=Linha, column = Coluna)
    return label

def CriarCaixaTexto(Local,Largura,Altura,Linha,Coluna,Texto="nada",Modo="Padrão"):
    Caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    Caixa.grid(row=Linha, column=Coluna)
    if Texto!="nada":
        Caixa.configure(placeholder_text=Texto)
    if Modo == "Senha":
        Caixa.configure(show="*")
    elif Modo == "Moeda":
        def format_moeda(event=None):
            text = Caixa.get().replace("R$", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "R$" + text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_moeda)
    if Modo == "CPF":
        def format_cpf(event=None):
            text = Caixa.get().replace(".", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):

                if not text[index] in "0123456789": continue
                if index in [2, 5]:
                    new_text += text[index] + "."
                elif index == 8:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_cpf)
    elif Modo == "CNPJ":
        def format_CNPJ(event=None):
            text = Caixa.get().replace(".", "").replace("/", "").replace("-", "")[:14]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 7:
                    new_text += text[index] + "/"
                elif index == 11:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_CNPJ)
    elif Modo == "Telefone":
        def format_tel(event=None):
            text = Caixa.get().replace("(", "").replace(")", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 1:
                    new_text += text[index] + ")"
                elif index == 5:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_tel)
    elif Modo == "Data":
        def format_data(event=None):
            text = Caixa.get().replace("/", "")[:8]
            new_text = ""
            if event.keysym.lower() == "backspace":
                return
            for index in range(len(text)):
                if not text[index] in "0123456789":
                    continue
                if index in [1, 3]:
                    new_text += text[index] + "/"
                elif index == 9:
                    new_text += text[index]
                else:
                    new_text += text[index]
            Caixa.delete(0, "end")
            Caixa.insert(0, new_text)

        Caixa.bind("<KeyRelease>", format_data)
    return Caixa

def CriarBotao(Local,Texto,Comando,Largura,Altura,Linha,Coluna):
    btn = tk.CTkButton(Local,text=Texto,command=Comando,width=Largura,height=Altura)
    btn.grid(row=Linha,column=Coluna)
    return btn

#---------------CheckBox---------------
def CriarCheckBox(Local,Texto,Linha,Coluna,Comando=0):
    check = tk.CTkCheckBox(Local,text=Texto)
    check.grid(row=Linha,column=Coluna)
    if Comando!=0:
        check.configure(command=Comando)
    return check

#---------------ComboBox---------------
def CriarComboBox(Local,Largura,Altura,Valores,Linha,Coluna,Comando=0):
    combo= tk.CTkComboBox(Local, width=Largura, height=Altura,
                          values=Valores, state="readonly")
    combo.grid(row=Linha, column=Coluna)
    combo.set("Selecione")
    if Comando!=0:
        combo.configure(command=Comando)
    return combo

#---------------ProgressBar---------------
def CriarProgressBar(Local,Largura,Altura,Linha,Coluna):
    progress =tk.CTkProgressBar(Local,width=Largura,height=Altura)
    progress.grid(row=Linha,column=Coluna)
    progress.set(0)
    return progress

#---------------Switch---------------
def CriarSwitch(Local,Texto,Linha,Coluna,Comando=0):
    switch = tk.CTkSwitch(Local,text=Texto)
    switch.grid(row=Linha,column=Coluna)
    if Comando!=0:
     switch.configure(command=Comando)
    return switch

#---------------Slider---------------
def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider=tk.CTkSlider(Local,width=Largura,height=Altura)
    slider.grid(row=Linha,column=Coluna)
    slider.set(0)
    return slider

def CriarImagem(Local,Caminho,Linha, Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.grid(row=Linha, column =Coluna)
    return imagem