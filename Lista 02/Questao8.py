#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        nota1 = float(input("1ª nota: "))
        nota2 = float(input("2ª nota: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10):
        print("Notas inválidas!")
    else:
        print(f"1ª Nota: {nota1}\n2ª Nota: {nota2}\nMédia aritmética simples: {(nota1 + nota2)/2}")
if(__name__ == "__main__"):
    main()
