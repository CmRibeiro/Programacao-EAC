# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:51:22 2022

@author: Lenovo
"""

if __name__ == '__main__':
    
    peso = int(input("Intruduza peso\n"))
    
    altura = float(input("Intruduza altura\n"))
    
    imc = peso / (altura ** 2)
    
    print("IMC: " + str(imc))
    
    if (imc <= 18.5):
        print("Peso abaixo do recomendado\n")
    
    elif (imc <=25):
        print("Peso normal\n")
    
    elif (imc <=30):
        print("Peso acima do recomendado\n")
    
    else:
        print("Obesidade\n")
    
    
    
    
    