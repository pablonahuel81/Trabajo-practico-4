#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

sumatoria = 0
media_valores = 0
for n in range (100):
    numero = int (input("Ingrese un numero: "))
    sumatoria = sumatoria + numero
media_valores = sumatoria / 100
print (f"La media de los numeros ingresados es: ", media_valores)