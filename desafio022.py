#   Crue um programa que leia o nome completo de uma pessoa e mostre:
#   O nome com todas as letras maíusculas
#   O nome com todas minúsculas
#   Quantas letras ao todo (sem considerar espaços)
#   Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: '))
print('O nome com letras maiúsculas fica assim: ')
print(nome.upper())
print('O nome com letras minúsculas fica assim: ')
print(nome.lower())
print('O seu nome contém a seguinte quantidade de letras: ')
print(len(nome))
print('Seu primeiro nome contém a seguinte quantidade de letras: ')
print(len(nome.split()[0]))

