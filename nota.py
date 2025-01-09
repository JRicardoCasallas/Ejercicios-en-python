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
"""print("-------------------------------------------------------") 
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
print("El puntaje total es:", PF) """







# -*- coding: utf-8 -*- 

#Decoración: Nombre del Algoritmo 
"""print("-------------------------------------------------------") 
print("Ejercicio4: PUNTAJE TOTAL DE PARTIDOS.") 
print("-------------------------------------------------------") 
 
#Entradas 
print("Ingrese número de partidos ganados") 
PG = int( input()) 
print("Ingrese número de partidos empatados") 
PE = int( input()) 
print("Ingrese número de partidos perdidos") 
PP = int( input()) 
 
#Proceso 
PPG = PG*3 
PPE = PE*1 
PPP = PP*0 
 
PF = PPG + PPE + PPP 
 
#Salida 
print("\nSALIDA: ") 
print("-------------------------------------------------------") 
print("Puntaje Final: ", PF)"""







 # -*- coding: utf-8 -*- 
import math #librería necesaria para usar funciones Matemáticas 
#en este caso math.ceil(), que redondea un numero al Entero      superior 
 
#Decoración: Nombre del Algoritmo 
print("-------------------------------------------------------") 
print("Ejercicio5: NÚMERO DE MICRO DISCOS 3.5 NECESARIOS") 
print("-------------------------------------------------------") 
 
#Entradas 
print("Ingrese GB: ") 
GB = float( input()) 
 
#Proceso 
MG = GB*1024 
MD = MG/1.44 
 
#Salida 
print("\nSALIDA: ") 
print("-------------------------------------------------------") 
print(MD) 
#En caso de Decimal Aproximar al siguiente entero 
#Ya que la parte decimal debe ser almacenada en otro DISCO 3.5 
print("Numero de Discos necesarios: ", math.ceil(MD)) 
