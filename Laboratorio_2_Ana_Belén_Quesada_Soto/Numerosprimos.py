def numerosprimos (numeroadigitar):

    numeroadigitar = input ("Digite el número que desea:  ")

    try:
        if (numeroadigitar/2):
            print ("No es un número primo")
        else:
            print ("Es un número primo")
    except BaseException:
        print ('Ha finalizado la ejecucion')
    
        input ()
