import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class Inicio:
    '''
    ---------------------------------------
    ---- Desenvolvido por Leandro Lima ----
    ---------------------------------------
    '''

    def __init__(self):
        self.segredo = 102030
        self.msg = 'Digite a senha: '

    def senha(self):
        print (Inicio.__doc__)
        while True:
            try:
                resp = int(input(self.msg))
            except ValueError as erro:
                print('Apenas números!')
                continue

            if resp != self.segredo:
                print('Senha errada :(')
            else:
                print('Senha correta :)')
                return False

x = Inicio()
# x.senha()


class DashBoard:

    def __init__(self):
        self.leandro = Tk()
        self.leandro.geometry('600x300')
        self.leandro.title('LELE LIMA')
        self.menubar = Menu(self.leandro)

        # Menu 1
        def menu_sistema_1(): os.system('sysdm.cpl')
        def menu_sistema_2(): os.system('lusrmgr.msc')
        def menu_sistema_3(): os.system('gpedit.msc')
        def menu_sistema_4(): os.system('hdwwiz.cpl')
        def menu_sistema_5(): os.system('appwiz.cpl')
        def menu_sistema_6(): os.system('msconfig')
        def menu_sistema_7(): os.system('regedit')
        def menu_sistema_8(): os.system('cleanmgr')

        menu_sistema = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Sistema', menu = menu_sistema)
        menu_sistema.add_command(label ='Propriedades do Sistema', command = menu_sistema_1)
        menu_sistema.add_command(label ='Usuários e Grupos Locais', command = menu_sistema_2)
        menu_sistema.add_command(label ='Politica de Grupo Local', command = menu_sistema_3)
        menu_sistema.add_command(label ='Gerenciador de Dispositivos', command = menu_sistema_4)
        menu_sistema.add_command(label ='Desinstalar/Alterar Programa', command = menu_sistema_5)
        menu_sistema.add_command(label ='Configuração do Sistema', command = menu_sistema_6)
        menu_sistema.add_command(label ='Editor do Registro', command = menu_sistema_7)
        menu_sistema.add_command(label ='Limpeza de Disco', command = menu_sistema_8)
        menu_sistema.add_separator()
        menu_sistema.add_command(label ='Sair', command = self.leandro.destroy)

        # Menu 2
        def menu_prompt_1(): os.system('date /t && time /t && whoami && net users')
        def menu_prompt_2(): os.system('systeminfo')
        def menu_prompt_3(): os.system('wmic bios get serialnumber')
        def menu_prompt_4(): os.system('ipconfig /all')
        def menu_prompt_5(): os.system('shutdown /r /t 1')
        def menu_prompt_6(): os.system('shutdown /s /t 1')

        menu_prompt = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Prompt de Comando', menu = menu_prompt)
        menu_prompt.add_command(label ='Informações do Usuario', command = menu_prompt_1)
        menu_prompt.add_command(label ='Informações do Sistema', command = menu_prompt_2)
        menu_prompt.add_command(label ='Informações do Serial', command = menu_prompt_3)
        menu_prompt.add_command(label ='Informações do IP', command = menu_prompt_4)
        menu_prompt.add_separator()
        menu_prompt.add_command(label ='Reinicar Sistema', command = menu_prompt_5)
        menu_prompt.add_command(label ='Desligar Sistema', command = menu_prompt_6)

        # Menu 3
        def menu_ajuda_1(): messagebox.showinfo(title='Leandro', message='Leandro Lima !')

        menu_ajuda = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Ajuda', menu = menu_ajuda)
        menu_ajuda.add_command(label ='Sobre o Autor', command = menu_ajuda_1)

        self.leandro.config(menu = self.menubar)
        self.leandro.mainloop()

x = DashBoard()
