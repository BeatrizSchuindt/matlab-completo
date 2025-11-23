# -*- coding: utf-8 -*-
# Código Python gerado automaticamente a partir de Matlab-like

def zeros(m, n=None):
    """Aproximação simples de zeros do Matlab."""
    if n is None:
        return [0] * m
    if m == 1:
        return [0] * n
    if n == 1:
        return [0] * m
    return [[0 for _ in range(n)] for _ in range(m)]

a = int(input('Informe o lado a: '))
b = int(input('Informe o lado b: '))
c = int(input('Informe o lado c: '))
if (a<=0 or b<=0 or c<=0):
    raise Exception('Medidas inválidas')
if (a+b<=c or a+c<=b or b+c<=a):
    raise Exception('Medidas inválidas')
if (a==b and b==c):
    print('Triângulo equilátero válido\n', end='')
elif (a==b or a==c or b==c):
    print('Triângulo isósceles válido\n', end='')
else:
    print('Triângulo escaleno válido\n', end='')