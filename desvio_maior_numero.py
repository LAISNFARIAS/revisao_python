num1 = int(input("Digite o 1º valor: "))
num2 = int(input("Digite o 2º valor: "))
num3 = int(input("Digite o 3º valor: "))

if num1 > num2 and num1 > num3:
    print("O maior número é: ",num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é: ",num2)
else:
    print("O maior número é: ",num3)