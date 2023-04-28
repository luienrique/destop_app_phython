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
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana 
ventana_principal.config(bg="yellow")
#----------------
#frama amarillo
#----------------
frame_amarillo=Frame(ventana_principal)
frame_amarillo.config(bg="yellow",width=500, height=125)
frame_amarillo.place(x=0,y=0)


#----------------
#frama azul
#----------------
frame_azul=Frame(ventana_principal)
frame_azul.config(bg="blue",width=500, height=125)
frame_azul.place(x=0,y=250)

#----------------
#frama rojo
#----------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red",width=500, height=125)
frame_rojo.place(x=0,y=375)


#run
ventana_principal.mainloop()
