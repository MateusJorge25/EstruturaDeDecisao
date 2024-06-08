
nota1 = int(input("Digite a primeira nota: "))

nota2 = int(input("Digite a segunda nota: "))

nota3 = int(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3)/3

if (media >= 7) == (media < 10):
    print("Aprovado com: ", media)

elif media < 7:
    print("Reprovado com: ", media)

else:
    print("Aprovado com Distinção com media maior que 10")

