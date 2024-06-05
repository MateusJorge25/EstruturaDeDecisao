
lado1 = int(input("Digite o primeiro lado: "))

lado2 = int(input("Digite o segundo lado: "))

lado3 = int(input("Digite o terceiro lado: "))


if lado1 == lado2 == lado3:
    print("Triangulo Equilatero")

elif (lado1 == lado2) !=  (lado2 == lado3):
    print("Triangulo Isosceles")

elif lado1 != lado2 != lado3:
    print("Triangulo Escaleno")