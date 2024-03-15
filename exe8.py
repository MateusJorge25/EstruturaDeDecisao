import math

preco1 = float(input("Digite o primeiro preço:")) 

preco2 = float(input("Digite o segundo preço:"))

preco3 = float(input("Digite o terceiro preço:"))


preco_menor = preco1

if(preco2 < preco_menor):
    preco_menor = preco2

if(preco3 < preco_menor):
    preco_menor = preco3

print("Menor preço é R$:",preco_menor)