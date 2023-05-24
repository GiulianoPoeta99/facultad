program ejercicioMod;
uses crt;
var

numeroY,numeroX: integer;
resultado: real;

begin
resultado:= 0;
writeln('Ingrese el valor para X');
readln(numeroX);
writeln('Ingrese el valor para Y');
readln(numeroY);

resultado := numeroX Mod numeroY;

Writeln('El MOD entre x,y, es: ', resultado);
readkey;
end.
