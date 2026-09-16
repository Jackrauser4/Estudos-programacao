import tkinter as tk
import psutil
import threading
import time

# Janela principal
janela = tk.Tk()
janela.title("Monitor de Hardware")
janela.geometry("300x150")

# Labels que vão mostrar o texto (equivalente às JProgressBar do Java)
label_cpu = tk.Label(janela, text="CPU: 0%", font=("Arial", 14))
label_cpu.pack(pady=10)

barra_cpu = tk.Canvas(janela, width=250, height=20, bg="white")
barra_cpu.pack()

label_ram = tk.Label(janela, text="RAM: 0%", font=("Arial", 14))
label_ram.pack(pady=10)

barra_ram = tk.Canvas(janela, width=250, height=20, bg="white")
barra_ram.pack()

def desenhar_barra(canvas, valor):
    canvas.delete("all")
    largura = 250 * (valor / 100)
    canvas.create_rectangle(0, 0, largura, 20, fill="green")

def monitorar():
    while True:
        cpu_uso = psutil.cpu_percent(interval=1)  # já calcula sozinho, sem "ticks"
        ram_uso = psutil.virtual_memory().percent

        label_cpu.config(text=f"CPU: {cpu_uso:.2f}%")
        desenhar_barra(barra_cpu, cpu_uso)

        label_ram.config(text=f"RAM: {ram_uso:.2f}%")
        desenhar_barra(barra_ram, ram_uso)

# Roda o monitoramento em uma thread separada (igual você fez em Java)
thread = threading.Thread(target=monitorar, daemon=True)
thread.start()

janela.mainloop()