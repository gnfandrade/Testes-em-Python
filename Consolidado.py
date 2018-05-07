# Script de consolidação do aprendizado em python.
# Autor: Gustavo Nunes
# Data: 06/05/2018
# coding: utf-8

# Bloco para execução da estrutura de decisão em python
numero = int(input('Digite um número: '))

if numero > 10:
    print('Número maior que dez!')
elif numero <= 10 and numero > 0:
    print('Número está entre 0 e dez')
else:
    print('Número inteiro negativo')
# Posteriormente descrever este bloco como uma função.

# Bloco para a execução do laço de repetição sem variável de controle.
while numero > 10:
    print(numero)
    numero -= 1
else:
    print('Loop finalizado com sucesso!!!')
# Posteriormente elencar com alguma função.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,66,77,88,99,100,numero]

# Bloco laço de repetição com variável de controle pelos statements "break" e "continue".
for i in lista:
    print(i)
    if i > 66:
        print("Saindo do laço")
        break
else:
    print("Laço abortado com sucesso!")

for i in lista:
    if i%2 == 0:
        continue
    print(i)
else:
    print("Loop Executado com sucesso!!!")












