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

n = int(input('Digite o numero de linhas (n >= 1): '))
if n<1:
    print('Erro: n deve ser um numero inteiro maior ou igual a 1.\n', end='')
else:
    row = [1]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('%d' % (row[(j - 1)]), end='')
            if j<i:
                print(' ', end='')
        print('\n', end='')
        nextRow = zeros(1,i+1)
        nextRow[0] = 1
        nextRow[(i+1 - 1)] = 1
        for j in range(2, i + 1):
            nextRow[(j - 1)] = row[(j-1 - 1)]+row[(j - 1)]
        row = nextRow