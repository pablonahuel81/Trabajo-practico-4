#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
suma = 0
num = int(input("Ingrese numeros, si ingresa un 0 el programa finalizara y sumara los numeros ingresados "))
while num != 0:
    suma = suma + num
    num = int (input("ingrese un numero "))
print (f"La suma total de los numeros ingresados es ", suma,)