#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function


from spacymoji import Emoji
from spacy import displacy
from pathlib import Path
import random
import spacy
import glob
import errno
import plac
import os
import io


#crea el nuevo directorio
def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)


def write_list_to_file(file, lst):
    if lst:
        cnt = 1
        lng = len(lst)
        for element in lst:
            file.write(element)
            if cnt < lng:
                file.write(", ")
                cnt = cnt + 1
            else:
                file.write(".")

#crea una copia de la lista de entidades encontrada sin repeticiones
def remove_duplicates(lst):
    newlist = []
    for element in lst:
       if element not in newlist:
           newlist.append(element)
    return newlist


#carga del modelo de spacy pre-entrenado con la entidad "DRUG"
nlp = spacy.load('spacy_model_es_drug')
#se agrega al pipeline el reconocimiento de emojis para poder analizar posible relación de estos con drogas
emoji = Emoji(nlp)
nlp.add_pipe(emoji, first = True)
path = 'C:/Users/Gaston Migone/Desktop/Gastón/Drug_Train/Files/*.csv'
files = glob.glob(path)
for name in files:
    try:
        print(f"\nAnalizando archivo: {name}... ")
        doc = open(name,'r',encoding="utf8").read()
        data = [(x.strip(), len(x) + 1) for x in doc.splitlines() if x]


        drugs_list = []
        per_list = []
        loc_list = []
        org_list = []
        misc_list = []
        me_list = []
        sentences = []
        emoji_drug = []
        emoji_sentences = []

        #lectura del nlp sobre el texto
        processed_raw_doc = nlp(doc)
        
        #si el texto posee emojis, estos serán descriptos y dibujados en un archivo .htm
        if processed_raw_doc._.has_emoji:
            with open(os.path.join(name[:-4]+'_Resultados','emojis.htm'),'w',encoding='utf-8-sig') as f:
                for token in processed_raw_doc:
                    if token._.is_emoji:
                        f.write(token._.emoji_desc)
                        f.write(str(token)+"\n")        

        #categorización de las entidades
        for element, lenght in data:
            processed_doc = nlp(element)
            for ent in processed_doc.ents:
                if ent.label_ == "DRUG":
                    drugs_list.append(ent.text)
                    sentences.append(element)
                if ent.label_ == "PER":
                    per_list.append(ent.text)
                if ent.label_ == "LOC":
                    loc_list.append(ent.text)
                if ent.label_ == "MISC":
                    misc_list.append(ent.text)
                if ent.label_ == "ORG":
                    org_list.append(ent.text)
                if ent.label_ == "ME":
                    me_list.append(ent.text)
            #en busca de emojis sospechosos        
            for token in processed_doc:
                if token._.is_emoji:
                    if ((token._.emoji_desc == "herb") or (token._.emoji_desc == "mushroom") or (token._.emoji_desc == "blossom")
                        or (token._.emoji_desc == "maple leaf") or (token._.emoji_desc == "syringe") or (token._.emoji_desc == "pill")
                        or (token._.emoji_desc == "cigarette") or (token._.emoji_desc == "biohazard")):
                       emoji_drug.append(token._.emoji_desc)
                       emoji_sentences.append(element)
                    
        mkdir_p(name[:-4]+'_Resultados')        
        filename = 'Resultados.txt'

        #para cada archivo analizado se genera una carpeta con los resultados del analisis hecho
        with open(os.path.join(name[:-4]+'_Resultados',filename),'w',encoding="utf8") as fi:
            counter_drug = 0
            counter_emoji = 0
            fi.write("\t\t\t\t------RESULTADOS OBTENIDOS POR EL RECONOCIMIENTO DE ENTIDADES--------\n\n\n\n\n")
            fi.write("Palabras referente a drogas encontradas: \n\t")
            nd_drugs_list = remove_duplicates(drugs_list)
            write_list_to_file(fi,nd_drugs_list)
            fi.write("\n\nPersonas encontradas: \n\t")
            nd_per_list = remove_duplicates(per_list)
            write_list_to_file(fi,nd_per_list)
            fi.write("\n\nLocaciones encontradas: \n\t")
            nd_loc_list = remove_duplicates(loc_list)
            write_list_to_file(fi,nd_loc_list)
            fi.write("\n\nOrganizaciones encontradas: \n\t")
            nd_org_list = remove_duplicates(org_list)
            write_list_to_file(fi,nd_org_list)
            fi.write("\n\nMisceláneos encontrados (Establecimientos, productos, nacionalidades): \n\t")
            nd_misc_list = remove_duplicates(misc_list)
            write_list_to_file(fi,nd_misc_list)
            fi.write("\n\nPalabras no reconocidas o mal escritas: \n\t")
            nd_me_list = remove_duplicates(me_list)
            write_list_to_file(fi,nd_me_list)
            fi.write("\n\nEmojis posiblemente referenciado a droga: \n\t")
            nd_emojid_list = remove_duplicates(emoji_drug)
            write_list_to_file(fi,nd_emojid_list)
            fi.write("\n\n\n")
            for drug in drugs_list:
                fi.write("\n\n\n" + drug.upper() + " visible en: \n")
                fi.write("\n\t" + str(sentences[counter_drug]))
                counter_drug = counter_drug + 1
            for emoji in emoji_drug:
                fi.write("\n\n\n" + emoji.upper() + " visible en: \n")
                fi.write("\n\t" + str(emoji_sentences[counter_emoji]))
                counter_emoji = counter_emoji + 1 

        print("Resultados guardados correctamente en: " +  name[:-4]+'_Resultados' + "\n")    
    except IOError as exc: 
        if exc.errno != errno.EISDIR:
            raise
print("Analisis finalizado correctamente.")

