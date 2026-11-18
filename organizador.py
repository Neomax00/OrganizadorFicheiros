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
        tamanho = ficheiro.stat().st_size
        
        if extensao == ".py":
            print("Tipo: Ficheiro Python (.py)")
        elif extensao == ".txt":
            print("Tipo: Ficheiro de Texto (.txt)")
        elif extensao == ".csv":
            print("Tipo: Ficheiro de Dados (.csv)")
        else:
            print("Tipo: Outro formato")
        
        
                    
        print("Nome:", ficheiro.name)
        print("Extensão:", extensao)
        print("Tamanho:", tamanho, "bytes")
        print("-----------------------")
        
    print(f"Total de ficheiros encontrados: {len(ficheiros)}")




"""
Path.cwd() indica o caminho completo da pasta de atual, onde o programa está a ser executado.

is_file() verifica se o elemento na pasta é um ficheiro.

suffix devolve a extensão do ficheiro.

"""