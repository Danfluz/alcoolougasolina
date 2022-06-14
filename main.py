import PySimpleGUI as sg

sg.theme('SandyBeach')
layout = [
    [sg.T('',size=10),sg.T('Álcool ou Gasolina?',font='Arial 20'),sg.T('',size=10)],
    [sg.T('',size=(20,5)),sg.Im(r"alcgas.png",subsample=7),sg.T('',size=10)],
    [sg.T('Álcool (R$)',size=11,font='Arial 12'),sg.InputText('',size=8,font='Arial 12',key='alcool'),sg.T('',size=10)],
    [sg.T('Gasolina (R$)',size=11,font='Arial 12'),sg.InputText('',size=8,font='Arial 12',key='gasolina'),sg.T('',size=10)],
    [sg.T('',size=10),sg.B('Calcular',key='presscalc',font='Arial 12',size=10),sg.T('Resultado: ',font='Arial 12',size=10),sg.T('',size=(10),font=('Arial 12'),key='resultado')],
    [sg.T('',size=10),sg.T('',size=15),sg.T('',font='Arial 8',size=30,key='relacao')]
]

janela = sg.Window('Álcool ou Gasolina?', layout,icon=r"alcgas.ico",finalize=True)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'presscalc':

        gasolina = values['gasolina'].replace(',','.')
        alcool = values['alcool'].replace(',','.')

        if len(gasolina) == 0:
            continue
        elif len(gasolina) != 4:
            sg.Popup('Erro: Por favor, use o formato: 5,34',title='Ops!',font='Arial 12')
            continue
        else:
            try:
                gasolina = float(gasolina)
            except ValueError:
                sg.Popup('Use apenas números, pontos ou vírgulas.',title='Ops!',font='Arial 12')
                continue

        if len(alcool) == 0:
            continue
        elif len(alcool) != 4:
            sg.Popup('Erro: Por favor, use o formato: 5,34',title='Ops!',font='Arial 12')
            continue
        else:
            try:
                alcool = float(alcool)
            except ValueError:
                sg.Popup('Use apenas números, pontos ou vírgulas.',title='Ops!',font='Arial 12')
                continue
        valeapena = alcool / gasolina
        if valeapena < 0.7:
            janela['resultado'].update('ÁLCOOL')
            janela['relacao'].update(f'(Relação álcool/gasolina de {valeapena:.2f})')
        else:
            janela['resultado'].update('GASOLINA')
            janela['relacao'].update(f'(Relação álcool/gasolina de {valeapena:.2f})')

janela.close()
