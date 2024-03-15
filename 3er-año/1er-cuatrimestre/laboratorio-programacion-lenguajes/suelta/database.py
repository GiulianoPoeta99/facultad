def insertar(dni: str, datos: dict, diccionario: dict) -> None:
    """
    Inserta un nuevo registro en el diccionario 'diccionario' utilizando el DNI como clave.

    Parámetros:
    - dni (str): El número de DNI de la persona a insertar.
    - datos (dict): Un diccionario que contiene los datos de la persona a insertar.
    - diccionario (dict): El diccionario donde se almacenarán los datos.

    Retorna:
    - None. Modifica el diccionario 'diccionario' directamente.

    Ejemplo:
    insertar("41789518", {"nombre": "Giuliano Ignacio", "apellido": "Poeta", "direccion": "Alem 4172"}, personas)
    """

    if dni not in diccionario:
        diccionario[dni] = datos
        print("Registro guardado.")
    else:
        print("Este dni ya existe en la tabla.")

def borrar(dni: str, diccionario: dict) -> None:
    """
    Borra un registro del diccionario 'diccionario' utilizando el DNI como clave.

    Parámetros:
    - dni (str): El número de DNI de la persona a borrar.
    - diccionario (dict): El diccionario del cual se borrará el registro.

    Retorna:
    - None. Modifica el diccionario 'diccionario' directamente.

    Ejemplo:
    borrar("12345678", personas)
    """

    if dni in diccionario:
        del diccionario[dni]
        print("Registro borrado.")
    else:
        print("El DNI no existe en la tabla")

def modificar(dni: str, columna: str, dato: str, diccionario: dict) -> None:
    """
    Modifica un dato específico de un registro en el diccionario 'diccionario'.

    Parámetros:
    - dni (str): El número de DNI de la persona cuyos datos serán modificados.
    - columna (str): El nombre de la columna que se modificará.
    - dato (str): El nuevo valor que se asignará a la columna especificada.
    - diccionario (dict): El diccionario donde se encuentran los datos.

    Retorna:
    - None. Modifica el diccionario 'diccionario' directamente.

    Ejemplo:
    modificar("41789518", "direccion", "Maipu 1305", personas)
    """
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

    print(insertar.__doc__)
