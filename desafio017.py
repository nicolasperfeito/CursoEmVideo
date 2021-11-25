#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt

a = float(input('Digite o valor do primeiro cateto: '))
b = float(input('Digite o valor do segundo cateto: '))

c = sqrt(a**2+b**2)

print('O valor da hipotenusa é {}'.format(c))