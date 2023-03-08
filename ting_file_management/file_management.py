import os
import sys


def txt_importer(path_file):
    _, file_extension = os.path.splitext(path_file)
    if file_extension != '.txt':
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, 'r') as file:
            reader = file.read().split('\n')
        return reader
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
