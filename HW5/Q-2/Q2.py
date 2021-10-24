import numpy as np

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(word):
    word = list(word)
    for i in word:
        if i in punctuations:
            word.remove(i)           
    return ''.join(word)

remove_punctuation('Hello & class !')