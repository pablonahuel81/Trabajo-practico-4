#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numero = 0 
numeros_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivos = 0

for n in range (100):
    numero = int(input("Ingrese un numero: ")) 
    if numero % 2 == 0:
        numeros_pares = numeros_pares + 1
    else:
        numeros_impares = numeros_impares + 1
    if numero > 0:
        numeros_positivos = numeros_positivos + 1
    elif numero < 0:
        numeros_negativos = numeros_negativos + 1
print (f"Numeros pares: ", numeros_pares)
print (f"Numeros impares: ", numeros_impares)    
print (f"Numeros negativos: ", numeros_negativos)
print (f"Numeros positivos: ", numeros_positivos)  