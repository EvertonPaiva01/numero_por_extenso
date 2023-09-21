from typing import Any
from num2words import num2words
import PySimpleGUI as sg

def number_to_long_number(number_p):
    if number_p.find(',')!=-1:
        number_p = number_p.split(',')
        number_p1 = int(number_p[0].replace('.',''))
        number_p2 = int(number_p[1])
    else:
        number_p1 = int(number_p.replace('.',''))
        number_p2 = 0    
        
    if number_p1 == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'
        
    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'
        
    text1 = ''
    if number_p1 > 0:
        text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
    else:
        text1 = ''
    
    if number_p2 > 0:
        text2 = num2words(number_p2,lang='pt_BR') + str(aux2) 
    else: 
        text2 = ''
    
    if (number_p1 > 0 and number_p2 > 0):
        result = text1 + ' e ' + text2
    else:
        result = text1 + text2

    return result.replace(',','')

class TelaPython:
    def __init__(self):
        # Layout
        #sg.theme('GrayGrayGray')
        layout = [
            [sg.Text('Digite o número:')],
            [sg.Input(key='numero',size=(35,0),font=("Helvetica", 16))],
            [sg.Button('OK')],
            [sg.Output(size=(50,10),key = 'saida',font=("Helvetica", 18), pad=(2, 21))],
            [sg.Text('Created by: Everton da Silva Paiva', font='Arial 8')]
        ]
        self.janela = sg.Window("Número por Extenso").layout(layout)
        #self.event, self.values = self.janela.Read()

    def Iniciar(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!','@','#','$','%','¨','&','*','(',')','/','[',']','{','}',':','?','-']

        while True:
            
            self.event, self.values = self.janela.Read()
            
            if self.event == sg.WIN_CLOSED:
                break
            if self.values['numero'] == '':
                sg.popup('Erro!, O campo de número não pode ficar vazio')
                self.event, self.values = self.janela.Read()

            if len(self.values['numero']) > 18:
                sg.popup('O número é muito grande! Meu amigo, vá devagar...')
                self.event, self.values = self.janela.Read()

            for i in letras:
                if i in self.values['numero']:
                    sg.popup('Erro!, O campo de número não pode conter letras ou caracteres especiais')
                    self.event, self.values = self.janela.Read()

            if self.event == 'OK':
                #self.janela['numero'].update('')
                self.janela['saida'].update('')
            numero = self.values['numero']
            resposta = number_to_long_number(numero)
            print(resposta)


tela = TelaPython()
tela.Iniciar()