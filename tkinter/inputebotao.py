import tkinter as tk

# Função executada quando o botão for clicado
def enviar_valor():
    valor = campo_input.get()
    resultado.config(text=f"Você digitou: {valor}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha primeira janela")
janela.geometry("300x200")

# Texto inicial
texto = tk.Label(janela, text="Digite um valor:")
texto.pack(pady=10)

# Campo input
campo_input = tk.Entry(janela, width=30)
campo_input.pack(pady=5)

# Botão para enviar
botao = tk.Button(janela, text="Enviar", command=enviar_valor)
botao.pack(pady=10)

# Label para mostrar o resultado
resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

# Mantém a janela aberta
janela.mainloop()