import os
import sys


def txt_importer(path_file):
    _, file_extension = os.path.splitext(path_file)
    if not path_file:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    if file_extension != '.txt':
        return sys.stderr.write("Formato inválido\n")
    else:
        with open(path_file, 'r') as file:
            reader = file.read().split('\n')
            print(reader)
        return reader
