#SimuProc 1.4.2.0
#Suma de N Parametros

#Segmento_Inicio
CLA;         Por Protocolo Ax:=0
MOV 011,012; Temporal:= 0
LDT "Cuantos Parametros sumare hoy Amo mio?: "
STA 010;     Nloop:= Ax
MOV Cx,010;  Cx:= Nloop

#Segmento_Loop
LDT "Ingrese Parametro: "
ADD 011;     Ax:= Ax+Temporal
STA 011;     Temporal:= Ax
LOOP 005;    SegmentoLoop en Loop

#Segmento_Final
LDA 011; Ax:= Temporal
EAP "Amo, el resultado es: "
HLT;     Finalizo


#Variables:
#010
0; Nloop
#011
0; Temporal
#012
0; SiempreZero
