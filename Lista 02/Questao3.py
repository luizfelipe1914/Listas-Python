#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

from math import sqrt

def main():
    try:
        number = int(input("Informe um número: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(number < 0):
        print(f"{number}^2 = {number**2}.")
    else:
        print(f"sqrt({number}) = {sqrt(number)}")


if(__name__ == "__main__"):
    main()
