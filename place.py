import tkinter as tk

def criar_interface_place():
    # Criar a janela principal
    janela_place = tk.Tk()
    janela_place.title("Gerenciador place() 📐")
    janela_place.geometry("300x300")

    # Criar labels usando place()
    label1 = tk.Label(janela_place, text="Row 0, Col 0", bg="red", fg="white")
    label1.place(x=10, y=10, width=130, height=50)

    label2 = tk.Label(janela_place, text="Row 0, Col 1", bg="green", fg="white")
    label2.place(x=160, y=10, width=130, height=50)

    label3 = tk.Label(janela_place, text="Row 1, Col 0", bg="blue", fg="white")
    label3.place(x=10, y=70, width=130, height=50)

    label4 = tk.Label(janela_place, text="Row 1, Col 1", bg="purple", fg="white")
    label4.place(x=160, y=70, width=130, height=50)

    # Criar botão de fechar
    botao_fechar = tk.Button(janela_place, text="Fechar", command=janela_place.destroy)
    botao_fechar.place(x=100, y=250, width=100, height=30)

    # Iniciar o loop principal
    janela_place.mainloop()

# Chamar a função para criar a interface
criar_interface_place()