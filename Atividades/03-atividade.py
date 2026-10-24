#área do circulo
raio = float(input('Digite o valor do Raio '))
area = 3.14 * raio ** 2
print(f'A área do circulo é {area:.1f}')


#temperatura
celsius = int(input('Digite a temperatura: '))
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura em fahrenheit é de: {fahrenheit}°F')


#diferentes nomes: primeiro e o ultimo nome
nome1 = str(input('Digite o seu Primeiro nome: '))
nome2 = str(input('Digite o seu Sobrenome: '))
print(f'Seu Nome completo é: {nome1} {nome2}')


#três notas + nomes
nome3 = str(input('Digite o seu Primeiro nome: '))
nota1 = int(input('Sua Primeira nota: '))
nota2 = int(input('Sua Segunda nota: '))
nota3 = int(input('Sua Terceira nota: '))
nota4 = nota1 + nota2 + nota3
print(f'Para nota final do aluno {nome3} ficou em: {nota4 / 3:.0f}')


#calculadora de soma
numero1 = float(input('Seu primeiro número: '))
numero2 = float(input('Seu Segundo número: '))
soma = numero1 + numero2
print(f'soma dos 2 número: {soma}')


#dobro de um número
numero3 = float(input('Digite um número para descobrir o dobro dele: '))
dobro = numero3 * 2
print(f'O dobro do seu número escolhido ({numero3}) é: {dobro}')


#calculo do salario
salario = float(input('Digite o quanto você recebe: '))
mes = float(input('Digite quanto(s) mes(es) você trabalhou '))
soma1 = salario * mes
print(f'Você recebeu no total dos meses trabalhado o valor de: {soma1}')


#calculadora de multiplicação
numero4 = float(input('Digite um número: '))
numero5 = float(input('Digite um número: '))
soma2 = numero4 * numero4
print(f'Resultado Multiplicando os 2 número: {soma2}')