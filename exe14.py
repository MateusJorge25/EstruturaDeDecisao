
note1 = int(input("Digite a primeira nota: "))

note2 = int(input("Digite a segunda nota: "))

media = (note1 + note2)/2

print(media)

if (media > 9.0) and (media <= 10.0):
    print("A")

elif (media > 7.5) and (media <= 9.0):
    print("B")

elif (media > 6.0) and (media <= 7.5):
    print("C")

elif (media > 4.0) and (media <= 6.0):
    print("D")

elif (media > 4.0) and (media <= 0):
    print("E")