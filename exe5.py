
num1 = int(input("Digite a primeira nota:"))

num2 = int(input("Digite a segunda nota:"))

media = (num1 + num2)/2

print("Sua media foi:",media)

if media >= 7:
    print("Aprovado")

if media < 7:
    print("Reprovado")

elif media > 7 <= 10:
    print("Aprovado com Distinção") 