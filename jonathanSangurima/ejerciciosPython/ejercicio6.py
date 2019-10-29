"""
    @autor: reroes
    nombre: ejercicio1.py
    descripción: ...
"""
# System.out.println("Ingrese su nombre")
# nombre = entrada.nextLine

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nota1 = input("Ingrese el valor de su nota 1: ")
nota2 = input("Ingrese el valor de su nota 2: ")

suma = int(nota1) + int(nota2);
promedio = suma / 2;

print("%s -- %s\nSu suma de notas es %s\nSu promedio es %s\n" %
	(nombre, edad, suma, promedio))




