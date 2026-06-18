import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira janela")
janela.geometry("300x200")

texto = tk.Label(janela, text="Olá, mundo!")
texto.pack()

janela.mainloop()