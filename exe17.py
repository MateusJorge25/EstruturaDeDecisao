
ano = int(input("Digite um ano: "))



if (ano % 4 == 0 and ano % 100 != 0):
    print("Ele é um ano bissexto")

else:
    print("Ano normal com 365 dias")


'''
 O operador logico % retorna o resto da divisão, então se o ano for divisivel por 4 e seu resto for igual a 0 então ele é um ano bissexto

 Agora se o resto for diferente de 0 ele não é um ano bissexto

 Se o ano for divisivel por 100 ele não é um ano bissexto
'''

