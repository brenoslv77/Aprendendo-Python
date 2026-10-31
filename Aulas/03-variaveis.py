# %% 1. Variáveis
nome = 'Breno'
idade = 17
altura = 1.75
peso = 70.5

print(nome)
print(idade)
print(altura)
print(peso)


# %% 2. Interpolação de strings (f-strings)
print(f'Meu nome é: {nome}')
print(f'Minha idade é: {idade}')
print(f'Minha altura é de: {altura}')
print(f'Meu peso é: {peso}')


# %% 3. Cálculo de IMC
imc = peso / altura ** 2
print(f'IMC: {imc:.2f}')


# %% 4. Convenções de nomes (snake_case e camelCase)

# snake_case
nome_completo = 'Breno B B'

# camelCase
nomeCompleto = 'Breno B B'

sala_de_aula = 'D13'
salaDeAula = 'D13'


# %% 5. Testando erros

# True = 'Teste'

# print = 123

# print(2)


# %% 6. Entrada de dados - Nome
nome = str(input('Nome: '))
print(nome)


# %% 7. Entrada de dados - Ano de nascimento
ano_nascimento = int(input('Informe o ano de nascimento: '))
print(f'Você nasceu em: {ano_nascimento}')

idade = 2026 - ano_nascimento
print(idade)


# %% 8. Entrada de dados - Altura
altura = float(input('Digite a altura: '))
print(f'Sua altura é de {altura}m')