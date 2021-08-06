"""
Gerando CPF

O gerador gera 9 números aleatórios, faz o cáluculo
para gerar os 2 últimos dígitos. Isso retorna um CPF válido.
"""
from random import randint
number = str(randint(100000000, 999999999))     # gerando 9 números aleatórios

sum_valitador = 0
dec = 10
new_cpf = number

for index in range(19):
    if index > 8:
        index -= 9

    sum_valitador += int(new_cpf[index]) * dec
    dec -= 1

    if dec < 2:
        dec = 11
        digit = 11 - (sum_valitador % 11)

        if digit > 9:
            digit = 0
        sum_valitador = 0
        new_cpf += str(digit)

print(new_cpf)
