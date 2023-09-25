import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame

def sonido():
    pygame.mixer.init()

    fondo_musical = pygame.mixer.Sound("RECURSOS/fondo.mp3")

    canal_fondo = pygame.mixer.Channel(0)

    canal_fondo.set_volume(0.5)

    canal_fondo.play(fondo_musical, loops=-1)

#sonido()

def detener_audio():
    pygame.mixer.music.stop()

def reproducir_bien():
    pygame.mixer.init()
    pygame.mixer.music.load("RECURSOS/bien.mp3")
    pygame.mixer.music.play(-1)

def detener_audio_bien():
    pygame.mixer.music.stop()

def reproducir_mal():
    pygame.mixer.init()
    pygame.mixer.music.load("RECURSOS/mal.mp3")
    pygame.mixer.music.play(-1)

def detener_audio_mal():
    pygame.mixer.music.stop()

preguntas = [
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿1Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
    'grado': 9,
    'tipo': 'mixta', 
    'pregunta': 'Texto de la pregunta',
    'opciones': ['RECURSOS/opcion1.png', 'RECURSOS/opcion2.png', 'RECURSOS/opcion3.png', 'RECURSOS/opcion4.png'],
    'respuesta_correcta': 'RECURSOS/opcion2.png'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿2Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'imagen': 'RECURSOS/pregunta1.png',
        'texto_debajo_imagen': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿3Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿4Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'imagen': 'RECURSOS/pregunta2.png',
        'texto_debajo_imagen': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': '¿1Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'imagen': 'RECURSOS/pregunta1.png',
        'texto_debajo_imagen': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': '¿2Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': '¿3Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'imagen': 'RECURSOS/pregunta2.png',
        'texto_debajo_imagen': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': '¿2Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '¿1Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '¿2Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 11,
        'tipo': 'imagen',
        'pregunta': '¿3Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'imagen': 'RECURSOS/pregunta2.png',
        'texto_debajo_imagen': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 11,
        'tipo': 'imagen',
        'pregunta': '¿4Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.?',
        'imagen': 'RECURSOS/pregunta1.png',
        'texto_debajo_imagen': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
]

preguntas_disponibles = []
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None
imagen_respuesta_correcta = None
imagen_respuesta_incorrecta = None
preguntas_respondidas = set()

def abrir_ventana_juego(grado):
    global preguntas_disponibles, pregunta_actual, imagen_pregunta_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta, puntaje_actual
    preguntas_disponibles = [pregunta for pregunta in preguntas if pregunta['grado'] == grado]

    if not preguntas_disponibles:
        tk.messagebox.showinfo("Olimpiadas de Matemáticas", "No hay preguntas disponibles para este grado.")
        terminar_juego()
        return

    puntaje_actual = 0
    botones_opciones = []
    preguntas_respondidas.clear()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    def mostrar_pregunta():
     nonlocal botones_opciones
     global pregunta_actual, imagen_pregunta_actual

     if preguntas_disponibles:
        pregunta_actual = random.choice([pregunta for pregunta in preguntas_disponibles if pregunta['pregunta'] not in preguntas_respondidas])
        preguntas_respondidas.add(pregunta_actual['pregunta'])

        pregunta_texto.config(text=pregunta_actual['pregunta'], wraplength=400)
        pregunta_imagen.pack_forget()
        texto_debajo_imagen.config(text='')

        for boton in botones_opciones:
            boton.destroy()
        botones_opciones = []

        if pregunta_actual['tipo'] == 'imagen':
            imagen = Image.open(pregunta_actual['imagen'])
            imagen = imagen.resize((400, 300))
            imagen_pregunta_actual = ImageTk.PhotoImage(imagen)
            pregunta_imagen.config(image=imagen_pregunta_actual)
            pregunta_imagen.image = imagen_pregunta_actual
            pregunta_imagen.pack()
            texto_debajo_imagen.config(text=pregunta_actual.get('texto_debajo_imagen', ''), wraplength=400)

        opciones_frame.pack()

        opciones = pregunta_actual['opciones']
        num_opciones = len(opciones)

        for i in range(num_opciones):
            opcion = opciones[i]
            if isinstance(opcion, str) and opcion.lower().endswith('.png'):
                imagen_opcion = Image.open(opcion)
                imagen_opcion = imagen_opcion.resize((400, 220))

                imagen_width, imagen_height = imagen_opcion.size

                imagen_opcion = ImageTk.PhotoImage(imagen_opcion)
                boton = tk.Button(opciones_frame, text="", image=imagen_opcion, compound="center", width=imagen_width, height=imagen_height, command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
                boton.image = imagen_opcion
            else:
                boton = tk.Button(opciones_frame, text=opcion, font=('Arial', 12), width=20, height=2, command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))

            boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)
            botones_opciones.append(boton)
            
            boton.config(bg='salmon', fg='black', highlightbackground='blue', borderwidth=7, font=('Arial', 12))

        siguiente_boton.config(state=tk.DISABLED)























            
    def verificar_respuesta(respuesta):
        global puntaje_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta
        if pregunta_actual['respuesta_correcta'] == respuesta:
            resultado_texto.config(text='¡Respuesta Correcta!', fg='green')
            puntaje_actual += 10
            puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")
            mostrar_imagen_respuesta(imagen_respuesta_correcta)
        else:
            resultado_texto.config(text='Respuesta Incorrecta', fg='red')
            mostrar_imagen_respuesta(imagen_respuesta_incorrecta)
        siguiente_boton.config(state=tk.NORMAL)

    def mostrar_imagen_respuesta(imagen_respuesta):
        resultado_ventana = tk.Toplevel()
        resultado_ventana.attributes('-fullscreen', True)
        resultado_ventana.overrideredirect(True)
        fondo_label_resultado = tk.Label(resultado_ventana, image=imagen_respuesta)
        fondo_label_resultado.pack(expand=True, fill="both")
        resultado_ventana.update_idletasks()
        width = resultado_ventana.winfo_width()
        height = resultado_ventana.winfo_height()
        x = (resultado_ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (resultado_ventana.winfo_screenheight() // 2) - (height // 2)
        resultado_ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        if imagen_respuesta == imagen_respuesta_correcta:
            reproducir_bien()
        elif imagen_respuesta == imagen_respuesta_incorrecta:
            reproducir_mal()
        resultado_ventana.after(1500, lambda: detener_audio_y_cerrar(resultado_ventana))

    def detener_audio_y_cerrar(ventana_a_cerrar):
        detener_audio_bien()
        detener_audio_mal()
        ventana_a_cerrar.destroy()

    def terminar_juego():
        pregunta_texto.config(text='¡JUEGO TERMINADO!')
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        terminar_boton.config(state=tk.DISABLED)
        if puntaje_actual <= 20:
            resultado_texto.config(fg='red')
        else:
            resultado_texto.config(fg='green') #SRD ❤ VOB
        resultado_texto.config(text=f'Puntaje final: {puntaje_actual}', font=('Arial', 30))
        puntaje_label.config(text='')
        texto_debajo_imagen.config(text='')
        pregunta_imagen.pack_forget()
        ventana_juego.after(3000, ventana_juego.destroy)

    def avanzar_pregunta():
        if not preguntas_disponibles or len(preguntas_respondidas) == len(preguntas_disponibles):
            for boton in botones_opciones:
                boton.config(state=tk.DISABLED)
            siguiente_boton.config(state=tk.DISABLED)
            resultado_imagen.pack_forget()
            resultado_texto.config(text='', fg='black')
            pregunta_texto.config(text='¡NO QUEDAN MAS PREGUNTAS DISPONIBLES!')
            resultado_texto.config(text=f'Puntaje final: {puntaje_actual}', font=('Arial', 30))
            puntaje_label.config(text='')
            texto_debajo_imagen.config(text='')
            pregunta_imagen.pack_forget()
            if puntaje_actual <= 20:
                resultado_texto.config(fg='red')
            else:
                resultado_texto.config(fg='green')
        else:
            siguiente_boton.config(state=tk.DISABLED)
            resultado_imagen.pack_forget()
            resultado_texto.config(text='', fg='white')
        mostrar_pregunta()

    ventana_juego = tk.Toplevel()
    ventana_juego.title(grado)
    ventana_juego.attributes('-fullscreen', True)

    imagen_fondo_juego = Image.open('RECURSOS/fondo_juego.png')
    imagen_fondo_juego = ImageTk.PhotoImage(imagen_fondo_juego)

    fondo_label_juego = tk.Label(ventana_juego, image=imagen_fondo_juego)
    fondo_label_juego.place(x=0, y=0, relwidth=1, relheight=1)
    fondo_label_juego.image = imagen_fondo_juego
    fondo_label_juego.lower()

    pregunta_texto = tk.Label(ventana_juego, text='', font=('Arial', 20))
    pregunta_texto.pack(pady=10)

    pregunta_imagen = tk.Label(ventana_juego)
    pregunta_imagen.pack()

    texto_debajo_imagen = tk.Label(ventana_juego, text='', font=('Arial', 12))
    texto_debajo_imagen.pack(pady=5)

    opciones_frame = tk.Frame(ventana_juego)
    opciones_frame.pack()

    botones_opciones = []
    for i in range(4):
        boton = tk.Button(opciones_frame, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]), borderwidth=7, width=40, bg='salmon', highlightbackground='blue')
        botones_opciones.append(boton)
        boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)

    resultado_texto = tk.Label(ventana_juego, text='', font=('Arial', 20))
    resultado_texto.pack(pady=10)

    resultado_imagen = tk.Label(ventana_juego)

    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 20),  bg='lightblue', width=40, command=avanzar_pregunta)
    siguiente_boton.pack(pady=10)
    siguiente_boton.config(state=tk.DISABLED)

    puntaje_label = tk.Label(ventana_juego, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 25))
    puntaje_label.pack(pady=10)

    terminar_boton = tk.Button(ventana_juego, text='TERMINAR JUEGO', font=('Arial', 12),  bg='red', width=40, command=terminar_juego)
    terminar_boton.pack(pady=10)

    imagen_respuesta_correcta = Image.open('RECURSOS/bien.png')
    imagen_respuesta_correcta = ImageTk.PhotoImage(imagen_respuesta_correcta)
    imagen_respuesta_incorrecta = Image.open('RECURSOS/mal.png')
    imagen_respuesta_incorrecta = ImageTk.PhotoImage(imagen_respuesta_incorrecta)

    mostrar_pregunta()

def chao():
    oli_titulo.config(text='¡JUEGO TERMINADO!')
    etiqueta_grado.config(text='GRACIAS POR JUGAR :D')
    ventana_inicio.after(1000, ventana_inicio.destroy)

ventana_inicio = tk.Tk()
ventana_inicio.title('Olimpiadas de matemáticas')
ventana_inicio.attributes('-fullscreen', True)

icono = tk.PhotoImage(file="RECURSOS/icono.png")
ventana_inicio.iconphoto(True, icono)

imagen_fondo_inicio = Image.open('RECURSOS/fondo_inicio.png')
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

terminar_boton = tk.Button(ventana_inicio, text='CERRAR JUEGO', font=('Arial', 12),  bg='red', width=40,  command=chao)
terminar_boton.pack(pady=10)

ventana_inicio.mainloop()
