"""
10.  Trabajo con Archivos: Elabore un programa que cree un archivo denominado 
"numeros.txt", escriba los números del 1 al 20 (uno por línea) y luego lea el archivo e 
imprima su contenido. 
"""

with open("numeros.txt", "w") as archivo:
    for i in range(1, 21):
        archivo.write(f"{i}\n")

with open("numeros.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)