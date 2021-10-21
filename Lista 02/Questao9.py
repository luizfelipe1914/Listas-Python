#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    try:
        parcela = float(input("Valor da prestação: "))
        salario = float(input("Salário: "))
    except:
        print("Apenas valores numéricos devem ser informados!")
    if(parcela <= (salario*0.2)):
        print("Empréstimo concedido!")
    else:
        print("Empréstimo não concedido!G")
if(__name__ == "__main__"):
    main()
