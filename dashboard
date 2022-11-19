import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# Controle de Acesso
def password():

    segredo = 102030

    while True:
        try:
            senha = int(input('Digite a senha: '))
        except ValueError as erro:
            print('A senha deve ser numérica !!!',erro)
            continue

        if senha != segredo:
            print('Senha Incorreta !!!')
        else:
            print('Senha Correta !\n')
            return False

s = password()

# Janela
leandro = Tk()
leandro.geometry('600x300')
leandro.title('DE OSASCO - NIT')

# Barra de Menu
menubar = Menu(leandro)

# Menu 1
def menu1_1(): os.system('sysdm.cpl')
def menu1_2(): os.system('lusrmgr.msc')
def menu1_3(): os.system('gpedit.msc')
def menu1_4(): os.system('hdwwiz.cpl')
def menu1_5(): os.system('appwiz.cpl')
def menu1_6(): os.system('msconfig')
def menu1_7(): os.system('regedit')
def menu1_8(): os.system('cleanmgr')

menu1 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Sistema', menu = menu1)
menu1.add_separator()
menu1.add_command(label ='Propriedades do Sistema', command = menu1_1)
menu1.add_command(label ='Usuários e Grupos Locais', command = menu1_2)
menu1.add_command(label ='Politica de Grupo Local', command = menu1_3)
menu1.add_command(label ='Gerenciador de Dispositivos', command = menu1_4)
menu1.add_command(label ='Desinstalar/Alterar Programa', command = menu1_5)
menu1.add_command(label ='Configuração do Sistema', command = menu1_6)
menu1.add_command(label ='Editor do Registro', command = menu1_7)
menu1.add_command(label ='Limpeza de Disco', command = menu1_8)
menu1.add_separator()
menu1.add_command(label ='Sair', command = leandro.destroy)

# Menu 2
def menu2_1(): os.system('date /t && time /t && whoami && net users')
def menu2_2(): os.system('systeminfo')
def menu2_3(): os.system('wmic bios get serialnumber')
def menu2_4(): os.system('ipconfig /all')
def menu2_5(): os.system('shutdown /r /t 1')
def menu2_6(): os.system('shutdown /s /t 1')

menu2 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Prompt de Comando', menu = menu2)
menu2.add_separator()
menu2.add_command(label ='Informações do Usuario', command = menu2_1)
menu2.add_command(label ='Informações do Sistema', command = menu2_2)
menu2.add_command(label ='Informações do Serial', command = menu2_3)
menu2.add_command(label ='Informações do IP', command = menu2_4)
menu2.add_separator()
menu2.add_command(label ='Reinicar Sistema', command = menu2_5)
menu2.add_command(label ='Desligar Sistema', command = menu2_6)

# Menu 3
def menu3_1(): messagebox.showinfo(title='Leandro', message='Oi, eu sou o Goku !')

menu3 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ajuda', menu = menu3)
menu3.add_separator()
menu3.add_command(label ='Sobre o Autor', command = menu3_1)

# Mostrar Menu
leandro.config(menu = menubar)
leandro.mainloop()
