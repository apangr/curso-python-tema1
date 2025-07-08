"""Module providing an a basic example functions"""


def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros (list): Lista de números enteros o flotantes.

    Returns:
        float: El promedio de los números.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)


print(calcular_promedio([1, 2, 3, 4, 5]))
print(calcular_promedio([]))
