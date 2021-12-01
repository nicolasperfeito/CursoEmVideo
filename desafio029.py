#   Escreva um programa que leia a velocidade de um carro.
#   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
#   ele foi multado.
#   A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade do carro? '))
exc = (vel - 80)
multa = (exc * 7)

if vel>80:
    print('A sua velocidade ultrapassou 80Km/h, e excedeu em {}Km/h o limite.'.format(exc))
    print('A multa recebida tem o valor de R${}.'.format(multa))
else:
    print('Você estava dentro do limite de velocidade, continue respeitando as regras de trânsito!')