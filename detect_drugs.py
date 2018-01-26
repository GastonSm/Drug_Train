#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function


import plac
import random
from pathlib import Path
import spacy
from spacy import displacy


nlp = spacy.load('C:/Users/Gaston Migone/Desktop/Drug_Train/es_drogas_000')
#nlp = spacy.load('C:/Users/Gaston Migone/Desktop/es_drogas_000')

#doc = open('C:/Users/Gaston Migone/Desktop/Reporte Narco 1.txt','r',encoding="utf8").read()
doc = open('C:/Users/Gaston Migone/Desktop/Drug_Train/Texto de prueba.txt','r').read()
processed_doc = nlp(doc)

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
"""


for ent in processed_doc.ents:
   print(ent.label_, ent.text)
