import spacy
from spacy.tokens import Doc, Span, Token
from os import scandir, getcwd
from os.path import abspath
from termcolor import colored
import enchant


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return d[lenstr1-1,lenstr2-1]

#Sentence by sentence analysis of each token.
def sent_analyse(sent):
    sent_analysis = []
    for token in sent:
        text = token.text
        lemma = token.lemma_
        pos = token.pos_
        tag = token.tag_
        dep = token.dep_
        shape = token.shape_
        is_alpha = token.is_alpha
        is_stop = token.is_stop
        sent_analysis.append(
        {'token':text, 'lemma':lemma, 'pos':pos, 'tag' : tag, 'dep' : dep,
        'shape':shape, 'is_alpha':is_alpha, 'is_stop':is_stop})
    return sent_analysis

#Prints a table with token analisys for each token in sentence.
def print_token_table(sent):
    sent_analysis = sent_analyse(sent)
    print("TOKEN\tLEMMA\tPOS\tTAG\tDEP\tSHAPE\tALPHA?\tCOMMON")
    for token in sent_analysis:
        print(token['token'][:6] + "\t"
        + token['lemma'][:6] + '\t'
        + token['pos'] + '\t'
        + token['tag'][:6] + '\t'
        + token['dep'] + '\t'
        + token['shape'] + '\t'
        + str(token['is_alpha']) + '\t'
        + str(token['is_stop']))

def msg_analysis(msg_file):
    for line in msg_file.realines():
        doc = nlp(line)
        for sent in doc.sents:
            flag = False
            for token in sent:
                if not flag and token.lemma_ in target:
                    flag = True
                    for token in sent:
                        print((colored(token, 'red') if token.lemma_ in target else colored(token, 'green')) + ' ', end = '')
                    print('\n')


def nlp_load(model):
    nlp = spacy.load(model)
    return nlp

#path_default:"Training/Models/Diccionarios/dic_drogas.dic"
def nlp_load_drug_token_detection(nlp, path, levenshtein_dist):
    drugs_dict = [drug for drug in open(path, "r").read().splitlines()]

    is_drug_getter = lambda token: any(demerau_levenshten_distance(token.text, drug) <= levenshtein_dist for drug in drugs_dict)
    Token.set_extension('is_drug', getter=is_drug_getter)
    has_drug_getter = lambda obj: any([t._.is_drug for t in obj])
    Doc.set_extension('has_drug', getter=has_drug_getter)
    Span.set_extension('has_drug', getter=has_drug_getter)

    target_comercio = ['comprar', 'vender', 'comercializar', 'negociar', 'pagar',
    'dinero', 'plata', 'venta', 'compra']

    is_comercio_getter = lambda token: any(lemma == token.lemma_ for lemma in target_comercio)
    Token.set_extension('is_comercio', getter=is_comercio_getter)

    has_comercio_getter = lambda obj: any([t._.is_comercio for t in obj])
    Doc.set_extension('has_comercio', getter=has_comercio_getter)
    Span.set_extension('has_comercio', getter=has_comercio_getter)

def file_analyse(file_name, nlp):
    for line in open(file_name, "r").readlines():
        doc = nlp(line)
        if doc._.has_drug:
            for token in doc:
                print(colored(token, 'red') if token._.is_drug else colored(token, 'green'), end = ' ')


def dir_analyse(path, nlp):
    for arch in scandir(path):
        if arch.is_file():
            print(colored("Analizando --> ", "green") + colored("Archivo: " + abspath(arch.path), "blue") + "\n\n")
            file_text = open(abspath(arch.path), "r").readlines()
            doc = [nlp(line) for line in file_text]
            drug_suspicious = False
            comerce_suspicious = False
            consume_suspicious = False

            drug_suspicious_string = ""
            comerce_suspicious_string = ""
            consume_suspicious_string = ""

            for line in doc:
                if line._.has_drug:
                    drug_suspicious = True
                    for token in line:
                        drug_suspicious_string += ' ' + (colored(token, 'red') if token._.is_drug else colored(token, 'green'))
                    drug_suspicious_string += '\n'
                if line._.has_comercio:
                    comerce_suspicious = True
                    for token in line:
                        comerce_suspicious_string += ' ' + (colored(token, 'red') if token._.is_comercio else colored(token, 'green'))
                    comerce_suspicious_string += '\n'
            if drug_suspicious:
                drug_suspicious_string = colored(" --> Encontrada asociación con drogas:\n", "red") + drug_suspicious_string
                print(drug_suspicious_string)
            if comerce_suspicious:
                comerce_suspicious_string = colored(" --> Encontrada asociación con compra y venta:\n", "red") + comerce_suspicious_string
                print(comerce_suspicious_string)
            print('\n')
