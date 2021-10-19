#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        number = int(input("Informe um número inteiro: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(number < 0):
        print("No conjunto dos reais, o cálculo de raízes de índice par só é possível com números positivos.")
    else:
        print("A raíz quadrada de %d é %d." %(number, int(number**(1/2))))
if(__name__ == "__main__"):
    main()
