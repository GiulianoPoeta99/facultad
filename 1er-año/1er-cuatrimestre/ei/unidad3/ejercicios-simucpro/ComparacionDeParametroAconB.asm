#SimuProc 1.4.2.0
#Compara A con B
msg Bienvenido al Ejercicio2
msg Usted me dara 2 parametros
msg Si ParametroA > ParametroB
msg Sumaremos.
msg Si ParametroA < ParametroB
msg Restaremos.
ldt Por favor, ingrese el ParametroA:
xab ;Pongo el parametroA en Bx.
ldt Por favor, ingrese el ParametroB:
sta 020 ; Ahora paso el parametroB a 01a
xab ;Devuelvo el parametroA a Ax.
cmp 020; Comparo A con B
jeq 015; Saltar si son iguales.
jma 019; Saltar si A es MAYOR.
sub 020; Restar A(ax)-B(01a) porque son menores
msg Debido a que ParametroB es mayor,
msg Se efectuarizará una resta.
msg El resultado es:
eap
hlt

#015
msg Por favor no coloque parametros iguales.
msg Vuelva a intentar.
jmp 006

#019
add 020
msg Como el Parametro A es Mayor,
msg Se realizará una suma.
msg El resultado es:
eap
hlt




