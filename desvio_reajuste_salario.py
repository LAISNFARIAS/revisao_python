salario = float(input("Digite o valor do seu salário: "))
reajuste = float
sal=float

if salario <= 280.00:
    reajuste = salario*(20/100)
    sal = salario + reajuste
    print("O salário antes do reajuste era: R${:_.2f}".format(salario))
    print("O percentual de reajuste é 20%")
    print("O valor do reajuste é: R${:_.2f}".format(reajuste))
    print("Seu novo salário é: R${:_.2f}".format(sal))
elif salario > 280.00 and salario <=700.00:
     reajuste = salario*(15/100)
     sal= salario + reajuste
     print("O salário antes do reajuste era: R${:_.2f}".format(salario))
     print("O percentual de reajuste é de 15%")
     print("O valor do reajuste é: R${:_.2f}".format(reajuste))
     print("Seu novo salário é: R${:_.2f}".format(sal))
elif salario > 700.00 and salario <= 1500.00:
     reajuste = salario*(10/100)
     sal= salario + reajuste
     print("O salário antes do reajuste era: R${:_.2f}".format(salario))
     print("O percentual de reajuste é de 10%")
     print("O valor do reajuste é: R${:_.2f}".format(reajuste))
     print("Seu novo salário é: R${:_.2f}".format(sal))
else:
     reajuste = salario*(5/100)
     sal= salario + reajuste
     print("O salário antes do reajuste era: R${:_.2f}".format(salario))
     print("O percentual de reajuste é de 5%")
     print("O valor do reajuste é: R${:_.2f}".format(reajuste))
     print("Seu novo salário é: R${:_.2f}".format(sal))