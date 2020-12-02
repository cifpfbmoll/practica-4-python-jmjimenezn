#P4 E4 - rgion
#Pida al usuario tres números y un cuarto número, y compruebe si éste
#último es divisor de los tres números primeros.
numero1=float(input("introduza el primer numero"))
numero2=float(input("introduzca el segundo numero"))
numero3=float(input("introduzca el tercer numero"))
numero4=float(input("introduzca un numero para comprobar si es divisor de los tres primeros"))
if(numero1%numero4==0):
    print(numero4,"es divisor de",numero1)
if(numero2%numero4==0):
    print(numero4,"es divisor de",numero2)
if(numero3%numero4==0):
    print(numero4,"es divisor de",numero3)
    