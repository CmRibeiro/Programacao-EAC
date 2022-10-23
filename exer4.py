# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:32:09 2022

@author: Lenovo
"""

if __name__ == '__main__':
    
    preco_compra = float(input("Introduza o preco de compra:\n"))
    codigo_produto = int(input("Intrpduza o codigo do produto:\n"))
    familia_produto = str()
    
    if(codigo_produto == 1):
        familia_produto = "Cobras"
        pvp_siva = preco_compra * 1.03
    elif (codigo_produto == 4):
        pvp_siva = preco_compra * 1.04
        familia_produto = "Ratos"
    elif(codigo_produto == 9):
        pvp_siva = preco_compra * 1.025
        familia_produto = "Caes"
        
    print("Familia do artigo: " + familia_produto)
    print("PVP s/iva: " + str(pvp_siva))
    print("PVP c/iva: " + str(pvp_siva * 1.23))
    