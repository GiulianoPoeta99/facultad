#SimuProc 1.4.2.0
#Promedio
msg Bienvenido al EjercicioC
msg Hoy promediaremos entre 4 Parametros.
msg Por favor ingrese los 4 parametros:
ldt Parametro 1
mov 020,ax      ; Pido Parametro 1 y guardo en la memoria 020.
ldt Parametro 2
mov 021,ax     ; Pido Parametro 2 y guardo en la memoria 021.
ldt Parametro 3
mov 022,ax      ; Pido Parametro 3 y guardo en la memoria 022.
ldt Parametro 4
mov 023,ax      ; Pido Parametro 4 y guardo en la memoria 023.
msg Muchas gracias Usuario,
msg Ahora procedere a calcular el promedio.

cla
mov ax,020; Ahora Ax:=020
add 021;    Ahora Ax:= Ax+021
add 022;    Ahora Ax:= Ax+022
add 023;    Ahora Ax:= Ax+023
div 024;    Ahora Ax:= Ax/4

msg El Promedio de los 4 parametros es:
eap
hlt

#024
100    ; Almaceno 4 en la memoria 024 para invocar a la division.






