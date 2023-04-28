# ---------------
#destktop app No.1
#----------------


#se imprta la libreria de tkinter con todas sus funciones
from tkinter import *

#----------------
# funciones de la app
#--------------

#---------------------------
#ventana principal de la app
#----------------------------

# se declara una variable llamada ventana_principal,que adquiere las carasteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo en la ventana
ventana_principal.title("bandera de colombia")

# tamañode la ventana 
ventana_principal.geometry("800x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

#----------------
#frama azul
#----------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red",width=800, height=800)
frame_rojo.place(x=0,y=0)


#----------------
#frama rojo
#----------------


#----------------
#frama blanco
#----------------
frame_blanco=Frame(ventana_principal)
frame_blanco.config(bg="white",width=800, height=200)
frame_blanco.place(x=0,y=100)

#----------------
#frama blanco
#----------------
frame_blanco=Frame(ventana_principal)
frame_blanco.config(bg="white",width=200, height=800)
frame_blanco.place(x=100,y=0)

frame_azul=Frame(ventana_principal)
frame_azul.config(bg="blue",width=800, height=100)
frame_azul.place(x=0,y=150)

#----------------
#frama azul
#----------------
frame_azul=Frame(ventana_principal)
frame_azul.config(bg="blue",width=100, height=600)
frame_azul.place(x=150,y=0)

#run
ventana_principal.mainloop()