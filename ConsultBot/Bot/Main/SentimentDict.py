#Sentiment dictionary
import re



def pos_files():

    posDictionary = open(r'/home/michael/Desktop/Project/ConsultBot/Bot/Corpora/positive-words.txt', 'r', encoding="ISO-8859-1")
    posWordList = re.findall(r"[a-z\-]+", posDictionary.read())
    return posWordList

def neg_files():
    negDictionary = open(r'/home/michael/Desktop/Project/ConsultBot/Bot/Corpora/negative-words.txt', 'r', encoding="ISO-8859-1")
    negWordList = re.findall(r"[a-z\-]+", negDictionary.read())
    return negWordList

def read_det_file():

    determiners = open(r'/home/michael/Desktop/Project/ConsultBot/Bot/Corpora/det-words.txt', 'r', encoding="ISO-8859-1")
    determiner_bank = re.findall(r"[a-z\-]+", determiners.read())
    return determiner_bank

def read_negate_file():

    negators = open(r'/home/michael/Desktop/Project/ConsultBot/Bot/Corpora/NegationWords.txt', 'r', encoding="ISO-8859-1")
    negators_bank = re.findall(r"[a-z\-]+", negators.read())
    return negators_bank
