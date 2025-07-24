import datetime
import math

print("Util v2 loaded")


def test_q1_1(radio):
    if radio == None:
        print("Error: La variable radio no fué definida. Revisa si está bien escrita")
    elif not (type(radio) is float):
        print("Error: La variable radio no coincide con el tipo esperado")
    else:
        print("Correcto. El radio es:", radio)


def test_q1_2(radio, area):
    if radio == None or area == None:
        print(
            "Error: Alguna de las variables no fué definida. Revisa si están bien escritas"
        )
    elif (type(radio) is not float) or (type(area) is not float):
        print("Error: Alguna de las variables no coindice con el tipo esperado")
    else:
        pi = 3.14159265359
        ac = pi * (radio**2)
        if ac != area:
            print("Error: El valor de la variable area no coincide con el esperado")
        else:
            print("Correcto. El área fué bien calculada", area)


def test_q1_3(area, area_redondeada):
    if area_redondeada == None or area == None:
        print(
            "Error: Alguna de las variables no fué definida. Revisa si están bien escritas"
        )
    elif (type(area_redondeada) is not float) or (type(area) is not float):
        print("Error: Alguna de las variables no coindice con el tipo esperado")
    else:
        acr = round(area, 2)
        if acr != area_redondeada:
            print("Error: El valor de la variable area no coincide con el esperado")
        else:
            print("Correcto. El redondeo fué bien calculado", area_redondeada)


def test_q2_1(lado1, lado2):
    if lado1 == None or lado2 == None:
        print(
            "Error: Alguna de las variables no fué definida. Revisa si están bien escritas"
        )
    elif (type(lado1) is not float) or (type(lado2) is not float):
        print("Error: Alguna de las variables no coindice con el tipo esperado")
    else:
        print("Correcto. Los lados fueron bien recibidos")


def test_q2_2(lado1, lado2, area):
    if area == None:
        print(
            "Error: Alguna de las variables no fué definida. Revisa si están bien escritas"
        )
    elif type(area) is not float:
        print("Error: Alguna de las variables no coindice con el tipo esperado")
    else:
        acr = lado1 * lado2
        if acr != area:
            print("Error: El valor de la variable area no coincide con el esperado")
        else:
            print("Correcto. El área fué bien calculada", area)
