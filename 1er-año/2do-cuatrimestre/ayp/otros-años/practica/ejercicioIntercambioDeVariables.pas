program ejercicioIntercambioDeVariables;
uses crt;
var

variableA,variableB,alternative:Integer;

begin
writeln('Ingrese el valor para la primera variable');
readln(variableA);
writeln('Usted a ingresado el valor: ', variableA);

writeln('Ingrese el valor para la segunda variable');
readln(variableB);
writeln('Usted a ingresado el valor: ', variableB);

alternative:= variableB;
variableB:= variableA;
variableA:= alternative;

writeln('Ahora en la primera variable se almacena: ', variableA);
writeln('y en la segunda variable se almacena: ', variableB);
writeln('La idea de este ejercicio es poder intercambiar la data');
writeln('entre dos variables, muchas gracias.');

readkey;
end.
