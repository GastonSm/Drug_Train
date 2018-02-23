#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function



TRAIN_DATA = [
    ("Muy buena hierba", {
        'entities': [(10, 16, 'DRUG')]
    }),

    ("Buenas tardes Jose", {
        'entities': [(14,18,'PER')]
    }),

    ("Linda maria me fume en Roma", {
        'entities': [(6, 11, 'DRUG'), (23,27,'LOC')]
    }),
]
