import tkinter as tk  # Importa o Tkinter com o apelido tk

# Esta função será executada quando o usuário clicar no botão Somar
def somar():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())

    resultado = n1 + n2

    lbl_resultado.config(text=f"Resultado: {resultado}")


# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x250")  # Largura x altura, em pixels

# Cria o texto e a caixa de entrada do primeiro número
lbl_numero1 = tk.Label(janela, text="Primeiro número:")
lbl_numero1.pack()  # Posiciona o componente na janela

entrada1 = tk.Entry(janela)
entrada1.pack()

# Cria o texto e a caixa de entrada do segundo número
lbl_numero2 = tk.Label(janela, text="Segundo número:")
lbl_numero2.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

# Cria o botão e associa o clique à função somar
botao_somar = tk.Button(
    janela,
    text="Somar",
    command=somar  # Sem (): a função será chamada somente no clique
)
botao_somar.pack(pady=15)  # Adiciona espaço vertical ao redor do botão

# Cria o espaço onde o resultado será exibido
lbl_resultado = tk.Label(janela, text="Resultado:")
lbl_resultado.pack()

# Mantém a janela aberta e aguardando as ações do usuário
janela = tk.Tk()
janela.title("Teclado da calculadora")

botao_7 = tk.Button(janela, text="7", width=6)
botao_7.grid(row=0, column=0)

botao_8 = tk.Button(janela, text="8", width=6)
botao_8.grid(row=0, column=1)

botao_9 = tk.Button(janela, text="9", width=6)
botao_9.grid(row=0, column=2)


janela.mainloop()