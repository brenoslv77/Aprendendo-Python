nome = 'Breno'
idade = 17
altura = 1.75
peso = 70.5

print(nome)
print(idade)
print(altura)
print(peso)


print(f'Meu nome é: {nome}')
print(f'Minha idade é: {idade}')
print(f'Minha altura é de: {altura}')
print(f'Meu peso é: {peso}')


imc = peso / altura ** 2
print(f'IMC: {imc:.2f}')


#snake_case
nome_completo = 'Breno B B'

#camelCase
nomeCompleto = 'Breno B B'

sala_de_aula = 'D13'
salaDeAula = 'D13'


#testando erros
#True = 'Teste'

#testando erros
#print = 123

#testando erros
#print(2)

nome = str(input('Nome: '))
print(nome)

ano_nascimento = int(input('Informe o ano de nascimento: '))
print(f'Você nasceu em: {ano_nascimento}')
idade = 2026 - ano_nascimento
print(idade)

altura = float(input('Digite a altura: '))
print(f'Sua altura é de {altura}m')