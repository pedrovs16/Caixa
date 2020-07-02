import PySimpleGUI as sg


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
        print('Arquivo criado')
    except:
        print('Houve algum erro')


def opcao1(arquivo, mes, dia, credito, debito, dinheiro):
    try:
        a = open(arquivo, 'at')
        mesUpper = mes.upper()
        a.write(f'{mesUpper};{dia};{credito};{debito};{dinheiro}\n')
    except:
        print('*-' * 46)
        print('ERROR. Não consegui computar os dados')
    else:
        try:
            a.close()
        except:
            print('*-' * 46)
            print('Arquivo não conseguiu ser fechado')
        else:
            print('*-' * 46)
            print('Cadastro feito com sucesso')
            print(f'Mês: {mesUpper}')
            print(f'Dia: {dia}')
            print(f'Crédito: {credito}')
            print(f'Débito: {debito}')
            print(f'Dinheiro {dinheiro}')


def opcao2(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('*-' * 46)
        print('Arquivo não conseguiu ser aberto')
    else:
        print('*-' * 46)
        print('...')
        print(f'DATA{"CRÉDITO":>22}{"""DÉBITO""":>12}{"DINHEIRO":>15}{"MÉDIA":>15}')
        print('-' * 98)
        for linha in arquivo:
            dado = linha.split(';')
            dado[4] = dado[4].replace('\n', '')
            media = int(dado[2]) + int(dado[3]) + int(dado[4])
            print(f'{dado[0]} {dado[1]:<{22 - len(dado[0]) - len(dado[1])}}{dado[2]:<17}'
                  f'{dado[3]:<17}{dado[4]:<20}{media}')
        arquivo.close()


def opcao3(nome, mesInicio1, diaInicio1, mesFinal1, diaFinal1):
    try:
        try:
            arquivo = open(nome, 'rt')
        except:
            print('*-' * 46)
            print('Arquivo não conseguiu ser aberto')
        else:
            print('...')
            mesInicio1Upper = mesInicio1.upper()
            mesFinal1Upper = mesFinal1.upper()
            debitoTotal = dinheiroTotal = creditoTotal = 0
            informacao = False
            duracao = 0
            error = False

            for linha in arquivo:
                dado = linha.split(';')
                dado[4] = dado[4].replace('\n', '')
                if mesInicio1Upper == dado[0] and diaInicio1 == dado[1]:
                    informacao = True
                if informacao == True:
                    creditoTotal += int(dado[2])
                    debitoTotal += int(dado[3])
                    dinheiroTotal += int(dado[4])
                    duracao += 1
                if mesFinal1Upper == dado[0] and diaFinal1 == dado[1]:
                    informacao = False
                    error = True

            somaTotal = creditoTotal + debitoTotal + dinheiroTotal
            print('*-' * 46)
            if error == False:
                print('Algum valor foi digitado errado')
            print(f'{mesInicio1Upper}:{diaInicio1}/{mesInicio1Upper}:{diaFinal1}')
            print(f'Durante {duracao} dias.')
            print(f'Soma dos valores em créditos = {creditoTotal}.')
            print(f'Soma dos valores em débitos = {debitoTotal}.')
            print(f'Soma dos valores em dinheiro = {dinheiroTotal}.')
            print(f'Lucro total = {somaTotal}')
            print(f'A média de lucro por dia é {(somaTotal / duracao):.2f}')
            if error == False:
                print('Algum valor foi digitado errado')
    except:
        print('*-' * 46)
        print('Algum valor foi digitado errado.')


def opcao4(nome, mesInicio1, diaInicio1, mesFinal1, diaFinal1, mesInicio2, diaInicio2, mesFinal2, diaFinal2):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('*-' * 46)
        print('Arquivo não conseguiu ser aberto')
    else:
        try:
            print('...')
            debitoTotal1 = dinheiroTotal1 = creditoTotal1 = 0
            informacao1 = False
            duracao1 = 0
            mesInicio1Upper = mesInicio1.upper()
            mesInicio2Upper = mesInicio2.upper()
            mesFinal2Upper = mesFinal2.upper()
            mesFinal1Upper = mesFinal1.upper()
            error1 = False

            for linha in arquivo:
                dado1 = linha.split(';')
                dado1[4] = dado1[4].replace('\n', '')
                if mesInicio1Upper == dado1[0] and diaInicio1 == dado1[1]:
                    informacao1 = True
                if informacao1 == True:
                    creditoTotal1 += int(dado1[2])
                    debitoTotal1 += int(dado1[3])
                    dinheiroTotal1 += int(dado1[4])
                    duracao1 += 1
                if mesFinal1Upper == dado1[0] and diaFinal1 == dado1[1]:
                    informacao1 = False
                    error1 = True
            somaTotal1 = creditoTotal1 + debitoTotal1 + dinheiroTotal1

            arquivo.close()
            arquivo = open(nome, 'rt')

            debitoTotal2 = dinheiroTotal2 = creditoTotal2 = 0
            informacao2 = False
            duracao2 = 0
            error = False
            for linha in arquivo:
                dado2 = linha.split(';')
                dado2[4] = dado2[4].replace('\n', '')
                if mesInicio2Upper == dado2[0] and diaInicio2 == dado2[1]:
                    informacao2 = True
                if informacao2 == True:
                    creditoTotal2 += int(dado2[2])
                    debitoTotal2 += int(dado2[3])
                    dinheiroTotal2 += int(dado2[4])
                    duracao2 += 1
                if mesFinal2Upper == dado2[0] and diaFinal2 == dado2[1]:
                    informacao2 = False
                    error = True

            somaTotal2 = creditoTotal2 + debitoTotal2 + dinheiroTotal2
            media1 = somaTotal1 / duracao1
            media2 = somaTotal2 / duracao2
            print('*-' * 46)
            if error == False or error1 == False:
                print('Algum valor foi digitado errado')
            print(
                f'PERÍODO {mesInicio1Upper:>15}:{diaInicio1}/{mesFinal1Upper}:{diaFinal1}{mesInicio2Upper:>14}:{diaInicio2}/{mesFinal2Upper}:{diaFinal2} ')
            print(f'CRÉDITO {creditoTotal1:>27}  {creditoTotal2:>37}')
            print(f'DÉBITO {debitoTotal1:>29}  {debitoTotal2:>37}')
            print(f'DINHEIRO {dinheiroTotal1:>26}  {dinheiroTotal2:>37}')
            print(f'TOTAL {somaTotal1:>31} {somaTotal2:>38}')
            print(f'MÉDIA DIÁRIA {media1:>20.2f}  {media2:>36.2f}')
            if error == False:
                print('Algum valor foi digitado errado')
        except:
            print('*-' * 46)
            print('Algum dado foi digitado errado.')
