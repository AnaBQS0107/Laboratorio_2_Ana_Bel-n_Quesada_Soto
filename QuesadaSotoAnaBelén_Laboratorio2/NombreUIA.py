
def nombredeusuario ():
   Nombredelapersona = input ("Digite su nombre completo: \n\r")
   MensajeBase = ("Bienvenidos a la UIA ")

   msj= (MensajeBase + Nombredelapersona)
   
   print (msj.lower())
   print (msj.upper())
   print (msj.format())


nombredeusuario()
