program ejercicio2ResoluciondeProblemas;
uses crt;

(*
Ejercicio 2: 
Una agencia de autos paga a sus
vendedores $2500 de sueldo básico, más una
comisión de 500 por cada auto vendido, mas
un 5% del valor del vehículo. Que datos debo
conocer para calcular el sueldo final

Para resolver mi consigna primero necesito saber que:

1) Cuantos autos vendio, y el valor de cada carro.
porque queremos sacar un 5% del valor de ese carro en especifico.

2) vamos a necesitar 5 variables:
* variableDeCuantosAutosVendidos - vAv: Imperativo saber cuantos autos vendio.
* valorTempdCadaAutoVendido: para poder calcular el 5% de cada valor de auto ingresado.
* resultado: sumarle 500 a cada venta + su 5% y apilar.
* SueldoBase: una variable que la da la empresa que es el sueldo base.
* N: que vamos a usar para el for.

3) Vamos a preguntar al usuario cuantos autos vendi en total, y en orden
preguntarle cuanto salio cada uno de esos autos.

4) Vamos a hacer un for N:=1 to VaV

*)
var
valorTempdCadaAutoVendido, resultado, sueldoBase: Real;
vAv, n: Integer;

begin
n							:= 0;
vAv							:= 0;
valorTempdCadaAutoVendido	:= 0;
resultado					:= 0;
sueldoBase 					:= 2500;


writeln('Buen dia Usuario');
writeln('para que usted pueda cobrar, necesitamos que nos ingrese,');
writeln('cuantos autos vendio usted este mes.');
write  ('Autos vendidos: ');
read(vAv);

writeln('Excelente, ahora voy a necesitar que en orden, ');
writeln('me valla indicando de que valor fueron los autos vendidos:');

//Proceso
 for n:=1 to vAv do
	begin
	if (vAv <> 0) then 
		begin
		writeln('Indique el valor del auto vendido nro ',n);
		readln(valorTempdCadaAutoVendido);
		//Sacar el 5% de ese valor.
		resultado:= (resultado + (valorTempdCadaAutoVendido * 0.05) + 500);		
		end;
	end;
	
	resultado := resultado + sueldoBase;
	
	writeln('Muchas gracias por la informacion.');
	writeln('Su sueldo de este mes deberia ser de: ', resultado:5:2,'.');


readkey;
end.
