# %% 1. FOR

# FOR:
# range() que é função de distancias percorridas
# range(inicio,fim,salto) - trabalha com esses 3 valores, sendo o fim o unico obrigatório.
# estrutura:
# for variavel in range(inicio,fim,salto):
#     sequência lógica que vai repetir
# sequêcia que não se repete

for i in range(10):
    print(i)

for x in range(1,11):
    print(x)

for j in range(0,61,5):
    print(j)


# %% 2. Maior número

# float('inf') - valor infinito positivo
# float('-inf') - valor infinito negativo

maior = float('-inf')

for i in range(3):
    num = float(input('Digite um número: '))
    if num > maior:
        maior = num

print(f'O maior número é {maior}')
print('Fim!')


# %% 3. Menor número

menor = float('inf')

for i in range(3):
    num2 = float(input('Digite um número: '))
    if num2 < menor:
        menor = num2

print(f'O menor número é {menor}')


# %% 4. Tabuada

num3 = int(input('Digite um número: '))

for i in range(11):
    print(f'{num3} X {i} = {i*num3}')

print('Fim!')


# %% 5. Lembrando - Maior e menor número

# lembrando...
# Maior número ('-inf')
# Menor número ('inf')

pessoa_mais_velha = float('-inf')
pessoa_mais_nova = float('inf')

for i in range(1,6):
    idade = int(input(f'informe a {i} idade:'))

    if idade > pessoa_mais_velha:
        pessoa_mais_velha = idade

    if idade < pessoa_mais_nova:
        pessoa_mais_nova = idade

print(f'Maior idade digitada foi {pessoa_mais_velha} anos')
print(f'Menor idade digitada foi {pessoa_mais_nova} anos')


# %% 6. WHILE

# While
# estrutura:
# variavel = ?
# while variavel < 10:
#     sequêcia lógica a ser repetida
# while True:
#     sequêcia lógica a ser repetida

x = 0

while x < 10:
    x+=1  # soma mais 1 ao valor de X
    print(x)


# %% 7. Maior número com WHILE

maior = float('-inf')

xx = 0

while xx < 3:
    xx+= 1

    num = float(input('Informe um número: '))

    if num > maior:
        maior = num

print(f'O maior número é {maior}')
print('Fim!')


# %% 8. Contagem regressiva

x = 10

while x >= 0:
    print(x)
    x -=1

print('Fim!')


# %% 9. WHILE TRUE - Deseja sair?

while True:
    sair = input('Deseja sair? (s/n) \n')

    if sair == 's':
        break


# %% 10. WHILE TRUE - Maior número

maior_numero = float('-inf')

while True:
    num = float(input('Digite um número: "0 para sair" '))

    if num == 0:
        break

    elif num > maior_numero:
        maior_numero = num
print(f'O maior número digitado foi {maior_numero}')