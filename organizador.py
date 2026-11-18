# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:18:36 2026

@author: Diogo Costa
"""

from pathlib import Path


pasta = Path.cwd()
print("ORGANIZADOR DE FICHEIROS")
print("-----------------------")
#for ficheiro in pasta.iterdir():
#    if ficheiro.is_file():
#        print("Nome:", ficheiro.name)
#        print("Extensão:", ficheiro.suffix)
#        print("-----------------------")


ficheiros = []

for f in pasta.iterdir():
    if f.is_file():
        ficheiros.append(f)
        

if not ficheiros:
    print("A pasta não contém ficheiros.")
else:
    for ficheiro in ficheiros:
        extensao = ficheiro.suffix
        
        if extensao == ".py":
            tipo = "Ficheiro Python (.py)"
        elif extensao == ".txt":
            tipo = "Ficheiro de Texto (.txt)"
        elif extensao == ".csv":
            tipo = "Ficheiro de Dados (.csv)"
                    
        print("Nome:", ficheiro.name)
        print("Extensão:", extensao)
        print("Tipo:", tipo)
        print("-----------------------")
        
    print(f"Total de ficheiros encontrados: {len(ficheiros)}")




"""
Path.cwd() indica o caminho completo da pasta de atual, onde o programa está a ser executado.

is_file() verifica se o elemento na pasta é um ficheiro.

suffix devolve a extensão do ficheiro.

"""