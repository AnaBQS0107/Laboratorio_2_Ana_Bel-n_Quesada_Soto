def elevacionnumeros (numeros1al10, numeros11al20, numeros21al30, numeros31al40, numeros41al50, numeroadigita):
    numeroadigita = input ("Digite el número que desea:  ")
    numeros1al10= 1,2,3,4,5,6,7,8,9,10
    numeros11al20= 11,12,13,14,15,16,17,18,19,20
    numeros21al30= 21,22,23,24,25,26,27,28,29,30
    numeros31al40= 31,32,33,34,35,36,37,38,39,40
    numeros41al50= 41,42,43,44,45,46,47,48,49,50
    
    try:
        if (not numeroadigita.isdigit()):
            return (0)
        if (numeroadigita == numeros1al10):
            numeroadigita = pow(2)
            print (numeroadigita)
        elif (numeroadigita == numeros11al20):
            numeroadigita = pow(4)
            print (numeroadigita)
        elif (numeroadigita == numeros21al30):
            numeroadigita = pow(6)
            print (numeroadigita)
        elif (numeroadigita == numeros31al40):
            numeroadigita = pow(8)
            print (numeroadigita)
        elif (numeroadigita == numeros41al50):
            numeroadigita = pow(10)
            print (numeroadigita)
       
    except BaseException:
        print ('Ha finalizado la ejecucion')
        
        input()

         
             