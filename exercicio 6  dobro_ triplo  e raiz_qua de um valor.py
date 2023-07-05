#Exercício Python 006: Crie um algoritmo que leia um número
#e mostre o seu dobro,triplo e raiz quadrada

num = int(input('Insira um valor: '))
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5

print(f'Dobro {dobro}')
print(f'Triplo {triplo}')
print(f'Raiz {raiz :.2f}')
print(f'Raiz' pow(num))