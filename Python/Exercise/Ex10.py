altura = float(input('Qual a altura da parede?: '))
largura = float(input('Qual a largura da parede?: '))
litros = float(input('Quantos litros tem cada balde?: '))
resultado1 = altura * largura / 2
resultado2 = int(resultado1 // litros)
print(f'A quantidade de litros é: {resultado1}\nA qunatidade de baldes é: {resultado2}')