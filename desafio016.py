#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
