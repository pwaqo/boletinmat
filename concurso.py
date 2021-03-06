# -*- coding: utf-8 -*-
# author: Ricardo Ruiz

# Programa en Python que halla la solucion del problema
# Problema: subconjuntos de N, con elementos consecutivos que sumen 91

import sys
# import itertools


def isnatural(num):
    return isinstance(num, int) and num > 0


def solve(total):
    """N must be a natural number"""

    if not isnatural(total):
        raise ValueError("El numero tiene que ser natural")

    suplimit = total//2 + 2
    for m in range(1, suplimit):
        for n in range(m, suplimit):
            suma = (n-m+1)*(m+n) // 2
            if suma < total:
                continue
            elif suma == total:
                yield (m, n)
            break


def formatConjunto(conjunto):
    return '{'+str(conjunto[0]) + ', ..., ' + str(conjunto[-1]) + '}'


def consultarNumero():

    try:
        numero = int(input("Número a ingresar: "))
    except ValueError:
        print("Debe ser un numero natural")
        exit()
    except KeyboardInterrupt:
        print("\nPrograma terminado")
        exit()

    return numero


if __name__ == '__main__':

    try:
            numero = int(sys.argv[1])
    except:
            numero = consultarNumero()

    solucion = solve(numero)

    print("Los siguientes subconjuntos en N de numeros consecutivos suman {}"
          .format(numero))

    for conjunto in solucion:
        print("{} => {}".format(formatConjunto(conjunto), numero))
