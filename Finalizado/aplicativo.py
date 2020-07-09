import PySimpleGUI as sg
import functions


class TelaPython:
    def __init__(self):
        # SISTEMA INTEIRO
        while True:
            # LAYOUT
            inicio = [
                [sg.Text('=' * 120)],
                [sg.Text('MENU PRINCIPAL'.center(230))],
                [sg.Text('=' * 120)],
                # 1° LINHA
                [sg.Text('1 - Cadastrar um novo dia ', size=(24, 0)),
                 sg.Text('2 - Ver dias cadastradas', size=(24, 0)),
                 sg.Text('3 - Leitura de Dados', size=(35, 0)),
                 sg.Text('4 - Comparação de períodos')],
                # 2° LINHA
                [sg.Text('Mês', size=(6, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                                                              'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='addMes')),
                 sg.Text('', size=(25, 0)),
                 sg.Text('Mês Inicio', size=(7, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                                                                     'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='mesInicio1')),
                 sg.Text('', size=(2, 0)),
                 sg.Text('1° Mês Inicio', size=(9, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
                                                                        'Setembro', 'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='mesInicio2')),
                 sg.Text('2° Mês Inicio', size=(9, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
                                                                        'Setembro', 'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='mesInicio3'))],
                # 3° LINHA
                [sg.Text('Dia', size=(6, 0)), (sg.Input(size=(12, 0), key='addDia', do_not_clear=False)),
                 sg.Text('', size=(26, 0)),
                 sg.Text('Dia Inicio', size=(7, 0)), (sg.Input(size=(12, 0), key='diaInicio1', do_not_clear=False)),
                 sg.Text('', size=(4, 0)),

                 sg.Text('1° Dia Inicio', size=(9, 0)), (sg.Input(size=(12, 0), key='diaInicio2', do_not_clear=False)),
                 sg.Text('2° Dia Inicio', size=(9, 0)), (sg.Input(size=(12, 0), key='diaInicio3', do_not_clear=False))],
                # 4° LINHA
                [sg.Text('Crédito', size=(6, 0)), (sg.Input(size=(8, 0), key='addCredito', do_not_clear=False)),
                 sg.Button('+', size=(2, 0), key='creditoPlus'), sg.Text('', size=(26, 0)),
                 sg.Text('Mês Fim', size=(7, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                                                                  'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='mesFim1')),
                 sg.Text('', size=(2, 0)),

                 sg.Text('1° Mês Fim', size=(9, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
                                                                     'Setembro', 'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='mesFim2')),
                 sg.Text('2° Mês Fim', size=(9, 0)), (sg.InputCombo(('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
                                                                     'Setembro', 'Outubro', 'Novembro', 'Dezembro'), size=(12, 0), key='mesFim3'))],
                # 5° LINHA
                [sg.Text('Débito', size=(6, 0)), (sg.Input(size=(8, 0), key='addDebito', do_not_clear=False)),
                 sg.Button('+', size=(2, 0), key='debitoPlus'), sg.Text('', size=(26, 0)),

                 sg.Text('Dia Fim', size=(7, 0)), (sg.Input(size=(12, 0), key='diaFim1', do_not_clear=False)),
                 sg.Text('', size=(4, 0)),

                 sg.Text('1° Dia Fim', size=(9, 0)), (sg.Input(size=(12, 0), key='diaFim2', do_not_clear=False)),
                 sg.Text('2° Dia Fim', size=(9, 0)), (sg.Input(size=(12, 0), key='diaFim3', do_not_clear=False))],
                # 6° LINHA
                [sg.Text('Dinheiro', size=(6, 0)), (sg.Input(size=(8, 0), key='addDinheiro', do_not_clear=False)),
                 sg.Button('+', size=(2, 0), key='dinheiroPlus')],
                # 7° LINHA
                [sg.Button('Cadastrar dia', size=(18, 0), key='addButton'), sg.Text('', size=(5, 0)),
                 sg.Button('Ver cadastros', size=(16, 0), key='seeButton'), sg.Text('', size=(5, 0)),
                 sg.Button('Escolher período', size=(20, 0), key='chooseButton'), sg.Text('', size=(2, 0)),
                 sg.Button('Comparar períodos', size=(43, 0), key='compairButton')],
                # 8° LINHA
                [sg.Text('=' * 120)],
                # OUTPUT
                [sg.Text('', size=(33, 0)), sg.Output(size=(60, 100))]
            ]
            # JANELA
            janela = sg.Window('Caixa', size=(1000, 670)).layout(inicio)
            # INFOS ARQUIVO COM OS DADOS
            arquivonome = 'Caixa'
            arquivoExistePrincipal = functions.arquivoExiste(arquivonome)

            if arquivoExistePrincipal is False:
                print('Arquivo não existe')
                functions.criarArquivo(arquivonome)
            else:
                print('Arquivo existe')

            creditoNum = debitoNum = dinheiroNum = 0

            # TROCA DE INFOS ENTRE O COMPUTADOR E O USUÁRIO
            while True:
                event, values = janela.read()

                if event == 'creditoPlus' and values['addCredito'].isnumeric():
                    creditoNum += int(values['addCredito'])
                    print('*-' * 46)
                    print(f'O valor {values["addCredito"]} foi adicionado a crédito.')
                    print(f'Valor de crédito até agora é {creditoNum}.')

                if event == 'debitoPlus' and values['addDebito'].isnumeric():
                    debitoNum += int(values['addDebito'])
                    print('*-' * 46)
                    print(f'O valor {values["addDebito"]} foi adicionado a débito.')
                    print(f'Valor de débito até agora é {debitoNum}.')
                if event == 'dinheiroPlus' and values['addDinheiro'].isnumeric():
                    dinheiroNum += int(values['addDinheiro'])
                    print('*-' * 46)
                    print(f'O valor {values["addDinheiro"]} foi adicionado a dinheiro.')
                    print(f'Valor de dinheiro até agora é {dinheiroNum}.')
                if event == 'addButton' and values['addCredito'].isnumeric() \
                        and values['addDebito'].isnumeric() and values['addDinheiro'].isnumeric():
                    mes = values['addMes']
                    dia = values['addDia']
                    creditoNum += int(values['addCredito'])
                    credito = str(creditoNum)
                    debitoNum += int(values['addDebito'])
                    debito = str(debitoNum)
                    dinheiroNum += int(values['addDinheiro'])
                    dinheiro = str(dinheiroNum)
                    functions.opcao1(arquivonome, mes, dia, credito, debito, dinheiro)
                    debitoNum = creditoNum = dinheiroNum = 0

                elif event == 'seeButton':
                    functions.opcao2(arquivonome)
                elif event == 'chooseButton':
                    mesInicio1 = values['mesInicio1']
                    diaInicio1 = values['diaInicio1']
                    mesFim1 = values['mesFim1']
                    diaFim1 = values['diaFim1']
                    functions.opcao3(arquivonome, mesInicio1, diaInicio1, mesFim1, diaFim1)

                elif event == 'compairButton':
                    mesInicio2 = values['mesInicio2']
                    diaFim2 = values['diaFim2']
                    diaInicio2 = values['diaInicio2']
                    mesFim2 = values['mesFim2']
                    mesInicio3 = values['mesInicio3']
                    mesFim3 = values['mesFim3']
                    diaInicio3 = values['diaInicio3']
                    diaFim3 = values['diaFim3']
                    functions.opcao4(arquivonome, mesInicio2, diaInicio2, mesFim2, diaFim2, mesInicio3,
                                diaInicio3, mesFim3, diaFim3)


tela = TelaPython()
