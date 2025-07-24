# Ejercicio 1
def ejercicio1_prueba(locals_dict) -> bool:
    # Función para probar la respuesta del primer ejercicio

    import datetime

    if "anio_nacimiento" not in locals_dict:
        print("Error: La variable 'anio_nacimiento' no ha sido creada.")
        return False
    if "nombre" not in locals_dict:
        print("Error: La variable 'nombre' no ha sido creada.")
        return False

    anio_nacimiento = locals_dict.get("anio_nacimiento")
    nombre = locals_dict.get("nombre")

    thisyear = datetime.date.today().year
    if anio_nacimiento is None:
        print("Error: La variable anio_nacimiento no fué definida.")
        return False
    if type(anio_nacimiento) is not int:
        print("Error: La variable anio_nacimiento no coincide con el tipo esperado.")
        return False
    if anio_nacimiento <= 0:
        print("Error: El valor de la variable anio_nacimiento debe ser mayor a cero")
        return False
    if anio_nacimiento > thisyear:
        print(
            "Error: El valor de la variable anio_nacimiento debe ser menor o igual al año de la fecha actual"
        )
        return False

    if nombre is None:
        print("Error: La variable nombre no fue definida. Revisa si está bien escrita")
        return False
    if not isinstance(nombre, str):
        print("Error: La variable nombre no coincide con el tipo esperado")
        return False
    if len(nombre) < 1:
        print("Error: El nombre debe tener al menos un caracter")
        return False

    print("Correcto", nombre, ". Tu edad es:", thisyear - anio_nacimiento, " años")
    return True


def ejercicio1_pista() -> None:
    # Función para mostrar la pista del primer ejercicio
    import random

    pistas = [
        "Las variables en Python se definen con el signo igual (=).",
        "Las variables de texto se definen entre comillas simples o dobles.",
        "Las variables numéricas se definen sin comillas.",
        "Los nombres de las variables no deben contener espacios ni caracteres especiales, y deben comenzar con una letra o un guión bajo.",
        "Revisa que los nombres de las variables sean correctos y que estén bien escritos.",
    ]

    print(random.choice(pistas))

    return None


def ejercicio1_respuesta() -> None:
    # Función para mostrar la respuesta del primer ejercicio
    print("anio_nacimiento = 2000\n" "nombre = 'Tu Nombre'\n")
    return None


# Ejercicio 2
def ejercicio2_prueba(locals_dict) -> bool:
    # Función para probar la respuesta del segundo ejercicio

    if "galones" not in locals_dict:
        print("Error: La variable 'galones' no ha sido creada.")
        return False
    if "litros" not in locals_dict:
        print("Error: La variable 'litros' no ha sido creada.")
        return False

    galones = locals_dict.get("galones")
    litros = locals_dict.get("litros")

    if galones is None:
        print("Error: La variable galones no fue definida. Revisa si está bien escrita")
        return False
    if galones < 0:
        print("Error: La variable galones debe tener un valor igual o superior a cero")
        return False
    if litros is None:
        print("Error: La variable litros no fue definida. Revisa si está bien escrita")
        return False
    if type(litros) is not float:
        print("Error: La variable litros no coincide con el tipo esperado")
        return False
    if round(litros, 2) != round(galones * 3.78541, 2):
        print("Error: El valor de la variable litros no coincide con el esperado")
        return False

    print("Correcto, la capacidad es de:", litros, "litros")
    return True


def ejercicio2_pista() -> None:
    # Función para mostrar la pista del segundo ejercicio
    import random

    pistas = [
        "Para convertir galones a litros, multiplica el número de galones por 3.78541.",
        "Asegúrate de que la variable 'galones' sea un número positivo.",
        "La variable 'litros' debe ser del tipo float.",
        "Revisa que las variables estén bien escritas y que no haya errores tipográficos.",
    ]

    print(random.choice(pistas))


def ejercicio2_respuesta() -> None:
    # Función para mostrar la respuesta del segundo ejercicio
    print("galones = 10\n" "litros = galones * 3.78541\n")


# Ejercicio 3
def ejercicio3_prueba(locals_dict) -> bool:
    # Código para probar la respuesta
    if "monto" not in locals_dict:
        print("Error: La variable 'monto' no ha sido creada.")
        return False
    if "interes" not in locals_dict:
        print("Error: La variable 'interes' no ha sido creada.")
        return False
    if "cuotas" not in locals_dict:
        print("Error: La variable 'cuotas' no ha sido creada.")
        return False
    if "primera_cuota" not in locals_dict:
        print("Error: La variable 'primera_cuota' no ha sido creada.")
        return False
    monto = locals_dict.get("monto")
    interes = locals_dict.get("interes")
    cuotas = locals_dict.get("cuotas")
    primera_cuota = locals_dict.get("primera_cuota")
    if monto is None:
        print("Error: La variable monto no tiene valor definido.")
        return False
    if type(monto) is not float:
        print("Error: La variable monto no coincide con el tipo esperado.")
        return False
    if monto <= 0:
        print("Error: El valor de la variable monto debe ser mayor a cero.")
        return False
    if interes is None:
        print("Error: La variable interes no tiene valor definido.")
        return False
    if type(interes) is not float:
        print("Error: La variable interes no coincide con el tipo esperado.")
        return False
    if interes < 0:
        print("Error: El valor de la variable interes debe ser mayor o igual a cero.")
        return False
    if cuotas is None:
        print("Error: La variable cuotas no tiene valor definido.")
        return False
    if type(cuotas) is not int:
        print("Error: La variable cuotas no coincide con el tipo esperado.")
        return False
    if cuotas <= 0:
        print("Error: El valor de la variable cuotas debe ser mayor a cero.")
        return False
    if primera_cuota is None:
        print("Error: La variable cuota no tiene valor definido.")
        return False
    if type(primera_cuota) is not float:
        print("Error: La variable cuota no coincide con el tipo esperado.")
        return False
    if round(primera_cuota, 2) != round(
        monto
        * ((interes * ((1 + interes) ** cuotas)) / (((1 + interes) ** cuotas) - 1)),
        2,
    ):
        print("Error: El valor de la variable cuota no coincide con el esperado")
        return False
    print("Correcto, la cuota es de:", primera_cuota)
    return True


def ejercicio3_pista() -> None:
    # Función para mostrar la pista del tercer ejercicio
    import random

    pistas = [
        "Para calcular la cuota de un préstamo, utiliza la fórmula: cuota = monto * ((interes * ((1 + interes) ** cuotas)) / (((1 + interes) ** cuotas) - 1)).",
        "Asegúrate de que las variables 'monto', 'interes', 'cuotas' y 'primera_cuota' estén bien definidas.",
        "Revisa que las variables tengan los tipos de datos correctos: monto y primera_cuota como float, interes como float, y cuotas como int.",
        "Verifica que el interés sea un número positivo o cero.",
        "Revisa que estés usando adecuadamente los paréntesis en la fórmula.",
        "Intenta imprimir los valores de las variables antes de calcular la cuota para verificar que estén correctos.",
        "Puedes hacer los cálculos parciales en variables intermedias para facilitar la comprensión y encontrar errores fácilmente.",
    ]

    print(random.choice(pistas))


def ejercicio3_respuesta() -> None:
    # Función para mostrar la respuesta del tercer ejercicio
    print(
        "monto = 80000000.0\n"
        "interes = 0.005\n"
        "cuotas = 120\n"
        "primera_cuota = monto * ((interes * ((1 + interes) ** cuotas)) / (((1 + interes) ** cuotas) - 1))\n"
    )


# Ejercicio 4
def ejercicio4_prueba(locals_dict) -> bool:
    # Código para probar la respuesta
    if "edad" not in locals_dict:
        print("Error: La variable 'edad' no ha sido creada.")
        return False
    if "clasificacion" not in locals_dict:
        print("Error: La variable 'clasificacion' no ha sido creada.")
        return False
    if "adulto" not in locals_dict:
        print("Error: La variable 'adultos' no ha sido creada.")
        return False
    if "autorizacion" not in locals_dict:
        print("Error: La variable 'autorizacion' no ha sido creada.")
        return False

    edad = locals_dict.get("edad")
    clasificacion = locals_dict.get("clasificacion")
    adulto = locals_dict.get("adulto")
    autorizacion = locals_dict.get("autorizacion")

    if edad is None:
        print("Error: La variable edad no tiene valor definido.")
        return False
    if type(edad) is not int:
        print("Error: La variable edad no coincide con el tipo esperado.")
        return False
    if edad < 0:
        print("Error: El valor de la variable edad debe ser mayor o igual a cero.")
        return False
    if clasificacion is None:
        print("Error: La variable clasificacion no tiene valor definido.")
        return False
    if clasificacion not in ["A", "B", "C"]:
        print("Error: La variable clasificacion debe ser 'A', 'B' o 'C'.")
        return False

    if adulto is None:
        print("Error: La variable adulto no tiene valor definido.")
        return False
    if type(adulto) is not bool:
        print("Error: La variable adulto no coincide con el tipo esperado.")
        return False
    if autorizacion is None:
        print("Error: La variable autorizacion no tiene valor definido.")
        return False
    if type(autorizacion) is not bool:
        print("Error: La variable autorizacion no coincide con el tipo esperado.")
        return False
    autorizacion_correcta = (
        (edad >= 18)
        or (clasificacion == "A")
        or (clasificacion == "B" and (edad >= 13 and edad < 18 and adulto == True))
    )

    if autorizacion != autorizacion_correcta:
        print("Error: El valor de la variable autorizacion no coincide con el esperado")
        return False
    print("Correcto, la autorización tiene valor:", autorizacion)
    return True


def ejercicio4_pista() -> None:
    # Función para mostrar la pista del cuarto ejercicio
    import random

    pistas = [
        "Revisa las reglas de clasificación de películas y asegúrate de que las condiciones estén bien definidas.",
        "Asegúrate de que la variable 'edad' sea un número entero positivo.",
        "La variable 'clasificacion' debe ser una cadena de texto que contenga 'A', 'B' o 'C'.",
        "La variable 'adulto' debe ser un valor booleano (True o False).",
        "Verifica que las condiciones lógicas estén correctamente formuladas.",
    ]

    print(random.choice(pistas))


def ejercicio4_respuesta() -> None:
    # Función para mostrar la respuesta del cuarto ejercicio
    print(
        "clasificacion = 'C'\n"
        "edad = 17\n"
        "adulto = True\n"
        "autorizacion = (edad >= 18) or (clasificacion == 'A') or (clasificacion == 'B' and (edad >= 13 and edad < 18) and adulto == True)\n"
    )
