#SimuProc 1.4.2.0
#Averigua cual es el mayor y el menor de N numeros.
#Parte 1 del Codigo: "Inside The Loop"
#Pequeña Adicion: "Cuanto de largo el loop maestro?"
CLA;                      Limpio Ax -Protocolo.
LDT "Cuantos Números quiere darme para calcular Amo?"
STA 020; Cargo en Pos(020) el valor del loop.
DEC 020; Decremento en 1, ya que la primera ves se pide por fuera del loop.

MOV Cx,020;               Cargo en Cx lo que esta en la Pos(020)
LDT "Ingrese un Número: ";Pido al Usuario el 1er Número.
STA 021;                  Lo guardo en la Variable MENOR.
STA 022;                  Lo guardo en la Variable MAYOR.
LDT "Ingrese un Número: ";Solicito a Usuario un siguiente Número.
CMP 021;                  Comparo Ax con La variable Menor.
JME 018;                  Si es menor se va a la pos(015).
CMP 022;                  Comparo Ax con La variable Mayor.
JMA 01C;                  Si es mayor se va a la pos(01A).
LOOP 008;                 Repite el proceso hasta que Cx=0.

#Parte 2 del Codigo: "Fuera del Loop"
LDA 021;                         (Ax:= MENOR)
EAP "El numero mas pequeño es: ";Muestro en pantalla el resultado del menor.
LDA 022;                         (Ax:= MAYOR)
EAP "El numero mas grande es: "; Muestro en pantalla el resultado del mayor.

#Parte 3 del Codigo -Adicional: "Limpieza"
MOV 020,023; Cargo en la Pos(020) 0.
MOV 021,023; Cargo en la Pos(021) 0.
MOV 022,023; Cargo en la Pos(022) 0.  Por seguridad.
HLT;         Fin.


#Apartado: "Funcion Modulo Independiente"

#018
STA 021;  Guardo Ax en La Variable MENOR. (Menor:= Ax)
LOOP 008; Verifico si termine el loop para volver.
JMP 00E;  Si termine el loop salto a la parte 2 del codigo.

#01C
STA 022;  Guardo Ax en La Variable MAYOR. (Mayor:= Ax)
LOOP 008; Verifico si termine el loop para volver.
JMP 00E;  Si termine el loop salto a la parte 2 del codigo.


#Apartado: "Variables"
#020
100;  (Loop Value:4)+ la que esta fuera de iteracion, total 5.
#021
1; Variable Menor.
#022
1; Variable Mayor.
#023
0; Variable Zero.













