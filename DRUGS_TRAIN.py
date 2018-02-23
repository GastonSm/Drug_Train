#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function


from train_data_test import *
from dict_validation import *
from spacymoji import Emoji

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
LABEL2 = 'ME' #MISSPELLED WORD OR UNKNOW WORD

@plac.annotations(
    model=("Model name. Defaults to blank 'es' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))


def main(model='C:/Users/Pasante/Desktop/Gastón/drug_model_v4/spacy_model' , new_model_name='spacy_model_es_drug', output_dir='C:/Users/Pasante/Desktop/Gastón/spacy_model_es_drug', n_iter=200):
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Modelo cargado '%s'" % model)
    else:
        nlp = spacy.blank('es')  # create blank Language class
        print("Modelo en blanco 'es' creado")

    # Add emojis to pipe
    emoji = Emoji(nlp)
    nlp.add_pipe(emoji, first = True)
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last = True)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label(LABEL1)   # add new entity label to entity recognizer
    ner.add_label(LABEL2)   # add new entity label to entity recognizer
    losses_max = 99999999999
    t0 = datetime.datetime.now()
    print("Start: ", t0)

    # load test text
    validation_data = list(filter(None, open('test_text.txt','r').read().splitlines()))
    iteration = 0
    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()

        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            iteration = iteration + 1
            losses = {}
            for raw_text, entity_offsets in TRAIN_DATA:
                nlp.update([raw_text], [entity_offsets], drop=0.25, sgd=optimizer,
                           losses=losses)
            print(losses)
            print("Iteration:" + str(iteration))
            for text in validation_data:
                doc = nlp(text)
                ents = [(ent.text, ent.label_) for ent in doc.ents]
                for ent, label in ents:
                    print(f'Found entity: "{ent}": "{label}",')
                       
            # save model to output directory
            # take the most successful
            for a in losses.keys():
                if losses[a] < losses_max:
                    losses_max = losses[a]
                    if output_dir is not None:
                        output_dir = Path(output_dir)
                        if not output_dir.exists():
                            output_dir.mkdir()
                        nlp.meta['name'] = new_model_name  # rename model
                        nlp.to_disk(output_dir)
                        print("saved model: ", output_dir)
        
    # test the trained model
    print("Finished: ", datetime.datetime.now() - t0)
    print("\n\n\n")
 
if __name__ == '__main__':
    plac.call(main)
