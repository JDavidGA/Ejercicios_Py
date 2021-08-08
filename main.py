from Areas import Area_Circulo, Area_Cuadrado, Area_Rectangulo
from Perimetro import Perimetro_Circulo ,Perimetro_Cuadrado, Perimetro_Rectangulo

def main():
    print("#"*70)
    print("PROGRAMA PARA CALCULAR AREAS Y PERIMETROS DE LAS FIGURAS GEOMETRICAS")
    print("#"*70)
    Figura = input("Escriba el nombre de la figura geometrica:  ")
    if Figura == "Circulo":
        Area_Circulo()
        Perimetro_Circulo()
    elif Figura == "Cuadrado":
        Area_Cuadrado()
        Perimetro_Cuadrado()
    elif Figura == "Rectangulo":
        Area_Rectangulo()
        Perimetro_Rectangulo()
    else:
        print("No se puede calcular la figura",Figura)

if __name__==("__main__"):
   main()
    
        