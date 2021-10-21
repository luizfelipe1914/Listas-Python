#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        sexo = input("Qual o sexo(biológico), [M]asculino ou [F]eminino? ")
        altura = float(input("Qual a altura? "))
    except:
        print("Parâmetros inválidos!")

    if(sexo.upper() == "M"):
        print(f"Seu peso ideal é: {72.7*altura -58} kg")
    elif(sexo.upper() == "F"):
        print(f"Seu peso ideal é: {62.1*altura -44.7} kg")
    else:
        print("Entrada inválida!")

if(__name__ == "__main__"):
    main()
