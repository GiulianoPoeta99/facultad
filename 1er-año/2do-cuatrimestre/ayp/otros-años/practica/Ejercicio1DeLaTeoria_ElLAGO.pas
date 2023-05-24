program ejercicio1ResoluciondeProblemas;
uses crt;


//Ejercicio 1:
//Un lago que tiene la forma de un triángulo rectángulo, está circunscripto
//entre tres terrenos cuadrados de los que se conoce su superficie, tal como
//se presentan en la figura, se desea conocer la superficie del lago.

//Para resolver mi consigna primero necesito saber que:
//1) Para sacar el lado de un cuadrado necesito sacar la raiz de su area.
//2) Para sacar el AREA del triangulo rectangulo solo necesito AxB, el 
//cuadrado de la hipotenusa me sobra, por lo que solo requiero pedirle al
//usuario 2 datos, el area del cuadrado a, y el area del cuadrado b.
//3)Entendiendo esto, paso a crear 3 variables. 
//var1 y var2 para almacenar los datos que ingresara el usuario, y
//una tercera para hacer los calculos(aunque es opcional).

//Defino variables. Manejan coma, asi que son reales.
var
ladoA, ladoB, varALT: real;

begin
//Por seguridad las seteo a 0, siempre.
ladoA:= 0;
ladoB:= 0;
varALT:= 0;

//Pido al usuario el ingreso de datos:
writeln('Buen dia Usuario');
writeln('Para poder resolver su problema, necesito que me de primero,');
writeln('El AREA del terreno cuadrado, que toca con el alto del lago.');
writeln('Llamaremos a este dato "Lado A"');
readln(ladoA);
writeln('Muchas gracias!');
writeln('Ahora, estaria necesitando el valor del AREA del terreno'); 
writeln('cuadrado, que toca el largo del lago,');
writeln('Llamaremos a este dato "Lado B"');
readln(ladoB);

//Ahora que tenemos los datos, los proceso:
//Primero saco la raiz de cada, para obtener el largo de estos cuadrados
ladoA := sqrt(ladoA);
ladoB := sqrt(ladoB);
//Con esta informacion puedo operar para sacar el area del triangulo rectangulo.

//Metodo "Variable extra":
varALT := ((ladoA * ladoB)/2);

//Metodo "RataSuciaSinRam":
//ladoA := ((ladoA * ladoB)/2);


//Ahora que tengo el resultado del area del triangulo, se lo informo al usuario:
writeln('Muchas gracias!');
writeln('Pues vera, el AREA(superficie) del lago, es:');
//depende del metodo que implementen, la variable que ira aqui, si eligen el metodo variable extra deberian modificar.
writeln(varALT);
writeln('Con esto doy finalizada mi existencia!');
writeln('Que tenga un buen dia!');

readkey;
end.
