import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame
import os

# AUDIO-------------------------------
def reproducir_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(-1)

def detener_audio():
    pygame.mixer.music.stop()

#reproducir_audio()

# PREGUNTAS---------------------------------
# Define una lista de preguntas y respuestas en el formato adecuado
preguntas = [
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿Cuál es la capital de Francia?',
        'opciones': ['Madrid', 'París', 'Berlín', 'Londres'],
        'respuesta_correcta': 'París'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿Cuál es la capital de Francia?',
        'imagen': 'IMG/pregunta1.png',
        'texto_debajo_imagen': 'holaaaaaaa',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': '¿Cuál de estas opciones es 1?',
        'imagen': 'IMG/pregunta1.png',
        'texto_debajo_imagen': 'holaaaaaaa',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '1'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '¿Cuál es el símbolo del hierro?',
        'opciones': ['Fe', 'He', 'H', 'Ir'],
        'respuesta_correcta': 'Fe'
    },
]

# Variables globales
preguntas_disponibles = []
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None
imagen_respuesta_correcta = None
imagen_respuesta_incorrecta = None

# Función para abrir la ventana de juego
def abrir_ventana_juego(grado):
    global preguntas_disponibles, puntaje_actual, pregunta_actual, imagen_pregunta_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta
    # Filtrar preguntas según el grado seleccionado
    preguntas_disponibles = [pregunta for pregunta in preguntas if pregunta['grado'] == grado]

    if not preguntas_disponibles:
        # Si no hay preguntas disponibles para el grado, mostrar un mensaje y salir
        tk.messagebox.showinfo("Olimpiadas de Matemáticas", "No hay preguntas disponibles para este grado.")
        return

    # Inicializar la lista de botones de opciones
    botones_opciones = []

    def mostrar_pregunta():
        nonlocal botones_opciones  # Usar nonlocal para modificar la variable externa
        global pregunta_actual, puntaje_actual, imagen_pregunta_actual
        if preguntas_disponibles:
            pregunta_actual = random.choice(preguntas_disponibles)
            pregunta_texto.config(text=pregunta_actual['pregunta'])

            if pregunta_actual['tipo'] == 'imagen':
                imagen = Image.open(pregunta_actual['imagen'])
                imagen = imagen.resize((400, 300))
                imagen_pregunta_actual = ImageTk.PhotoImage(imagen)
                pregunta_imagen.config(image=imagen_pregunta_actual)
                pregunta_imagen.image = imagen_pregunta_actual
                pregunta_imagen.pack()

                # Mostrar el texto debajo de la imagen
                texto_debajo_imagen.config(text=pregunta_actual.get('texto_debajo_imagen', ''))

                # Mostrar las opciones de respuesta para preguntas de imagen
                opciones_frame.pack()
                for i in range(4):
                    botones_opciones[i].config(text=pregunta_actual['opciones'][i])
                    botones_opciones[i].config(state=tk.NORMAL)
            elif pregunta_actual['tipo'] == 'texto':
                pregunta_imagen.pack_forget()  # Ocultar la imagen si es una pregunta de texto
                texto_debajo_imagen.config(text='')  # Ocultar el texto debajo de la imagen
                opciones_frame.pack()  # Mostrar las opciones si es una pregunta de texto
                for i in range(4):
                    botones_opciones[i].config(text=pregunta_actual['opciones'][i])
                    botones_opciones[i].config(state=tk.NORMAL)

    def verificar_respuesta(respuesta):
     global puntaje_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta
     if pregunta_actual['respuesta_correcta'] == respuesta:
        resultado_texto.config(text='¡Respuesta Correcta!', fg='green')
        puntaje_actual += 10
        mostrar_imagen_respuesta(imagen_respuesta_correcta)
     else:
        resultado_texto.config(text='Respuesta Incorrecta', fg='red')
        mostrar_imagen_respuesta(imagen_respuesta_incorrecta)
     siguiente_boton.config(state=tk.NORMAL)

    def mostrar_imagen_respuesta(imagen_respuesta):
     resultado_imagen.config(image=imagen_respuesta)
     resultado_imagen.image = imagen_respuesta
     resultado_imagen.pack()  # Muestra la imagen en la parte superior
     resultado_imagen.lift()  # Coloca la imagen en la parte superior de la ventana
     ventana_juego.after(2000, ocultar_imagen_respuesta)  # Oculta la imagen después de 2 segundos

    def ocultar_imagen_respuesta():
        resultado_imagen.pack_forget()
        #mostrar_pregunta() <---se elimina para que no avanze el juego al ocultar la imagen de los monos

    def terminar_juego():
        pregunta_texto.config(text='Juego Terminado')
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        resultado_texto.config(text=f'Puntaje final: {puntaje_actual}')
    
    def avanzar_pregunta():
     siguiente_boton.config(state=tk.DISABLED)
     resultado_imagen.pack_forget()  # Ocultar la imagen de respuesta
     mostrar_pregunta()

    # Crear la ventana de juego
    ventana_juego = tk.Toplevel()
    ventana_juego.title(grado)
    
    ventana_juego.attributes('-fullscreen', True)

    # Configurar el fondo de imagen para la ventana de juego
    imagen_fondo_juego = Image.open('IMG/fondo_juego.png')
    imagen_fondo_juego = ImageTk.PhotoImage(imagen_fondo_juego)
    fondo_label_juego = tk.Label(ventana_juego, image=imagen_fondo_juego)
    fondo_label_juego.place(x=0, y=0, relwidth=1, relheight=1)
    fondo_label_juego.lift()  # Coloca el fondo en la parte inferior

    resultado_imagen = tk.Label(ventana_juego)
    resultado_imagen.pack()
    resultado_imagen.lift()


    # Etiqueta para mostrar la pregunta o imagen
    pregunta_texto = tk.Label(ventana_juego, text='', font=('Arial', 14))
    pregunta_texto.pack(pady=10)

    # Imagen de la pregunta
    pregunta_imagen = tk.Label(ventana_juego)
    pregunta_imagen.pack()

    # Etiqueta para mostrar el texto debajo de la imagen
    texto_debajo_imagen = tk.Label(ventana_juego, text='', font=('Arial', 12))
    texto_debajo_imagen.pack()

    # Frame para las opciones
    opciones_frame = tk.Frame(ventana_juego)
    opciones_frame.pack()

    botones_opciones = []
    for i in range(4):
        boton = tk.Button(opciones_frame, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]), borderwidth=7, width=40, bg='salmon', highlightbackground='blue')
        botones_opciones.append(boton)
        boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)  # Diseño de 2 arriba y 2 abajo

    resultado_texto = tk.Label(ventana_juego, text='', font=('Arial', 12))
    resultado_texto.pack(pady=10)

    resultado_imagen = tk.Label(ventana_juego)  # Para mostrar la imagen de respuesta
    resultado_imagen.pack()

    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 12),  bg='lightblue', width=40, command=avanzar_pregunta)
    siguiente_boton.pack(pady=10)
    siguiente_boton.config(state=tk.DISABLED)
    
    puntaje_label = tk.Label(ventana_juego, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 12))
    puntaje_label.pack(pady=10)

    # Iniciar el juego mostrando la primera pregunta
    mostrar_pregunta()

    # Cargar imágenes de respuesta
    imagen_respuesta_correcta = Image.open('IMG/bien.png')
    imagen_respuesta_correcta = ImageTk.PhotoImage(imagen_respuesta_correcta)
    imagen_respuesta_incorrecta = Image.open('IMG/mal.png')
    imagen_respuesta_incorrecta = ImageTk.PhotoImage(imagen_respuesta_incorrecta)

# Ventana de inicio para seleccionar el grado
ventana_inicio = tk.Tk()
ventana_inicio.title('Olimpiadas de matemáticas')
ventana_inicio.attributes('-fullscreen', True)

icono = tk.PhotoImage(file="IMG/icono.png")
# Establecerlo como ícono de la ventana.
ventana_inicio.iconphoto(True, icono)

# Configurar el fondo de imagen para la ventana de inicio
imagen_fondo_inicio = Image.open('IMG/fondo_inicio.png')  # Reemplaza 'fondo_inicio.png' con la ruta de tu imagen de fondo para la ventana de inicio
imagen_fondo_inicio = ImageTk.PhotoImage(imagen_fondo_inicio)
fondo_label_inicio = tk.Label(ventana_inicio, image=imagen_fondo_inicio)
fondo_label_inicio.place(x=0, y=0, relwidth=1, relheight=1)

oli_titulo = tk.Label(ventana_inicio, text='OLIMPIADAS DE MATEMATICAS', bg="white", fg="black", pady=20, font=('bold', 50))
oli_titulo.pack(pady=10)

etiqueta_grado = tk.Label(ventana_inicio, text='Selecciona el grado:', bg="white", fg="black", pady=20, font=('bold', 50))
etiqueta_grado.pack(pady=10)

boton_grado_9 = tk.Button(ventana_inicio, text='Grado 9°', bg="white", fg="black", font=('arial', 25), width=18, height=2, pady=2, command=lambda: abrir_ventana_juego(9))
boton_grado_9.pack(pady=15)

boton_grado_10 = tk.Button(ventana_inicio, text='Grado 10°', bg="white", fg="black", font=('arial', 25), width=18, height=2, command=lambda: abrir_ventana_juego(10))
boton_grado_10.pack(pady=15)

boton_grado_11 = tk.Button(ventana_inicio, text='Grado 11°', bg="white", fg="black", font=('arial', 25), width=18, height=2,  command=lambda: abrir_ventana_juego(11))
boton_grado_11.pack(pady=15)

ventana_inicio.mainloop()
