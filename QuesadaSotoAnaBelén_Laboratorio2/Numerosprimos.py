def numerosprimos ():

    numeroadigitar = input ("Digite el número que desea:  ")

    if (numeroadigitar<= 1):
        return ("No es un número primo")
    elif (numeroadigitar == 2):
        return ("Es un número primo")
    else:
        for i in range (2, numeroadigitar):
            if numeroadigitar%i == 0:
                return ("No es un número primo")
        return ("Es un número primo")
            
numerosprimos()
