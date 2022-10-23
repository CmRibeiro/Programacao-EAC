# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:27:11 2022

@author: Lenovo
"""

if __name__ == '__main__':
    
    volume_compras = float(input("Introduza o volume de compras: \n "))
    
    if(volume_compras <= 5000):
        print("Cliente normal\n")
    elif (volume_compras <= 20000):
        print("Cliente Profissional\n")
    else:
        print("Cliente Empresarial\n")
        