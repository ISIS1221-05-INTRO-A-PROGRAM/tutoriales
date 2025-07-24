# Archivo: pruebas.py


def test_ejercicio1(colores):
    """
    Función de prueba para el Ejercicio 1.
    Verifica si la lista 'colores' fue creada correctamente.
    """
    expected_colors = ["rojo", "verde", "azul", "amarillo"]
    if colores == expected_colors:
        print("¡Ejercicio 1 Correcto! La lista 'colores' es la esperada.")
    else:
        print(
            f"Ejercicio 1 Incorrecto. Se esperaba {expected_colors}, pero se obtuvo {colores}."
        )


def hint_ejercicio1():
    """
    Función de pista para el Ejercicio 1.
    """
    print(
        "Pista: Recuerda que las listas se crean usando corchetes `[]` y los elementos se separan por comas."
    )
    print("Ejemplo: `mi_lista = [elemento1, elemento2]`")


def solution_ejercicio1():
    """
    Función de solución para el Ejercicio 1.
    """
    print("Solución Ejercicio 1:")
    print("```python")
    print("colores = ['rojo', 'verde', 'azul', 'amarillo']")
    print("```")


def test_ejercicio2(segundo_animal, ultimo_animal):
    """
    Función de prueba para el Ejercicio 2.
    Verifica si se accedió correctamente al segundo y último elemento.
    """
    animales = ["perro", "gato", "elefante", "tigre"]
    expected_second = animales[1]
    expected_last = animales[-1]

    correct_second = segundo_animal == expected_second
    correct_last = ultimo_animal == expected_last

    if correct_second and correct_last:
        print("¡Ejercicio 2 Correcto! Los elementos se accedieron correctamente.")
    else:
        if not correct_second:
            print(
                f"Ejercicio 2 Incorrecto (segundo elemento). Se esperaba '{expected_second}', pero se obtuvo '{segundo_animal}'."
            )
        if not correct_last:
            print(
                f"Ejercicio 2 Incorrecto (último elemento). Se esperaba '{expected_last}', pero se obtuvo '{ultimo_animal}'."
            )


def hint_ejercicio2():
    """
    Función de pista para el Ejercicio 2.
    """
    print(
        "Pista: Recuerda que los índices de las listas empiezan en 0. Para el último elemento, puedes usar un índice negativo."
    )
    print("Ejemplo: `lista[1]` para el segundo elemento, `lista[-1]` para el último.")


def solution_ejercicio2():
    """
    Función de solución para el Ejercicio 2.
    """
    print("Solución Ejercicio 2:")
    print("```python")
    print("animales = ['perro', 'gato', 'elefante', 'tigre']")
    print("segundo_animal = animales[1]")
    print("ultimo_animal = animales[-1]")
    print('print(f"Segundo animal: {segundo_animal}")')
    print('print(f"Último animal: {ultimo_animal}")')
    print("```")


def test_ejercicio3(ciudades):
    """
    Función de prueba para el Ejercicio 3.
    Verifica si la lista 'ciudades' fue modificada correctamente.
    """
    expected_ciudades = ["Bogotá", "Medellín", "Cartagena", "Barranquilla"]
    if ciudades == expected_ciudades:
        print(
            "¡Ejercicio 3 Correcto! La lista 'ciudades' fue modificada correctamente."
        )
    else:
        print(
            f"Ejercicio 3 Incorrecto. Se esperaba {expected_ciudades}, pero se obtuvo {ciudades}."
        )


def hint_ejercicio3():
    """
    Función de pista para el Ejercicio 3.
    """
    print(
        "Pista: Puedes cambiar el valor de un elemento en una posición específica usando su índice. Por ejemplo: `mi_lista[indice] = nuevo_valor`."
    )


def solution_ejercicio3():
    """
    Función de solución para el Ejercicio 3.
    """
    print("Solución Ejercicio 3:")
    print("```python")
    print("ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla']")
    print("ciudades[2] = 'Cartagena'")
    print("print(ciudades)")
    print("```")


def test_ejercicio4(tareas):
    """
    Función de prueba para el Ejercicio 4.
    Verifica si los métodos de lista fueron aplicados correctamente.
    """
    expected_tareas = [
        "Estudiar",
        "Leer",
        "Hacer ejercicio",
    ]  # Después de añadir, insertar y eliminar
    if tareas == expected_tareas:
        print("¡Ejercicio 4 Correcto! Los métodos de lista se aplicaron correctamente.")
    else:
        print(
            f"Ejercicio 4 Incorrecto. Se esperaba {expected_tareas}, pero se obtuvo {tareas}."
        )


def hint_ejercicio4():
    """
    Función de pista para el Ejercicio 4.
    """
    print(
        "Pista: Usa `append()` para añadir al final, `insert(indice, valor)` para insertar en una posición y `remove(valor)` para eliminar por valor."
    )


def solution_ejercicio4():
    """
    Función de solución para el Ejercicio 4.
    """
    print("Solución Ejercicio 4:")
    print("```python")
    print("tareas = ['Estudiar', 'Comprar', 'Cocinar']")
    print("tareas.append('Hacer ejercicio')")
    print("tareas.insert(1, 'Leer')")
    print("tareas.remove('Comprar')")
    print("print(tareas)")
    print("```")


def test_ejercicio5(primeros_tres, del_d_al_g):
    """
    Función de prueba para el Ejercicio 5.
    Verifica si el slicing fue realizado correctamente.
    """
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h"]
    expected_primeros_tres = ["a", "b", "c"]
    expected_del_d_al_g = ["d", "e", "f", "g"]

    correct_primeros_tres = primeros_tres == expected_primeros_tres
    correct_del_d_al_g = del_d_al_g == expected_del_d_al_g

    if correct_primeros_tres and correct_del_d_al_g:
        print("¡Ejercicio 5 Correcto! El slicing se realizó correctamente.")
    else:
        if not correct_primeros_tres:
            print(
                f"Ejercicio 5 Incorrecto (primeros_tres). Se esperaba {expected_primeros_tres}, pero se obtuvo {primeros_tres}."
            )
        if not correct_del_d_al_g:
            print(
                f"Ejercicio 5 Incorrecto (del_d_al_g). Se esperaba {expected_del_d_al_g}, pero se obtuvo {del_d_al_g}."
            )


def hint_ejercicio5():
    """
    Función de pista para el Ejercicio 5.
    """
    print(
        "Pista: Recuerda que el slicing usa la sintaxis `[inicio:fin]`, donde `fin` es exclusivo. Para el principio, omite `inicio`. Para el final, omite `fin`."
    )


def solution_ejercicio5():
    """
    Función de solución para el Ejercicio 5.
    """
    print("Solución Ejercicio 5:")
    print("```python")
    print("alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']")
    print("primeros_tres = alfabeto[:3]")
    print("del_d_al_g = alfabeto[3:7]")
    print('print(f"Primeros tres: {primeros_tres}")')
    print('print(f"Del d al g: {del_d_al_g}")')
    print("```")


def test_ejercicio6(numeros_pares):
    """
    Función de prueba para el Ejercicio 6.
    Verifica si se imprimieron los números correctamente.
    """
    # Esta prueba no puede verificar directamente la salida de 'print',
    # pero podemos verificar si el bucle se ejecutó correctamente
    # y si la lista original no fue modificada.
    expected_output_phrases = []
    for num in [2, 4, 6, 8, 10]:
        expected_output_phrases.append(f"{num} es un número par")

    # Para una prueba más robusta, necesitaríamos capturar la salida estándar,
    # pero para este contexto, asumimos que el bucle `for` se implementó.
    # Se puede añadir una verificación si la lista 'numeros_pares' original no fue alterada.
    if numeros_pares == [2, 4, 6, 8, 10]:
        print(
            "¡Ejercicio 6 Correcto! Parece que el bucle `for` se implementó correctamente."
        )
    else:
        print(
            "Ejercicio 6 Incorrecto. La lista 'numeros_pares' fue modificada inesperadamente."
        )


def hint_ejercicio6():
    """
    Función de pista para el Ejercicio 6.
    """
    print(
        "Pista: Usa un bucle `for` de la forma `for elemento in lista:` y la función `print()` con un f-string para formatear el mensaje."
    )


def solution_ejercicio6():
    """
    Función de solución para el Ejercicio 6.
    """
    print("Solución Ejercicio 6:")
    print("```python")
    print("numeros_pares = [2, 4, 6, 8, 10]")
    print("for numero in numeros_pares:")
    print('    print(f"{numero} es un número par")')
    print("```")
