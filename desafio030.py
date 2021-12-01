#   Crie um programa que leia um número inteiro e mostra na tela se ele é PAR ou IMPAR.

num = int(input('Digite um número e vamos descobrir se ele é par ou ímpar! '))
res = num % 2
if res == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))