#SimuProc 1.4.2.0
#Suma de 3 numeros

msg Bienvenido al programa 1
msg Aqui sumaremos 3 numeros.
ldt Por favor ingrese el primer numero:
sta 01a
ldt Por favor ingrese el segundo numero:
add 01a
mov ax,01a
ldt Por favor ingrese el tercer numero:
add 01a
msg La sumatoria de los numeros es:
eap
hlt
