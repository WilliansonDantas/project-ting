import os
import sys


def txt_importer(path_file):
    if not path_file:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
