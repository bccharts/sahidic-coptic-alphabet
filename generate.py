#!/usr/bin/env python

# Script to generate graded list of glyphs

import grade

# Sahidic Coptic alphabet glyphs
glyphs = [
    u"\u2c80",
    u"\u2c82",
    u"\u2c84",
    u"\u2c86",
    u"\u2c88",
    u"\u2c8c",
    u"\u2c8e",
    u"\u2c90",
    u"\u2c92",
    u"\u2c94",
    u"\u2c96",
    u"\u2c98",
    u"\u2c9a",
    u"\u2c9c",
    u"\u2c9e",
    u"\u2ca0",
    u"\u2ca2",
    u"\u2ca4",
    u"\u2ca6",
    u"\u2ca8",
    u"\u2caa",
    u"\u2cac",
    u"\u2cae",
    u"\u2cb0",
    u"\u03e2",
    u"\u03e4",
    u"\u03e8",
    u"\u03ea",
    u"\u03ec",
    u"\u03ee",
]

graded_list = grade.GradedList(list(glyphs))

result = graded_list.make()

# Save it
with open('graded-alphabet.list', 'w') as f:
    f.write(' '.join(result).encode('utf-8'))
