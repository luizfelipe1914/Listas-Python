#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

from math import log    # Importando o módulo de cálculo de logarítmos.
import random           # Importando o módulo random.
from datetime import datetime   # Importando o módulo datetime para obter-se o horário atual da máquina.

def main():
    random.seed(datetime.now()) # A "semente" para "geração" o numero inteiro será o horário atual da máquina.
    num = random.randint(1,10)  # Será "gerado" um inteiro entre 1 e 10. Ele será a base do logarítmo.
    try:
        number = float(input("Informe um número: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(number < 0):
        print("Número inválido.")
    else:
        print(f"O logarítmo de base {num} de {number} é: {log(num, number)}")


if(__name__ == "__main__"):
    main()
