unit UpilaCaracteres;

interface

type
    TELemento = integer;
    TLista = ^TNodo;

    TNodo = record 
        elemento: TElemento;
        siguiente:TLista;
    end;

procedure crear(var lista: T);

procedure meter(lista: TLista; var elemento: TElemento);

procedure borrar(var lista: TLista; elemento: TElemento);

function buscar(lista: TLista; elemento: TElemento): TElemento;
    

implementation

procedure crear(var lista: T);
begin
    lista := Nil; 
end;

procedure meter(lista: TLista; var elemento: TElemento);
var
    aux: TLista;
begin
    new(aux);
    aux^.elemento := elemento;
    aux^.siguiente := lista;
    lista := aux;
end;

procedure borrar(var lista: TLista; elemento: TElemento);
begin
    
end;

begin
    
end.