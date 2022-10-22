import cadenatexto as CT 
import Horasempleadas as HE
import NombreUIA as NU
import Numeroentero as NE 
import Numerosprimos as NP

try:
    while(True):
        opcionesdeusuario = input ("Digite la opción que desea:  \n\r 1- Calculo de horas empleadas \n\r 2- UIA \n\r 3-Potencias \n\r 4-Numeros primos \n\r 5-Texto \n\r 6-Salir")
        if(not opcionesdeusuario.isdigit()):
            print ('Ha ingresado un caracter fuera de los preestablecidos')
            continue
        elif(opcionesdeusuario==1):
            resultado = HE.calculodehoras
            print (HE.calculodehoras)
        elif(opcionesdeusuario==2):
            resultado = NU.nombredeusuario
            print (NU.nombredeusuario)
        elif(opcionesdeusuario==3):
            resultado = NP.numerosprimos
            print (NP.numerosprimos)
        elif(opcionesdeusuario==4):
            resultado = NE.elevacionnumeros
            print(NE.elevacionnumeros)
        elif(opcionesdeusuario==5):
            resultado = CT.contadorletras
            print (CT.contadorletras)
        elif(opcionesdeusuario==6):
            break
        
except BaseException:
    print ('Ha finalizado la ejecucion')
    
    input ()
            