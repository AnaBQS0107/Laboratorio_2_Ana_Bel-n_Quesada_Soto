import traceback


def calculodehoras(**Kargs):
    try:
        msjBase = ("Bienvenido al calculo de horas laborales")
        if (Kargs["Tipo de trabajador"] == "ET"):
            Horasempleadas= input ("Digite la cantidad de horas trabajadas: \n\r")
            Costeporhora= 1200
            msj = msjBase.format("Empleado temporal", Kargs["Horas empleadas"], Kargs["Coste por hora"])
            calculo1= (Horasempleadas * Costeporhora)
            print(msj,calculo1)
            
        if (Kargs["Tipo de trabajador"] == "EF"):
            Horasempleadas= input ("Digite la cantidad de horas trabajadas: \n\r")
            Costeporhora= 2400
            msj = msjBase.format("Empleado Fijo", Kargs["Horas empleadas"], Kargs["Coste por hora"])
            calculo1= (Horasempleadas * Costeporhora)
            print(msj, calculo1)
            
    except BaseException:
        print(traceback.format_exc())
                 
    input() 
    






        
         