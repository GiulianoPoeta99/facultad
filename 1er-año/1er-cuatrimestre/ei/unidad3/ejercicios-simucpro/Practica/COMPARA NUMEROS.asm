CLA
MSG "El numero Mayor"
LDT "Ingrese el primer numero"
STA 0A1
LDT "Ingrese el segundo numero"
STA 0A2
CMP 0A1
JMA 100   ;Salta a la posicion de memoria 100 si ax es mayor, o sea el segundo numero
LDA 0A1   ;Si no carga en ax el primer numero cargado
EAP "El numero mayor es:
HLT

#100
EAP "El numero mayor es:
HLT



