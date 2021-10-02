import random


def gerador_mega_sena():
    numeros = list(range(1, 60))
    random.shuffle(numeros)
    return numeros[:6]
