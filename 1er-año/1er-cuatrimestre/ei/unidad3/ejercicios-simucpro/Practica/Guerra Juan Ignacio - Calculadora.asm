#SimuProc 1.4.2.0
CLA
MSG "1) Suma, 2) Resta, 3) Mult, 4) Div, 5) Salir"
LDT "Ingrese una opcion"
CMP 10E ;Comparar con el 5
JEQ 602 ;Salto al HLT, termina el programa
STA 0AC ;Guardo la opcion para compararlo luego

LDT "Ingrese un numero A"
STA 0AA
LDT "Ingrese un numero B"
STA 0AB
;A estos dos numeros los guardamos en 0AA y 0AB para
;usarlos despues

;Retiramos 0AC (Si el usuario no eligio "5) Salir")
;Y lo usamos para ir a las respectivas operaciones
CLA
LDA 0AC
CMP 10A ;Comparo con el 1
JEQ 200 ;voy hasta la suma
CMP 10B ;Comparo con el 2
JEQ 300 ;voy hasta la resta
CMP 10C ;Comparar con el 3
JEQ 400 ;voy hasta la mult.
CMP 10D ;Comparar con el 4
JEQ 500 ;voy hasta la div.
MSG "Opcion no valida"
JMP 000 ;Reiniciar programa

#200
;Suma
CLA
LDA 0AA
ADD 0AB
EAP "El resultado de la suma es: "
JMP 000
#300
;Resta
CLA
LDA 0AA
SUB 0AB
EAP "El resultado de la resta es: "
JMP 000
#400
;Multiplicacion
CLA
LDA 0AA
MUL 0AB
EAP "El resultado de la mult. es: "
JMP 000
#500
;Division
;Antes de hacer la division, nos aseguramos
;de verificar si nuestro numero B no es 0
CLA
CMP 0AB
JEQ 600
CLA
LDA 0AA
DIV 0AB ;Ya que el numero B no es 0, dividiremos
EAP "El resultado de la div. es: "
JMP 000
;Failsafe
#600
MSG "Operacion Imposible"
JMP 000
HLT

;Dejamos cargados los valores que debemos usar
;Para la comparacion de opciones
#10A
00000001
00000010
00000011
00000100
00000101

;En cada operacion nos aseguramos de usar CLA para limpiar AX
;Cosa de que no haya algun tipo de residuo
