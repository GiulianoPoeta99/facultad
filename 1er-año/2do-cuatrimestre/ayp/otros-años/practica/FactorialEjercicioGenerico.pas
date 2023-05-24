program Factorial;
uses crt;
var

numero,cota:longint;
contador:integer;

begin
clrscr;
write ('Escriba un numero:');
read (cota);
contador:= 1;
numero:= 1;
repeat
    numero := numero * contador;
    contador:= contador +1;
until
    contador > cota;
    writeln('El factorial del numero es: ', numero);
    readkey;
end.
