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
