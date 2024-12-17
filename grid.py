import tkinter as tk

def criar_interface_grid():
 janela_grid = tk.Tk()
 janela_grid.title("Gerenciador grid() 📐")
 janela_grid.geometry("300x300")
 
 tk.Label(janela_grid, text="Row 0, Col 0", bg="red", fg="white").grid(row=0, column=0, padx=5, pady=5)
 tk.Label(janela_grid, text="Row 0, Col 1", bg="green", fg="white").grid(row=0, column=1, padx=5, pady=5)
 tk.Label(janela_grid, text="Row 1, Col 0", bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)
 tk.Label(janela_grid, text="Row 1, Col 1", bg="purple", fg="white").grid(row=1, column=1, padx=5, pady=5)

 tk.Button(janela_grid, text="Fechar", command=janela_grid.destroy).grid(row=2, column=0, columnspan=2, pady=10)

 tk.mainloop()

criar_interface_grid()