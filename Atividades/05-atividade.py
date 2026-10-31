# %% 1. Jogo de Adivinhação:
#Crie um programa em Python que sorteie um número aleatório entre 1 e 10 utilizando a biblioteca random.
#O usuário deverá tentar adivinhar o número sorteado, tendo no máximo 5 tentativas.
#   O programa deve:
#Utilizar random para sortear um número entre 0 e 10.
#Utilizar um laço for para controlar as 5 tentativas.
#A cada tentativa, solicitar que o usuário digite um número.
#Se o usuário não acertar em nenhuma das 5 tentativas, informar qual era o número sorteado.
from random import randint
num_a = randint(0, 10)

for j in range(5):
    num4 = int(input('Adivinhe o número de 1 a 10: '))

    if num4 == num_a:
        print(f'Você acertou! O número era {num_a}')
        #break - para o looping ATUAL
        break
    else:
        print('Não foi dessa vez! Tente novamente.')
print('Fim!')



# %% 2. Jogo de Adivinhação
#Crie um programa em Python que sorteie um número aleatório entre 1 e 100 utilizando a biblioteca random.
#O usuário deverá tentar adivinhar o número sorteado, tendo no máximo 5 tentativas.
#   O programa deve:
#Utilizar random para sortear um número entre 1 e 100.
#Utilizar um laço for para controlar as 5 tentativas.
#A cada tentativa, solicitar que o usuário digite um número.
#Informar se o número digitado é maior ou menor que o número sorteado.
#Caso o usuário acerte, exibir uma mensagem de parabéns e encerrar as tentativas.
#Se o usuário não acertar em nenhuma das 5 tentativas, informar qual era o número sorteado.
#Desafio: tente utilizar break para encerrar o laço assim que o usuário acertar o número.
from random import randint
from time import sleep
#---from google.colab import output
#sleep () - para o programa por alguns segundos
#output.clear() - limpa a saida do programa
num_a = randint(0, 10)

for j in range(5):
    num4 = int(input('Adivinhe o número de 0 a 10: '))

    if num4 == num_a:
        print(f'Você acertou! O número era {num_a}')
         #break - para o looping ATUAL
        break
    else:
        print('Tente novamente.')
    if num_a > num4:
        print(f'🔼 O número sorteado é maior 🔼')
    else:
        print(f'🔽 O número sorteado é menor 🔽')
    sleep(4)
    #---output.clear()
print(f'Fim')



# %% 3. Maior Número e Quantidade de Números Digitados Escreva um programa em Python que solicite ao usuário a digitação de vários números. O programa deverá continuar pedindo números até que o usuário digite 0, que será utilizado para encerrar a entrada de dados.
#Ao final, o programa deverá:
#Identificar e exibir o maior número digitado.
#Informar a quantidade de números digitados, desconsiderando o zero utilizado para encerrar o programa.
#Utilize uma estrutura de repetição while para realizar a leitura dos números e estruturas condicionais para verificar qual é o maior número.
maior_numero = float('-inf')
quanti_n = 0
while True:
    quanti_n += 1
    num = float(input('Digite um número: "0 para sair" '))
    if num == 0:
        break
    elif num > maior_numero:
        maior_numero = num

print(f'O maior número digitado foi {maior_numero}')
print(f'Você digitou {quanti_n - 1}')



# %% 4. Média de notas:
#Crie um programa em Python que solicite ao usuário 4 notas de um aluno.
#Utilize um laço for para receber as notas e calcular a média aritmética. Ao final, exiba a média calculada.



# %% 5. Jogo de Adivinhação:
#com while Crie um programa em Python que sorteie um número aleatório entre 1 e 20 utilizando a biblioteca random.
#O usuário deverá tentar adivinhar o número sorteado, e o programa continuará solicitando novos palpites até que ele acerte.
#   O programa deve:
#Sortear um número aleatório entre 1 e 20 utilizando random. 
#Utilizar um laço while para repetir as tentativas até o usuário acertar. 
#Solicitar que o usuário digite um número a cada tentativa. 
#Informar se o número digitado é maior ou menor que o número sorteado. 
#Contar quantas tentativas o usuário realizou. 
#Quando o usuário acertar, exibir uma mensagem de parabéns e informar o número total de tentativas realizadas. 
#Desafio: inicialize um contador antes do laço while e atualize seu valor a cada palpite.