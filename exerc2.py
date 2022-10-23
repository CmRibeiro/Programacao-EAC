# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:09:22 2022

@author: Lenovo
"""

if __name__ == '__main__':
    
    salario = float(input("Intruduza salario do trabalhador: \n"))
    vendas = float(input("Intruduza vendas do trabalhador: \n"))
    
    if (salario < vendas ):
        comissao = 0.15 * vendas
        print("Salario final: " + str(salario + comissao))
    else:
        print("Salario final: " + str(salario))
        
    if (vendas <= 19999):
        print("Classificacao do vendedor: D \nPremio: 0€")
    elif (vendas <= 29999):
        print("Classificacao do vendedor: C \nPremio: 150€")
    elif (vendas <= 60000):
        print("Classificacao do vendedor: B \nPremio: 400€")
    else:
        print("Classificacao do vendedor: A \nPremio: " + str(vendas * 0.015) + "€")
        