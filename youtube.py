import yt_dlp
import os
from tkinter import *
from tkinter import messagebox as MessageBox

# Mostrar el ID del proceso actual
print("ID del proceso:", os.getpid())

# Función para descargar videos
def accion():
    enlace = videos.get()  # Obtén el enlace ingresado
    if not enlace.strip():  # Verifica si el campo está vacío
        MessageBox.showwarning("Error", "Por favor ingresar un enlace de válido.")
        return

    try:
        opciones = {
            'format': 'best',  # Descargar el video de mejor calidad
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Define la ruta de descarga
            'noplaylist': True,  # Evita descargar listas de reproducción, solo un video
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([enlace])  # Descarga el video

        MessageBox.showinfo("Éxito", "Video descargado correctamente.")
    except Exception as e:
        MessageBox.showerror("Error", f"Ocurrió un error: {e}")

# Función para borrar la URL ingresada
def borrar_url():
    videos.delete(0, END)  # Borra el texto en el campo de entrada

# Función para mostrar información del autor
def popup():
    MessageBox.showinfo("Sobre mí", "programa creado por el ingeniero Mairon Salazar") # interpretacion de la informacion a ingrersar 

# Crear la ventana principal
root = Tk()
root.config(bd=15)
root.title("App Descargar Videos")

# Verificar si la imagen existe antes de cargarla
if os.path.isfile("youtube.png"):
    imagen = PhotoImage(file="youtube.png")
    foto = Label(root, image=imagen, bd=0)
    foto.grid(row=0, column=0)
else:
    MessageBox.showwarning("Advertencia", "No se encontró la imagen youtube.png")
    foto = Label(root, text="Imagen no disponible", bd=0)
    foto.grid(row=0, column=0)

# Menú
menubar = Menu(root)
root.config(menu=menubar)

# Menú de información
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Información del autor", command=popup)
menubar.add_cascade(label="Para más información", menu=helpmenu)

# Opción para salir
menubar.add_command(label="Salir", command=root.destroy)

# Texto de instrucciones
instrucciones = Label(root, text="Programa creado en Python por el instructor M. Salazar\n")
instrucciones.grid(row=0, column=1)

# Campo de entrada
videos = Entry(root, width=50)
videos.grid(row=1, column=1)

# Botón de descarga
boton_descargar = Button(root, text="DESCARGAR :)", command=accion)
boton_descargar.grid(row=2, column=1)

# Botón para borrar la URL
boton_borrar = Button(root, text="BORRAR URL", command=borrar_url)
boton_borrar.grid(row=3, column=1)

# Mantener la ventana abierta
root.mainloop()