#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input('selecione o sexo F ou M: ')) .upper() .strip()
while sexo not in 'FM':
    sexo = str(input('selecione o sexo F ou M: ')).upper().strip()
print(f'Sexo selecionado {sexo} !!!')
