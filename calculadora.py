
import tkinter as tk

# Função para adicionar números ao visor
def digitar(valor):
    visor.insert(tk.END, valor)

# Função para limpar o visor
def limpar():
    visor.delete(0, tk.END)

# Função para somar
def somar():
    try:
        numeros = visor.get().split("+")
        n1 = float(numeros[0])
        n2 = float(numeros[1])

        resultado = n1 + n2

        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))

    except (ValueError, IndexError):
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("250x300")

# Criar visor
visor = tk.Entry(
    janela,
    width=24,
    justify="right",
    font=("Arial", 16)
)
visor.grid(row=0, column=0, columnspan=3, padx=2, pady=10)

botao_0 = tk.Button(
    janela, text="1", width=6,
    command=lambda: digitar("1")
)
botao_0.grid(row=5, column=0,columnspan=3, padx=2, pady=2)


botao_1 = tk.Button(
    janela, text="1", width=6,
    command=lambda: digitar("1")
)
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(
    janela, text="2", width=6,
    command=lambda: digitar("2")
)
botao_2.grid(row=4, column=0, padx=2, pady=2)

botao_3 = tk.Button(
    janela, text="3", width=6,
    command=lambda: digitar("3")
)
botao_3.grid(row=4, column=, padx=2, pady=2)




botao_4 = tk.Button(
    janela, text="4", width=3,
    command=lambda: digitar("4")
)
botao_4.grid(row=3, column=1, padx=2, pady=2)

botao_5 = tk.Button(
    janela, text="5", width=3,
    command=lambda: digitar("5")
)
botao_5.grid(row=3, column=2, padx=2, pady=2)

botao_6 = tk.Button(
    janela, text="6", width=3,
    command=lambda: digitar("6")
)
botao_6.grid(row=3, column=3, padx=2, pady=2)




botao_7 = tk.Button(
    janela, text="7", width=3,
    command=lambda: digitar("7")
)
botao_7.grid(row=2, column=1, padx=2, pady=2)

botao_8 = tk.Button(
    janela, text="8", width=3,
    command=lambda: digitar("8")
)
botao_8.grid(row=2, column=2, padx=2, pady=2)

botao_9 = tk.Button(
    janela, text="9", width=3,
    command=lambda: digitar("9")
)
botao_9.grid(row=2, column=3, padx=2, pady=2)









# Botões de operação
botao_mais = tk.Button(
    janela, text="+", width=6,
    command=lambda: digitar("+")
)
botao_mais.grid(row=3, column=4, padx=2, pady=2)

botao_c = tk.Button(
    janela, text="C", width=6,
    command=limpar
)
botao_c.grid(row=1, column=1, padx=2, pady=2)

botao_igual = tk.Button(
    janela, text="=", width=6,
    command=somar
)
botao_igual.grid(row=5, column=4, padx=2, pady=10)



# Manter janela aberta
janela.mainloop()
