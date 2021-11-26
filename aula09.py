print('Manipulando Texto')
print('Fatiamento:\n')

print('Frase de exemplo é: Curso em vídeo Python')
print('='*40)
frase = 'Curso em Vídeo Python'

print('Exemplo 1')
print("print(frase[2:10:2])")
print(frase[2:10:2])
print('No exemplo acima, o print fatia a frase do caractere 2 até o 10,\npulando de 2 em 2 casas.')
print('='*40)

print('Exemplo 2')
print("print(frase[:5])")
print(frase[:5])
print('Este exemplo faz com que o print mostre do início da frase até o caractere 5')
print('='*40)

print('Exemplo 3')
print('print(frase[15:])')
print(frase[15:])
print('Com ":" após o número, o print mostra somente os carcteres após o caractere 15')
print('='*40)

print('Exemplo 4')
print('print(frase[9::3])')
print(frase[9::3])
print('Com este exemplo, começará o print a partir do 9, até o infinito,\ne pulando de 3 em 3 casas')

print('='*40)
print('='*40)

print('Análise:\n')
print('Comando "len"')
print('(print(len(frase))')
print(len(frase))
print('O comando "len" faz a análise da frase com a contagem de caracteres que possui (0-21')

print('='*40)

print('Outra forma de analisar a string é pelo comando "count"')
print("print(frase.count('o'))")
print(frase.count('o'))
print("print(frase.count('o',0,13))")
print(frase.count('o',0,13))
print('Esse comando faz a contagem da letra "o" entre 0 e 13')

print('='*40)

print('Find')
print('O comando find encontra a posição das letras especificadas')
print("frase.find('deo')")
print(frase.find('deo'))
print('No caso, mostra onde a sequencia de letras "deo" começou, ou seja, na posição 11')
print('Se colocar no find uma string que não existe dentro da string analisada, retorna o valor -1')
print("frase.find('Android')")
print(frase.find('Android'))
print('='*40)
print('='*40)

print('Replace')
print('O comando replace substitiu uma string por outra.')
print("frase = frase.replace('Python', 'Android')")
print('A primeira string após o parenteses é a que vai ser substituida pela segunda string.\nVeja o resultado:')
frase = frase.replace('Python', 'Android')
print(frase)




