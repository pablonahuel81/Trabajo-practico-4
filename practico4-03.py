#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores

num1 = int(input("Primer numero "))
num2 = int(input("Segundo numero "))
if num1 > num2:
    num1, num2 = num2, num1

num1 = num1 + 1
suma = 0

while num1 < num2:
    suma = suma + num1
    num1 = num1 + 1
print ("La suma es ", suma,)