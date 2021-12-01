#   Escreva um programa que faã o computador "pensar"
#   em um número inteiro entre 0 e 5 e peça para o usuário
#   tentar descobrir qual foi o número escolhido pelo computador.
#   O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

npc = randint(0,5)

pc = int(input('Tente advinhar um número entre 0 e 5!\nDigite o número: '))
print('Será que você escolheu o número certo???')

print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')

if npc==pc:
    print('Você acertou! O número era {}'.format(npc))
else:
    print('Você errou!\nO número era {}!\nTente novamente.'.format(npc))