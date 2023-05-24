#SimuProc 1.4.2.0
#EjercicioD_TP5: Resto por Complemento.

#Primera Parte: Pido Valores.
CLA; Protocolo-
MSG "Vamos a restar A-B por complemento Amo"
MSG "Recuerde que para que funcione,"
MSG "La resta debe dar negativo."
LDT "Ingrese A: "
STA 021; Guardo A en 021.
LDT "Ingrese B:"
CMP 021; Comparo si es mayor o menor o igual.
JME 016; Si es menor a A salta a 016.
JEQ 01B; Si es Igual a A salta a 01B.

#Segunda Parte: Resto por Complemento.
STA 022; Guardo B en 022.
NOT 022; Pos(022)=B => Pos(022)= B*
CLA;     Limpio Ax Protocolo.
LDA 021; Ax:= A;
ADD 022; Ax:= A+(B*)
NOT Ax;  Ax:= Resultado*
EAP "El resultado es el negativo de: "

#Tercera Parte: Limpieza.
MOV 021,023; Limpio Parametro A.
MOV 022,023; Limpio Parametro B.
CLA;         Limpio Parametro Ax.
HLT

#Cuarta Parte: Modulos de Error.
#016
MSG "Recuerde Amo, que el numero debe ser"
MSG "Mayor, que A, para que de negativo."
MSG "Por favor, vuelva a ingresar un numero."
JMP 006;
#01B
MSG "Disculpe Amo, pero si pone"
MSG "El mismo numero el resultado es 0"
MSG "Y este ejercicio no tendria sentido."
MSG "Por favor, vuelva a ingresar un numero."
JMP 006;

#Variables:
#021
0; Parametro A.
#022
0; Parametro B.
#023
0; La Intocable.
