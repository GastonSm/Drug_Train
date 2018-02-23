#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function

from train_tagger_pos import *

import plac
import random
from pathlib import Path
import spacy





@plac.annotations(
    lang=("ISO Code of language to use", "option", "l", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model='es_core_news_md',lang='es', output_dir='C:/Users/Gaston Migone/Desktop/es_drogas_taggerV2', n_iter=2):
    """Create a new model, set up the pipeline and train the tagger. In order to
    train the tagger with a custom tag map, we're creating a new Language
    instance with a custom vocab.
    """
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Modelo cargado '%s'" % model)
    else:
        nlp = spacy.blank('es')  # create blank Language class
        print("Modelo en blanco 'es' creado")


    # add the tagger to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'tagger' not in nlp.pipe_names:
        tagger = nlp.create_pipe('tagger')
        for tag, values in TAG_MAP.items():
            tagger.add_label(tag, values)
        nlp.add_pipe(tagger)
        
    # otherwise, get it, so we can add labels to it
    else:
        tagger = nlp.get_pipe('tagger')
        for tag, values in TAG_MAP.items():
            tagger.add_label(tag, values)

    # Add the tags. This needs to be done before you start training.
    



    validation_data = list(filter(None, open('Texto de prueba.txt','r').read().splitlines()))

    optimizer = nlp.begin_training()
    for i in range(n_iter):
        random.shuffle(TRAIN_DATA_POS)
        losses = {}
        for text, annotations in TRAIN_DATA_POS:
            nlp.update([text], [annotations], sgd=optimizer, losses=losses)
        print(losses)
        for text in validation_data:
                doc = nlp(text)
                for token in doc:
                    print(token.text,token.pos_)

  
    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Modelo guardado en: ", output_dir)

        # test the save model
        print("Modelo cargado desde: ", output_dir)
        nlp2 = spacy.load(output_dir)
        doc = nlp2(validation_data)
        print('Tags', [(t.text, t.tag_, t.pos_) for t in doc])


if __name__ == '__main__':
    plac.call(main)

