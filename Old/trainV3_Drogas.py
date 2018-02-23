#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function

from train_data_2 import *
from dict_validation import *


import datetime
import ujson as json
import plac
import random
from pathlib import Path
import spacy
from spacy.pipeline import EntityRecognizer
from spacy.pipeline import Tagger
from spacy.gold import GoldParse
from spacy.tokens import Doc
from collections import Counter, defaultdict



# new entity label
LABEL1 = 'DRUG'
LABEL2 = 'ME' #MAL ESCRITO

@plac.annotations(
    model=("Model name. Defaults to blank 'es' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))


def main(model='C:/Users/Gaston Migone/Desktop/drug_model_v4/spacy_model' , new_model_name='spacy_model_v2', output_dir='C:/Users/Gaston Migone/Desktop/drug_model_v4/spacy_model_v2', n_iter=500):
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Modelo cargado '%s'" % model)
    else:
        nlp = spacy.blank('es')  # create blank Language class
        print("Modelo en blanco 'es' creado")

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last = True)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label(LABEL1)   # add new entity label to entity recognizer
    ner.add_label(LABEL2)

    t0 = datetime.datetime.now()
    print("Start: ", t0)

    # load test
    validation_data = list(filter(None, open('Texto de prueba.txt','r').read().splitlines()))
    error_global = 1_000_000_000_000
    
    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()

        """
        for raw_text, _ in TRAIN_DATA:
            doc = nlp.make_doc(raw_text)
            for word in doc:
                _ = nlp.vocab[word.orth]
        ner = EntityRecognizer(nlp.vocab, entity_types=['PERSON', 'LOC', 'MISC', 'DRUG', 'ME', 'ORG'])
        """
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            for raw_text, entity_offsets in TRAIN_DATA:
                nlp.update([raw_text], [entity_offsets], drop=0.25, sgd=optimizer,
                           losses=losses)
            print(losses)
            for text in validation_data:
                doc = nlp(text)
                ents = [(ent.text, ent.label_) for ent in doc.ents]
                error = 0
                for ent, label in ents:
                    if ent in dict_validation:
                        if label != dict_validation[ent]:
                            error += 1
                    else:
                        print(f'No encontrada: "{ent}": "{label}",')
                        error += 2
                        
                if error < error_global:
                    # save model to output directory
                    if output_dir is not None:
                        output_dir = Path(output_dir)
                        if not output_dir.exists():
                            output_dir.mkdir()
                        nlp.meta['name'] = new_model_name  # rename model
                        nlp.to_disk(output_dir)
                        print("Modelo guardado en ", output_dir)
                    error_global = error
        

    # test the trained model
    print("Finished: ", datetime.datetime.now() - t0)
    print("\n\n\n")
 
if __name__ == '__main__':
    plac.call(main)
