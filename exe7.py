num1 = int(input("Digite o primeiro numero:"))

num2 = int(input("Digite o segundo numero:"))

num3 = int(input("Digite o terceiro numero:"))

maior = num1

if (num2 > maior):
    maior = num2

if (num3 > maior):
    maior = num3

print("Maior numero:", maior)


menor = num1

if(num2 < menor):
    menor = num2

if (num3 < menor):
    menor = num3

print("Menor numero:", menor)