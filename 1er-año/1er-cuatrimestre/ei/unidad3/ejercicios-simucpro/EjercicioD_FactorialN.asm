#SimuProc 1.4.2.0
#Factorial de N numero
msg Bienvenido al Ejercicio_D
msg Sacar Factorial de un numero N.
ldt Por favor introduzca N:
sta 022;     Guardo Ax(N), en variable N
lda 021;     Cargo en Ax, el valor de i
cmp 022;     Comparo (i <= N)
jme 010;
jeq 010;     Si es menor-igual salta al 010.

lda 020;     Ax       := Factorial
mov 020,023; Factorial:= 1
mov 021,023; i        := 1
mov 022,023; N        := 1
msg El valor de Factor N, es:
eap
hlt

#020
001  ; Variable Factorial
#021
001  ; Variable i
#022
001  ; Variable N
#023
001  ; Variable ZeroMultiplicativo.


#010
cla       ; Ax := 0, por seguridad
lda 020   ; Ax:= Factorial
mul 021   ; Ax:= Ax(Factorial)*i
sta 020   ; Factorial:= Ax
cla       ; Limpio Ax, denuevo por siacaso.
inc 021   ; i:=i+1
jmp 004   ; Salto al inicio de comparacion.


