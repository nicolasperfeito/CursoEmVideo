#   Desenvolva um programa que pergunte a distância de uma viagem em KM.
#   Calcule o preço da passagem, cobrado R$0,50 por KM para viagens de até 200KM
#   e R$0,45 para viagens mais longas.

d = int(input('Vamos calcular o preço da viagem.\nPrimeiro, insira quantos a distância do trajeto em KM: '))

if d<=200:
    print('A viagem custa R${:.2f}'.format(d * 0.5))
else:
    print('A viagem custa R${:.2f}'.format(d * 0.45))