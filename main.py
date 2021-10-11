import math
import numpy as np


def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca.
    Szczegółowy opis w zadaniu 1.

    Parameters:
    r (float): promień podstawy walca
    h (float): wysokosć walca

    Returns:
    float: pole powierzchni walca
    """
    x = float

    if r < 0 or h < 0:

        return float("NaN")

    else:
        x = 2*math.pi*r*(r+h)
        return x


def fib(n: int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego.
    Szczegółowy opis w zadaniu 3.

    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia

    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    result = []
    x = 0
    y = 1
    if isinstance(n, int) == False:
        return None

    if n <= 0:
        return None
    for i in range(n):
        z = x + y
        x, y = y, z
        result.append(x)
    return result


def matrix_calculations(a: float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej
    na podstawie parametru a.
    Szczegółowy opis w zadaniu 4.

    Parameters:
    a (float): wartość liczbowa

    Returns:
    touple: krotka zawierająca wyniki obliczeń
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mdet = np.linalg.det(M)
    if Mdet == 0:
        Minv = np.array("NAN")
    else:
        Minv = np.linalg.inv(M)
    Mt = np.transpose(M)
    return Minv, Mt, Mdet


def custom_matrix(m: int, n: int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie
    z opisem zadania 7.

    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy

    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if m<0 or n<0:
        return None
    if isinstance(m, int) ==False:
        return None
    if isinstance(n, int) == False:
        return None
    M = np.zeros([m, n])

    for i in range(m):
        for j in range(n):
            if i > j:
                M[i, j] = i
            else:
                M[i, j] = j
    return M
