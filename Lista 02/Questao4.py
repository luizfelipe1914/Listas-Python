#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        number = int(input("Informe um número: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(number < 0):
        print(f"{number} é negativo.")
    else:
        print(f"{number}^2 = {number**2}")
        print(f"{number}^(1/2) = {number**(1/2)}")
if(__name__ == "__main__"):
    main()
