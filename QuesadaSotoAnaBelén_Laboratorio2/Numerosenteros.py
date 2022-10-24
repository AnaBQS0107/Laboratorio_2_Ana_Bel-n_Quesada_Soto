def elevacióndenúmeros():
    Numero= input("Digite el número que desea:  ")
    if (Numero == 1 and Numero<10):
        Numero=pow(Numero, 2)
        print ("Su número elevado sería:  " + Numero)
    elif (Numero == 11 and Numero<20):
        Numero=pow(Numero, 4)
        print ("Su número elevado sería:  " + Numero)
    elif (Numero == 21 and Numero<30):
        Numero=pow(Numero, 6)
        print ("Su número elevado sería:  " + Numero)
    elif (Numero == 31 and Numero<40):
        Numero=pow(Numero, 8)
        print ("Su número elevado sería:  " + Numero)
    elif (Numero == 41 and Numero<50):
        Numero=pow(Numero, 10)
        print ("Su número elevado sería:  " + Numero)
    elif (not Numero.isdigit()):
        return (0)
    
elevacióndenúmeros()
