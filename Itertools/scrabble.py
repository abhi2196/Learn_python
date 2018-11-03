import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    all_permutations = _get_permutations_draw(draw)
    return [ item for item in all_permutations if item in dictionary ]

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    max_length = len(draw)
    result = []
    for i in range(1, max_length + 1):
        out = itertools.permutations(draw, i)
        for item in out:
            result.append(''.join(item).lower())
    return result
