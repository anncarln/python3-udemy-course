"""
Validando CPF

O validador funciona pegando os 9 primeiros dígitos do CPF
original, faz o cálculo para gerar os 2 dígitos finais e cria
um novo CPF com os dígitos que foram gerados. Depois ele checa
por comparação se o CPF que ele gerou é igual o CPF original.
Se for, o CPF é válido.

"""
while True:
    cpf = input('Informe o seu CPF: ')
    sum_valitador = 0
    dec = 10
    cpf_sliced = cpf[:9]

    for index in range(19):
        if index > 8:
            index -= 9

        sum_valitador += int(cpf_sliced[index]) * dec
        dec -= 1

        if dec < 2:
            dec = 11
            digit = 11 - (sum_valitador % 11)

            if digit > 9:
                digit = 0
            sum_valitador = 0
            cpf_sliced += str(digit)

    if cpf == cpf_sliced:
        print('Válido')
    else:
        print('Inválido')
