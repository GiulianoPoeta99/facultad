#SimuProc 1.4.2.0
MSG  "Programa 2"
MSG "Menu"
MSG "1 - Saludo"
MSG "2 - Despedida"
LDT "Ingrese una opción"
CMP 015 ;La comparo con la opcion 1
JEQ 020 ;Si es uno salto a 020
CMP 016 ;La comparo con la opc 2"
JEQ 030 ;Salto si es la opcion 2
MSG "Ninguna opcion valida"
JMP 000

#020
MSG "La opcion elegida es la uno"
HLT

#030
MSG "La opcion elegida es la dos"
HLT




#015
1
10

