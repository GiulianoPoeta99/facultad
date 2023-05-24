#SimuProc 1.4.2.0
MSG "Hola"
MSG MENU
MSG 1 SUMA
MSG 2 RESTA
MSG 3 DIV
MSG 4 MUL

LDT "Ingrese opcion"     ; Ingreso opcoin del menu
STA  00A

CMP 100    ;COmparo con el uno guardado y si es igual voy a la operacion de suma
JEQ 200
CMP 101
JEQ 300
CMP 102
JEQ 400
CMP 103
JEQ 500
MSG "Ninguna opcion valida"
JMP 001

#100
1    ;opcion uno
10    ;opcion dos
11    ;opcion 3
100   ;opcion 4

#200
;suma
ldt "ingrese un numero"
sta 210
ldt "ingrese segundo numero"
add 210
eap
hlt

#300
msg "resta"
HLT
#400
msg "Multiplicacion"
HLT
#500
msg "division"
HLT


