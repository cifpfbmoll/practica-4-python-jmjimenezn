#P4 E2 - rgion
#Pida al usuario 5 números y diga si estos estaban en orden decreciente,
#creciente o desordenados.

numero1=float(input("Introduzca el primer número "))
numero2=float(input("Introduzca el segundo número "))
numero3=float(input("Introduzca el tercero número "))
numero4=float(input("Introduzca el cuarto número "))
numero5=float(input("Introduzca el quinto número "))
if (numero1<numero2)and(numero2<numero3)and(numero3<numero4)and(numero4<numero5):
    print("los numeros",numero1,numero2,numero3,numero4,numero5,"estan en orden ascendente")
elif (numero1>numero2)and(numero2>numero3)and(numero3>numero4)and(numero4>numero5):
    print ("los numeros",numero1,numero2,numero3,numero4,numero5,"estan en orden descendiente")
else:
    print ("los numeros estan desordenados")