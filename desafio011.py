print('Vamos calcular a área de uma parede e quanto de tinta você precisa para pintá-la.')
a = float(input('Digite a altura da parede em metros: '))
l = float(input('Agora, digite a largura da parede em metros: '))
area = float(a * l)
tinta = (area/2)
print('A área da parede é de {}m² e você vai precisar de {} litros de tinta para pintar essa parede.'.format(area,tinta))