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
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)


#----------------
#frama rojo
#----------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red",width=600, height=200)
frame_rojo.place(x=0,y=0)

#----------------
#frama amarillo
#----------------
frame_amarillo=Frame(ventana_principal)
frame_amarillo.config(bg="yellow",width=600, height=400)
frame_amarillo.place(x=0,y=200)

#----------------
#frama rojo
#----------------
frame_rojo=Frame(ventana_principal)
frame_rojo.config(bg="red",width=600, height=200)
frame_rojo.place(x=0,y=400)

#----------------
#frama negro
#----------------
frame_negro=Frame(ventana_principal)
frame_negro.config(bg="black",width=100, height=100)
frame_negro.place(x=200,y=250)


#run
ventana_principal.mainloop()