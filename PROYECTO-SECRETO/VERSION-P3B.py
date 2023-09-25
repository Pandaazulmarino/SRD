import tkinter as tk
import random
from PIL import Image, ImageTk

# Define una lista de preguntas y respuestas en el formato adecuado
preguntas = [
    {
        'tipo': 'texto',
        'pregunta': '¿Cuál es la capital de Francia?',
        'opciones': ['Madrid', 'París', 'Berlín', 'Londres'],
        'respuesta_correcta': 'París'
    },
    {
        'tipo': 'imagen',
        'pregunta': 'pregunta1.png',  # Asegúrate de que la imagen esté en la misma carpeta que este script
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '1'
    },
    {
        'tipo':'texto',
        'pregunta':'¿Cuál es el símbolo del hierro?',
        'opciones':['Fe','He','H','Ir'],
        'respuesta_correcta':'Fe'
    },
    # Agrega más preguntas aquí en el mismo formato
]

# Configura la ventana principal
ventana = tk.Tk()
ventana.title('Juego de Preguntas y Respuestas')

# Variables globales
preguntas_disponibles = preguntas.copy()
puntaje_actual = 0
pregunta_actual = None

# Variable para mostrar la pregunta actual
pregunta_texto = tk.StringVar()

# Crea la etiqueta para mostrar la pregunta como una imagen o texto
pregunta_label = tk.Label(ventana)
pregunta_label.pack(pady=10)

def mostrar_pregunta():
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    resultado_texto.set('')

    if not preguntas_disponibles:
        pregunta_texto.set('No hay más preguntas disponibles.')
        siguiente_boton.config(state=tk.DISABLED)
        terminar_juego()
        return

    pregunta_actual = random.choice(preguntas_disponibles)
    pregunta_texto.set(pregunta_actual['pregunta'])

    if pregunta_actual['tipo'] == 'imagen':
        # Cargar y mostrar la imagen de la pregunta
        imagen_pregunta = Image.open(pregunta_actual['pregunta'])
        imagen_pregunta = imagen_pregunta.resize((400, 300))
        imagen_pregunta = ImageTk.PhotoImage(imagen_pregunta)
        pregunta_label.config(image=imagen_pregunta)
        pregunta_label.image = imagen_pregunta
    else:
        pregunta_label.config(image=None)  # Elimina cualquier imagen previa

    for i, opcion in enumerate(pregunta_actual['opciones']):
        botones_opciones[i].config(text=opcion)

    siguiente_boton.config(state=tk.DISABLED)
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

def verificar_respuesta(respuesta):
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    if pregunta_actual['respuesta_correcta'] == respuesta:
        resultado_texto.set('¡Respuesta Correcta!')
        puntaje_actual += 10
    else:
        resultado_texto.set('Respuesta Incorrecta')
    siguiente_boton.config(state=tk.NORMAL)
    preguntas_disponibles.remove(pregunta_actual)

def terminar_juego():
    pregunta_texto.set('Juego Terminado')
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
    resultado_texto.set(f'Puntaje final: {puntaje_actual}')
    pregunta_label.config(image=None)  # Elimina cualquier imagen al finalizar el juego

# Botones para opciones de respuesta
botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
    botones_opciones.append(boton)
    boton.pack(pady=5)

# Variable para mostrar si la respuesta fue correcta o incorrecta
resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto, font=('Arial', 12))
resultado_label.pack(pady=10)

# Botón "Siguiente"
siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial', 12), command=mostrar_pregunta)
siguiente_boton.pack(pady=10)
siguiente_boton.config(state=tk.DISABLED)

# Puntaje Actual
puntaje_actual = 0
puntaje_label = tk.Label(ventana, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 12))
puntaje_label.pack(pady=10)

# Iniciar el juego
mostrar_pregunta()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
