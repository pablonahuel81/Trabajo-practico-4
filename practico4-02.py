#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Por favor ingrese un numero entero y le diremos la cantidad de digitos que contiene el mismo "))
c = 0
while num > 0:
    num = num // 10
    c = c + 1 
print (f"El numero posee", c, "digitos")