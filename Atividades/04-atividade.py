# %% 1. Maior entre Dois Número
#Crie um programa que peça ao usuário para digitar dois números.
#O programadeve comparar os dois números e exibir uma mensagem indicando qual deles é o maior.
num1 = int(input('Digite o Primeiro número: '))
num2 = int(input('Digite o Segundo número: '))
if num1 > num2:
    print('O seu Primeiro número: (', num1, ') é maior que o segundo número escolhido: (', num2, ')')
if num2 > num1:
    print('O seu Segundo número: (', num2, ') é maior que o Primero número escolhido: (', num1, ')')
else:
    print('Os Dois números tem o mesmo valor')


# %% 2. Número positivo e negativo
#Peça um número inteiro e informe se ele é positivo ou negativo. Considere também a possibilidade de ser zero.
num3 = int(input('Digite um número: '))
if num3 >= 0:
    print('Positivo!')
else:
    print('Negativo!')


# %% 3. Idade:
#Solicite o ano de nascimento.
#Calcule a idade considerando o ano atual (use a função datetime.now() do módulo datetime).
#Exiba a idade.
from datetime import datetime
#.year pega o ano
#.monrg pega o mes
#.day pega o dia
ano_n = int(input('Informe o seu ano de nascimento: '))
dt = datetime.now().year - ano_n
print('sua idade hoje é:', dt)


# %% 4. A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo
#com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 24 anos: SÊNIOR
#Acima: MASTER
ano_nasci = int(input('Digite o ano de nascimento: '))
idade = 2026 - ano_nasci
if idade <= 9:
    print('Mirim!')
elif idade <= 14:
    print('Infantil!')
elif idade <= 19:
    print('Junior!')
elif idade <= 24:
    print('Sênior"!')
else:
    print('Master!')

# %% 5. Comparação de números:
#Peça dois números inteiros. Se forem iguais, exiba “Números iguais”; caso contrário, exiba “Números diferentes”.


# %% 6. Controle de temperatura:
#Peça a temperatura atual em graus Celsius. Se for maior ou igual a 30, exiba “Dia quente”; caso contrário, exiba “Temperatura amena”.


# %% 7. Multas de trânsito:
#Crie um programa que solicite ao usuário o limite de velocidade da via e a velocidade registrada pelo radar. Utilize if, elif e else para verificar se houve multa, classificar a infração e informar a quantidade de pontos na CNH.
#Considere as seguintes regras para uma via de 60 km/h:
#Até 60 km/h: sem multa (0 pontos).
#De 61 a 72 km/h: infração média (4 pontos).
#De 73 a 90 km/h: infração grave (5 pontos).
#Acima de 90 km/h: infração gravíssima (7 pontos).



# %% 8. Classificação de Salário:
#Baixa renda: (até R$1500)
#Média renda: (R$1500 a R$5000)
#Alta renda: (R$5000 a R10000)
#Renda muito alta:(acima de R$10000)).



# %% 9. Desafio Bónus
#Dada a atual crise hídrica do país, as pessoas começaram a construir reservatórios para armazenar água em suas propriedades. Faça um programa em Python que auxilie os utilizadores do reservatório a controlarem seu consumo. Obtenha do teclado as dimensões de um reservatório (altura, largura e comprimento, em centímetros) e o consumo médio diário dos utilizadores do reservatório (em litros/dia). Assuma que o reservatório esteja cheio, tenha formato cúbico e informe:
#(a) A capacidade total do reservatório, em litros;
#(b) A autonomia do reservatório, em dias;
#(c) A classificação do consumo, de acordo com a quantidade de dias de autonomia: Consumo elevado, se a autonomia for menor que 2 dias; Consumo moderado, se a autonomia estiver entre 2 e 7 dias; Consumo reduzido, se a autonomia for maior que 7 dias