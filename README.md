# dashboard_kivy

***** MANUAL DE CONFIG. DA BIBLIOTECA TKINTER PARA PYTHON 3 *****


1 - Instalar o Python 3.9 via Microsoft Sore



2 - Instalar bibliotecas: idna e cx_Freeze
win + r
	cmd
		pip install idna
		pip install cx_Freeze



3 - Criar arquivo setup.py e colar o código abaixo

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("dashboard.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "1",
    description = '<any description>',
    executables = executables
)



4 - Criar seu script com o nome dashboard.py



5 - Compilar seu script para executável windows
win + r
	cmd
		python setup.py build



6 - Acesse a pasta criada e execute o arquivo dashboard.exe
