
salario = float(input("Digite seu salario:"))


if salario <= 280.00:
     percentual = 20

if salario <= 700.00:
     percentual = 15

if salario <= 1500:
     percentual = 10

else:
     percentual = 5

print("Salario Original R$: ", salario)

print("Percentual:", percentual, "%")

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento


print('Aumento: R$ ',aumento)
print('Novo salário: R$ ', novo_salario)