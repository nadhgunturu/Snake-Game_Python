from cx_Freeze import setup, Executable

setup(name = "myapp",
      version = '0.1',
      description = "Parse stuff",
      executables = [Executable("Snake_game.py")])
