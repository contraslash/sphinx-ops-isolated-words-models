#! /usr/local/python
# -*- coding: UTF-8 -*-
"""
Crea un diccionario a partir de una lista de fonemas
"""
import codecs
import re
NAME = "voxforge_test"
trasncript_file = "raw_transcription"
# trasncript_file = "ops_most_recorded_etc/example.transcription"
output_dict = NAME+"/"+NAME+"_etc/"+NAME+".dic"

def clean_accents(word):
    output = []
    for letter in word:
        modified_letter = ""
        if letter == u"á":
            modified_letter = "a"
        elif letter == u"é":
            modified_letter = "e"
        elif letter == u"í":
            modified_letter = "i"
        elif letter == u"ó":
            modified_letter = "o"
        elif letter == u"ú":
            modified_letter = "u"
        elif letter == u"ñ":
            modified_letter = "N"
        else:
            modified_letter = letter
        output.append(modified_letter)
    return ''.join(output)

def filter_special_characters(word):
    output = []
    for letter in word:
        modified_letter = ""
        if letter == u"-":
            modified_letter = ""
        elif letter == u"\n":
            modified_letter = ""
        elif letter == u"\.":
            modified_letter = ""
        elif letter == u"?":
            modified_letter = ""
        else:
            modified_letter = letter
        output.append(modified_letter)
    return ''.join(output)

def allow_characters(word):
    alphabet = "abcdefghijklmnNopqrstuvwxyz"
    output = []
    for letter in word:
        if letter in alphabet:
            output.append(letter)
    return ''.join(output)

def extract_phones_from_word(word):
    return ' '.join(apply_filters(word))

def apply_filters(word):
    return allow_characters(filter_special_characters(clean_accents(word)))

words = []
word_phones = []
file = codecs.open(trasncript_file, 'r', encoding="UTF-8")
lines = file.readlines()

for line in lines:
    print line
    line = " ".join(line.split()[1:])
    # line_words = re.split(':|;|\.| |,|-|\n|\r|\(|\)|¿|\?|¡|!', line)
    line_words = re.split(':|;| |,|\n|\r|\(|\)|¿|¡|!', ' '.join(line.replace("&quot;", " ").split(".")))
    print line_words

    for word in line_words:
        word = apply_filters(word)
        if word not in words:
            words.append(word)
            word_phones.append(extract_phones_from_word(word))

output_file = codecs.open(output_dict, 'w+', encoding="UTF-8")
for i in range(len(words)):
    output_file.write(unicode(words[i]) + " " + unicode(word_phones[i]) + "\n")

output_file.close()
