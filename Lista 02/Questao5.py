#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        number = int(input("Informe um número: "))
    except:
        print("Apenas valores numéricos são aceitos!")
    if(number % 2 == 0):
        print(f"{number} é par.")
    else:
        print(f"{number} é ímpar.")


if(__name__ == "__main__"):
    main()
