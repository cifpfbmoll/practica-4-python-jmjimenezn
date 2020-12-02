#P4 E3 - rgion
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado,
#y pida los datos según que caso y muestre el resultado
area=input("quiere calcular el área de un cuadrado o de un triangulo?")
if(area=="triangulo"):
    base=float(input("introduzca la bse del triangulo"))
    altura=float(input("introduzca la altura del triangulo"))
    area=(base*altura)/2
    print("El area del triangulo es de",area)
if(area=="cuadrado"):
    lado=float(input("introduce la longitud del lado del cuadrado"))
    area=lado**2
    print("el area del cuadrado es de",area)
else:
    print("introduca una geometria válida")