 #-*- coding: utf-8 -*- 
#Decoración: Nombre del Algoritmo 
"""print("\n")
print("-------------------------------------------------------") 
print("Ejercicio2: PROMEDIO DE 3 NOTAS.") 
print("-------------------------------------------------------") 
print("\n")
#Entradas 
print("Ingrese las 3 notas del alumno N1 , N2, N3") 
N1 = int( input("N1: ")) 
N2 = int( input("N2: ")) 
N3 = int( input("N3: ")) 
#Proceso 
P = int( (N1+N2+N3)/3 ) 
#Salida
print("\nSalida:")
print( P )"""


 #-*- coding: utf-8 -*- 
#Decoración: Nombre del Algoritmo 
print("-------------------------------------------------------") 
print("Ejercicio3: PUNTAJE FINAL.") 
print("-------------------------------------------------------") 
#Entradas 
print("Ingrese número de respuestas correctas: ") 
RC = int( input()) 
print("Ingrese número de respuestas incorrectas: ") 
RI = int( input()) 
print("Ingrese número de respuestas en blanco: ") 
RB = int( input()) 
#Proceso 
PCR = RC*3 
PRI = RI*-1 
PRB = RB*0 
 
PF = PCR + PRI + PRB 
#Salida 
print("El puntaje total es:", PF) 
