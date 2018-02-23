

from __future__ import unicode_literals, print_function


from spacymoji import Emoji
import plac
import random
from pathlib import Path
import spacy
from spacy import displacy
import os

nlp = spacy.load('C:/Users/Pasante/Desktop/Gastón/Drug_Train/es_drogas_000')
#nlp = spacy.load('C:/Users/Pasante/Desktop/Gastón/es_drogas_act000')
#nlp = spacy.load('es_core_news_md')

#doc = open('C:/Users/Pasante/Desktop/Gastón/whatsapp-messages.csv','r').read()
doc = open('C:/Users/Pasante/Desktop/Gastón/whatsapp-messages.csv','r',encoding="utf8").read()
#doc = open('C:/Users/Pasante/Desktop/Gastón/Drug_Train/Texto de prueba.txt','r').read()


emoji = Emoji(nlp)
nlp.add_pipe(emoji, first = True)
processed_doc = nlp(doc)


with open('test.htm','w',encoding='utf-8-sig') as f:

   for ent in processed_doc.ents:
      print(ent.label_, ent.text)


   for token in processed_doc:
           if token._.is_emoji:
                   print(token._.emoji_desc)
                   print(token)
                   f.write(token._.emoji_desc)
                   f.write(str(token))

os.startfile('test.htm')

"""
for sent in processed_doc.sents:
    tmp = nlp(str(sent))
    for ent in tmp.ents:
        if ent.label_ == "DRUG":
            print(ent.label_, ent.text)
            print(tmp)



for ent in processed_doc.ents:
        if ent.label_ == "DRUG":
            print(ent.label_, ent.text)



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


for sent in processed_doc.sents:
   print_token_table(sent)


"""

