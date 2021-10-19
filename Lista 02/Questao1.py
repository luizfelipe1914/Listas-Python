#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        number1 = int(input("INFORME UM NÚMERO: "))
        number2 = int(input("INFORME OUTRO NÚMERO: "))
    except:
        print("APENAS VALORES NUMÉRICOS DEVEM SER INFORMADOS!")
    if(number1 > number2):
        print(f"{number1} > {number2}")
    elif(number2 > number1):
        print(f"{number2} > {number1}")
    else:
        print(f"{number1} = {number2}")

if(__name__ == '__main__'):
    main()
