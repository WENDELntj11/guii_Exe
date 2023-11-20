import tkinter as tk
def mostrar_mensagem():
    label.config(text="Olá, Tudo bem?  bem vindo ao nosso Mundo!")
janela = tk.Tk()
janela.title("Exemplo de GUI em Python")
label = tk.Label(janela, text="Bem-vindo à GUI em Python")
label.pack(padx=10, pady=10)
botao = tk.Button(janela, text="Clique Aqui", command=mostrar_mensagem)
botao.pack(padx=10, pady=10)
janela.mainloop()