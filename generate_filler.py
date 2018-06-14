#! /usr/local/python
# -*- coding: UTF-8 -*-
"""
Genera un archivo con los silencios necesarios para el entrenamiento
"""
import codecs
FILLER_FILE = "etc/ops_aphasia.filler"


def execute_script(filler_file):

    default_silences = ['<s>', '<sil>', '</s>']

    f = codecs.open(filler_file, 'w+', encoding='UTF-8')
    for default_silence in default_silences:
        f.write(default_silence + "\t" + "SIL\n")

    f.close()


if __name__ == "__main__":
    execute_script(FILLER_FILE)
