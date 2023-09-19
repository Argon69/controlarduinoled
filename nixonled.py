import tkinter as tk
import serial
import time
from tkinter import messagebox

# Variable global para la conexión serial
arduino = None
baud_rate = 9600  # Velocidad de baudios inicial

# Función para configurar la conexión serial con el Arduino
def configurar_serial():
    global arduino
    global baud_rate  # Se accede a la variable global
    puerto = puerto_entry.get()
    try:
        arduino = serial.Serial(puerto, baud_rate)
        status_label.config(text=f"Conectado al puerto {puerto} ({baud_rate} baud)", fg="#00FF00")  # Color verde
    except serial.SerialException:
        status_label.config(text="Error al conectar al puerto", fg="#FF0000")  # Color rojo

# Función para desconectar el puerto serial
def desconectar_serial():
    global arduino
    if arduino is not None and arduino.isOpen():
        arduino.close()
        status_label.config(text="Puerto desconectado", fg="#FF0000")  # Color rojo
        status_led.config(bg="#FF0000")  # Cambiar color de fondo a rojo

# Funciones para encender y apagar los LEDs
def encender():
    if arduino is not None and arduino.isOpen():
        arduino.write(b'1')
        status_led.config(bg="#00FF00")  # Cambiar color de fondo a verde

def apagar():
    if arduino is not None and arduino.isOpen():
        arduino.write(b'0')
        status_led.config(bg="#FF0000")  # Cambiar color de fondo a rojo

# Función para mostrar información adicional
def mostrar_informacion():
    informacion = """\
    Autor: Nixon Ortiz 8vo A TICS
    Fecha de Creación: 11/09/2023
    Descripción: Este programa sirve para controlar el encendido y apagado de LEDs en Arduino de forma automática.
    """
    messagebox.showinfo("Información Adicional", informacion)

# Función para cambiar la velocidad de baudios
def cambiar_baud_rate():
    global baud_rate
    new_baud_rate = baud_rate_entry.get()
    try:
        baud_rate = int(new_baud_rate)
        status_label.config(text=f"Velocidad de Baudios cambiada a {baud_rate} baud", fg="#00A300")  # Color verde
    except ValueError:
        status_label.config(text="Error: Ingrese un valor válido para Baud Rate", fg="#FF0000")  # Color rojo

# Crear la ventana principal
root = tk.Tk()
root.title("Nixon Control Arduino")

# Configurar fondo de la ventana
root.configure(bg="#121212")  # Color de fondo oscuro

# Etiqueta de estado
status_label = tk.Label(root, text="Desconectado", fg="#FF0000", bg="#121212", font=("Helvetica", 14))
status_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campo de entrada de texto para el puerto serial
puerto_label = tk.Label(root, text="Puerto Serial:", fg="#FFFFFF", bg="#121212", font=("Helvetica", 12))
puerto_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
puerto_entry = tk.Entry(root, font=("Helvetica", 12))
puerto_entry.grid(row=1, column=1, padx=10, pady=5)

# Botón para configurar el puerto serial
configurar_button = tk.Button(root, text="Configurar Puerto Serial", command=configurar_serial, fg="#FFFFFF", bg="#0078D4", font=("Helvetica", 12))
configurar_button.grid(row=2, column=1, columnspan=2, pady=10)

# Botón para desconectar el puerto serial
desconectar_button = tk.Button(root, text="Desconectar Puerto", command=desconectar_serial, fg="#FFFFFF", bg="#FF0000", font=("Helvetica", 12))
desconectar_button.grid(row=2, column=0, columnspan=1, pady=10)

# Campo de entrada de texto para la velocidad de baudios
baud_rate_label = tk.Label(root, text="Velocidad de Baudios:", fg="#FFFFFF", bg="#121212", font=("Helvetica", 12))
baud_rate_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
baud_rate_entry = tk.Entry(root, font=("Helvetica", 12))
baud_rate_entry.insert(0, str(baud_rate))  # Establecer el valor predeterminado en "9600"
baud_rate_entry.grid(row=4, column=1, padx=10, pady=5)

# Botón para cambiar la velocidad de baudios
cambiar_baud_rate_button = tk.Button(root, text="Cambiar Baud Rate", command=cambiar_baud_rate, fg="#FFFFFF", bg="#0078D4", font=("Helvetica", 12))
cambiar_baud_rate_button.grid(row=5, column=1, columnspan=2, pady=10)

# Etiqueta para mostrar el estado del LED
status_led = tk.Label(root, text="LED", width=60, height=2, bg="#FF0000")  # Inicialmente rojo
status_led.grid(row=6, column=0, columnspan=2, pady=10)

# Estilo para los botones
button_style = {'fg': '#FFFFFF', 'bg': '#0078D4', 'font': ('Helvetica', 14)}

# Botones para encender y apagar los LEDs
encender_button = tk.Button(root, text="ENCENDER LEDs", command=encender, **button_style)
apagar_button = tk.Button(root, text="APAGAR LEDs", command=apagar, **button_style)

# Colocar los botones en la ventana
encender_button.grid(row=7, column=0, pady=10)
apagar_button.grid(row=7, column=1, pady=10)

# Botón para mostrar información adicional
informacion_button = tk.Button(root, text="Más Información", command=mostrar_informacion, fg="#FFFFFF", bg="#00A300", font=("Helvetica", 12))
informacion_button.grid(row=8, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
