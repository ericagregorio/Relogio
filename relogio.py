
import tkinter as tk
from time import strftime

# Cria a janela principal
root = tk.Tk()
root.title("Relógio Digital")

# Função para atualizar o horário
def atualizar_horario():
    hora = strftime('%H:%M:%S')
    label_hora.config(text=hora)
    label_hora.after(1000, atualizar_horario)  # Atualiza a cada segundo

# Configuração do rótulo para exibir o horário
label_hora = tk.Label(root, font=('Arial', 50), background='black', foreground='green')
label_hora.pack(anchor='center')

# Chama a função para iniciar o relógio
atualizar_horario()

# Inicia o loop principal da janela
root.mainloop()