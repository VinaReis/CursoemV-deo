#preço produto: coca-2,29 farinha-3 leite-3,50 ovo-10,40 fermento-3,25 magarina-5,90
print('opções:')
print('1-[Coca-Cola]')
print('2-[Farinha-de-Trigo]')
print('3-[Leite]')
print('4-[Ovo]')
print('5-[Fermento]')
print('6-[Margarina]')
escolha = int(input('Qual produto você deseja?: '))
cocaína = 2.29
muamba = 3.0
leitada = 3.50
ovão = 10.40
fumaça = 3.25
pressãoalta = 5.90

if escolha == 1:
    print(f'O valor da Coca-Cola é: R${cocaína}')
    printfloat(f'\nO valor da Coca-Cola com o desconto é: R${cocaína*(5/100)}.')

elif escolha == 2:
    print(f'O valor da Farinha-de-Trigo é: R${muamba}\nO valor da Farinha-de-Trigo com desconto é: R${muamba*(5/100)}.')

elif escolha == 3:
    print(f'O valor do Leite é: R${leitada}\nO valor do Leite com desconto é: R${leitada*(5/100)}.')

elif escolha == 4:
    print(f'O valor do Ovo é: R${ovão}\nO valor do Ovo com desconto é: R${ovão*(5/100)}.')

elif escolha == 5:
    print(f'O valor do Fermento é: R${fumaça}\nO valor do Fermento com desconto é: R${fumaça*(5/100)}.')

elif escolha == 6:
    print(f'O valor da Margarina é: R${pressãoalta}\nO valor da Margarina com desconto é: R${pressãoalta(5/100)}.')