import tkinter 

ventana = tkinter.Tk()
ventana.title("Title TB")
ventana.geometry("500x500")
ventana.configure(background="medium purple")
ventana.title("RECORDATORIO")
cabecera = tkinter.Label(ventana,text = "PRUEBA1", bg = "purple", fg = "white").pack()
texto = tkinter.Label(ventana,text = "PRUEBA1", bg = "deep pink2").pack()
text = tkinter.Label(ventana,text = "PRUEBA2", bg = "blue violet").pack()
text = tkinter.Label(ventana,text = "PRUEBA3", bg = "dark violet").pack()
text = tkinter.Label(ventana,text = "PRUEBA4", bg = "violet red").pack()
text = tkinter.Label(ventana,text = "PRUEBA5", bg = "magenta").pack()

ventana.mainloop() 