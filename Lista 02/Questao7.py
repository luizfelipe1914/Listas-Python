#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        number1 = int(input("Informe um número: "))
        number2 = int(input("Informe outro número: "))
    except:
        print("Apenas valores numéricos são aceitos!")
    
    if(number1 > number2):
        print(f"{number1} é maior que {number2}. A diferença entre eles é de {number1 - number2}.")
    elif(number2 > number1):
        print(f"{number2} é maior que {number1}. A diferença entre eles é de {number2 - number1}.")
    else:
        print(f"Números iguais!")

if(__name__ == "__main__"):
    main()
