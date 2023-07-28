import PySimpleGUI as sg

arquivoUser = 'usuario/usuarios.txt'

def principal(nome):

    layout = [[sg.Text(nome)]]

    # Create the Window
    window = sg.Window( nome, layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
    window.close()

def validaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'r')
        a.close()
    except FileNotFoundError or FileExistsError: criaArquivo(nomeArquivo)
    except: print('Um erro inesperado aconteceu')
    else:
        print('Arquivo localizado'
              '')

def criaArquivo(nomeArquivo):
    with open(nomeArquivo, 'wt+') as arquivo:
        print('Arquivo criado com sucesso...')

def registrar(nome,email,senha,arquivo):
    with open(arquivo,'at+') as arquivo:
        arquivo.write(f'{nome},{email},{senha}\n')
        sg.popup('Cadastro concluído')

def validaLogin(nome,senha,nomeArquivo):
    with open(nomeArquivo, 'rt+') as arquivo:
        a=arquivo.readlines()
        print(a)
        flag= False
        for linhas in a:
            linhas = linhas.replace('\n','')
            lista = linhas.split(',')
            print(lista)
            if lista [0] == nome:
                flag = True
                if lista[2] == senha:
                    return lista[0]
                else:
                    sg.popup('Senha inválida')
                    break
        if not flag:
            sg.popup("usuario não encontrado")


def login():
    layout = [[sg.Text(' NOME'), sg.InputText(key='nome')],
              [sg.Text('SENHA'), sg.InputText(key='senha',password_char='*')],
              [sg.Button('login'), sg.Button('registrar'), sg.Button('sair')]]

    # Create the Window
    window = sg.Window('login', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'sair':  # if user closes window or clicks cancel
            break
        if event == 'registrar':
            window.hide()
            registro()
            window.un_hide()
        if event == 'login':
            nome = validaLogin(values['nome'],values['senha'],arquivoUser)
            if nome:
                window.close()
                return nome


    window.close()

def registro():
        layout = [[sg.Text('NOME '), sg.InputText(key='nome')],
                  [sg.Text('EMAIL '), sg.InputText(key='email')],
                  [sg.Text('SENHA'), sg.InputText(key='senha',password_char='*')],
                  [ sg.Button('SALVAR'), sg.Button('cancelar')]]

        # Create the Window
        window = sg.Window('Cadastro', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'cancelar':  # if user closes window or clicks cancel
                break
            if event == 'SALVAR':
                if  values['nome'] and values['email'] and values['senha'] and arquivoUser:

                    if len(values['senha']) >= 6:
                        if values['email'].count('@') == 1:
                            e1,e2 = values['email'].split('@')
                            if e2.count('.') >= 1 and e2.count('.') <= 2:
                                # validando nome
                                with open(arquivoUser, 'rt+') as arquivo:
                                    x = arquivo.readlines()
                                    flag = 0
                                    for i in x:
                                        nome,email,senha = i.split(',')
                                        if values['nome'] == nome:
                                            flag +=1
                                            sg.popup('Usuário já cadastrado')
                                            break
                                        if values['email'] == email:
                                            flag +=1
                                            sg.popup('Email já cadastrado')
                                            break
                                if flag == 0:

                                    registrar(values['nome'], values['email'], values['senha'], arquivoUser)
                                    break
                            else:
                                sg.popup('Email inválido')
                        else:
                            sg.popup('Email inválido')


                    else:
                        sg.popup('Senha precisa conter 6 dígitos')


                else:
                    sg.popup('Todos os campos precisam ser preenchidos!!!')


        window.close()
#progrma principal
validaArquivo(arquivoUser)
nome = login()
if nome:
    sg.popup(f'Usuario {nome} logando...')
    validaArquivo(f'Usuario/{nome}.txt')
    principal(nome)