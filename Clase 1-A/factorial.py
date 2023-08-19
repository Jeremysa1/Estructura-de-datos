def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


def factorial_recursivo(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero-1)


valor = 5
f = factorial(valor)
print(f"El factorial de {valor} es {f}")
f = factorial(valor)
print(f"El factorial (calculado de manera recursiva) de {valor} es {f}")