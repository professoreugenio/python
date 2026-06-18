import tkinter as tk

def mostrar_mensagem():
    label_resultado.config(text="Botão clicado!")

janela = tk.Tk()
janela.title("Exemplo com botão")
janela.geometry("400x300")

botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem)
botao.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()