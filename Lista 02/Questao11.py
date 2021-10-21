#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        number = int(input("Informe um número: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(number < 0):
        print("Apenas valores positivos devem ser informados!")
    else:
        soma = 0
        aux = number
        while(aux != 0):
            soma = soma + (aux % 10)
            aux = aux // 10
        print(f"A soma dos algarismo de {number} é {soma}.")

if(__name__ == "__main__"):
    main()
