
def Perimetro_Cuadrado():
    Lado = float(input("Digite el lado del cuadrado"))
    return print("El Perimetro del Cuadrado es  ",Lado **4)





def Perimetro_Rectangulo():
    Base = float(input("Digite la base del rectangulo"))
    Altura = float(input("Digite la altura"))
    return print ("El Perimetro del rectangulo",(Base**2) + (Altura**2))





def Perimetro_Circulo():
    pi = 3.1416
    Radio = float(input("Digite el radio del circulo"))
    return print("Area del circulo es", (pi**2) +(Radio*2))



if __name__==("__main__"):
   main()