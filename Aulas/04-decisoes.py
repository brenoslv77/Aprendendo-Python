# %% 1. Condicional IF
media = 7

if media > 6:
    print('Aprovado')

print('Boas Ferias!')


# %% 2. Condicional IF e ELSE
media1 = 8

if media1 > 7:
    print('Aprovado')
else:
    print('Reprovado')

print('Boas Férias!')


# %% 3. Verificando maioridade
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = 2026 - ano_nasc

if idade > 18:
    print('Maior de idade')
else:
    print('Menor de idade')


# %% 4. Verificando número PAR ou ÍMPAR
num = int(input('Digite um número: '))
resto = num % 2

if resto == 0:
    print('Par!')
else:
    print('Ímpar!')


# %% 5. Condicional ELIF
media1 = float(input('Informe a média: '))

if media1 > 6:
    print('Aprovado!')
elif media1 < 6:
    print('Reprovado!')
else:
    print('Recuperação')


# %% 6. Classificação de IMC
altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso normal!')
elif imc < 30:
    print('Excesso de peso!')
elif imc < 35:
    print('Obesidade 1!')
elif imc < 40:
    print('Obesidade 2!')
else:
    print('Obesidade 3!')

print(f'IMC: {imc:.2f}')


# %% 7. Operadores lógicos - AND
usr = input('Me informe o Usuario: ')
snh = input('Informe a Senha: ')

if usr == 'senai' and snh == '123':
    print('logado!')
else:
    print('Usuario ou senha incorreta')


# %% 8. Operadores lógicos - OR
valor_compra = float(input('Informe o valor da compra: '))
cupom = input('Possui cupom? (s/n) \n')

if cupom == 's' or valor_compra > 200:
    print(f'total a pagar: R${valor_compra * 0.90}')
else:
    print(f'total a pagar: R${valor_compra}')


# %% 9. Importando biblioteca RANDOM
from random import randint

num_pc = randint(0, 10)

usr = int(input('Informe um valor de 0 a 10: '))

if usr == num_pc:
    print('Você acertou')
else:
    print('Errou!')

print('O número era', num_pc)