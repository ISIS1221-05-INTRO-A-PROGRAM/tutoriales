# Script de pruebas para el tutorial de diccionarios en Python


def test_ejercicio1(mi_libro):
    "Prueba el resultado del ejercicio 1."
    resultado_esperado = {
        "título": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
    }
    assert (
        mi_libro == resultado_esperado
    ), f"Se esperaba {resultado_esperado}, pero se obtuvo {mi_libro}."
    print("Ejercicio 1 correcto.")


def hint_ejercicio1():
    "Proporciona una pista para el ejercicio 1."
    print("Recuerda usar la sintaxis {'clave': 'valor'} para crear un diccionario.")


def solution_ejercicio1():
    "Muestra la solución para el ejercicio 1."
    print(
        "La solución es: mi_libro = {'título': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967}"
    )


def test_ejercicio2(autor_libro):
    "Prueba el resultado del ejercicio 2."
    resultado_esperado = "Gabriel García Márquez"
    assert (
        autor_libro == resultado_esperado
    ), f"Se esperaba {resultado_esperado}, pero se obtuvo {autor_libro}."
    print("Ejercicio 2 correcto.")


def hint_ejercicio2():
    "Proporciona una pista para el ejercicio 2."
    print(
        "Usa el nombre del diccionario seguido de la clave entre corchetes para acceder al valor."
    )


def solution_ejercicio2():
    "Muestra la solución para el ejercicio 2."
    print("La solución es: autor_libro = mi_libro['autor']")


def test_ejercicio3(mi_libro):
    "Prueba el resultado del ejercicio 3."
    resultado_esperado = {
        "título": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "género": "Realismo mágico",
    }
    assert (
        mi_libro == resultado_esperado
    ), f"Se esperaba {resultado_esperado}, pero se obtuvo {mi_libro}."
    print("Ejercicio 3 correcto.")


def hint_ejercicio3():
    "Proporciona una pista para el ejercicio 3."
    print(
        "Puedes añadir un nuevo par clave-valor a un diccionario usando la sintaxis diccionario['nueva_clave'] = nuevo_valor."
    )


def solution_ejercicio3():
    "Muestra la solución para el ejercicio 3."
    print("La solución es: mi_libro['género'] = 'Realismo mágico'")


def test_ejercicio4(claves_libro):
    "Prueba el resultado del ejercicio 4."
    resultado_esperado = ["título", "autor", "año", "género"]
    assert (
        claves_libro == resultado_esperado
    ), f"Se esperaba {resultado_esperado}, pero se obtuvo {claves_libro}."
    print("Ejercicio 4 correcto.")


def hint_ejercicio4():
    "Proporciona una pista para el ejercicio 4."
    print("Usa el método .keys() para obtener las claves de un diccionario.")


def solution_ejercicio4():
    "Muestra la solución para el ejercicio 4."
    print("La solución es: claves_libro = list(mi_libro.keys())")
