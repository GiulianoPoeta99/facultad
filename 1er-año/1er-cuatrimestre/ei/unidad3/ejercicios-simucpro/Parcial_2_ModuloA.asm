#SimuProc 1.4.2.0
MSG ‘Que hago?’
LDT ‘Ingrese un número:’
STA 00F
LDT ‘Ingrese un número:’
NOT Ax
ADD 00F
JNO 009
INC Ax
JMP 00D
NOT Ax
STA 00F
CLA
SUB 00F
EAP ‘...’; ¿Qué mensaje corresponde poner aquí?
HLT
