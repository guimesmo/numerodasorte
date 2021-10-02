import random


def gerador_mega_sena():
    numeros = list(range(1, 100))
    random.shuffle(numeros)
    return numeros[:6]
