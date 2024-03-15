def insertar(dni: str, datos: dict, diccionario: dict) -> None:
    if dni not in diccionario:
        diccionario[dni] = datos
        print("Registro guardado.")
    else:
        print("Este dni ya existe en la tabla.")

def borrar(dni: str, diccionario: dict) -> None:
    if dni in diccionario:
        del diccionario[dni]
        print("Registro borrado.")
    else:
        print("El DNI no existe en la tabla")

def modificar(dni: str, columna: str, dato: str, diccionario: dict) -> None:
    if dni in diccionario:
        if columna in diccionario[dni]:
            diccionario[dni][columna] = dato
            print(f"{columna} modificado correctamente.")
        else:
            print("La columna no existe.")
    else:
        print("El DNI no existe en la tabla.")

if __name__ == "__main__":
    personas = {}

    insertar(
        "41789518", 
        {
            "nombre": "Giuliano Igancio", 
            "apellido": "Poeta", 
            "direccion": "Alem 4172"
        },
        personas
    )
    insertar(
        "41789823", 
        {
            "nombre": "Rocio", 
            "apellido": "Jofre Olivero", 
            "direccion": "Maipu 1305"
        },
        personas
    )
    insertar(
        "12345678", 
        {
            "nombre": "Cosme", 
            "apellido": "Fulanito", 
            "direccion": "Calle Falsa 123"
        },
        personas
    )

    modificar("41789518", "direccion", "Maipu 1305", personas)

    # Borrar datos
    borrar("12345678", personas)

    print(personas)
