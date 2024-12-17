import tkinter as tk

def criar_interface():
    janela_atividade = tk.Tk()
    janela_atividade.title("atividade de layout")
    janela_atividade.geometry("600x400")
    frame = tk.Frame()
    tk.Label(janela_atividade, text="Row 0, Col 0", bg="red", fg="white").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(janela_atividade, text="Row 0, Col 1", bg="green", fg="white").grid(row=0, column=1, padx=5, pady=5)
    tk.Label(janela_atividade, text="Row 1, Col 0", bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(janela_atividade, text="Row 1, Col 1", bg="purple", fg="white").grid(row=1, column=1, padx=5, pady=5)




  
    



    janela_atividade.mainloop()

criar_interface()   


     