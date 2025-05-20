#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Usuario ingrese un numero "))
suma = 0
for n in range (num + 1):
    suma = suma + n
print ("La suma de los numeros desde 0 hasta", num, "es ", suma)