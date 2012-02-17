"""First programming assignment for NLP question at end of AI class.

Author: Robert Berry <rjberry@gmail.com>
"""
import re
import string

from collections import Counter

from utils import argmax, product

CORPUS_FILE = "corpus.txt"

PROBLEM = "Esp qtcde nzyqpcpynp zy esp ezatn zq Lcetqtntlw Tyepwwtrpynp hld spwo le Olcexzfes Nzwwprp ty estd jplc."

class Corpus(object):
    """Represents a corpus of words from which histogramatic probabilities can
    be inferred.
    """
    def __init__(self, words):
        """Creates the corpus from the list of words.
        """
        self.counts = Counter(words)
    
    def Pword(self, word):
        """Histogram probability of the given word based on the corpus.
        """
        return float(self.counts[word]) / self.total_words

    @property
    def total_words(self):
        """Total count of words in corpus.
        """
        return sum(self.counts.values())

    def Psentence(self, sentence):
        """Naive Bayesian probability of the given sentence using the bag of words
        technique.
        """
        # tried doing this with product and it was too small - review material
        return sum(self.Pword(word) for word in words(sentence))

def rotation(text, n):
    """Rotation cipher. Replaces letters in the text with the letter occurring
    n places afterwards in the alphabet.
    """
    alphabet = string.lowercase
    alpha_size = len(alphabet)
    if abs(n) > alpha_size:
        n = n % alpha_size
    translation_alphabet = alphabet[n:] + alphabet[:n]
    translation_table = string.maketrans(alphabet + alphabet.upper(), \
                                             translation_alphabet + \
                                             translation_alphabet.upper())
    return text.translate(translation_table)

def rotations(text):
    """Returns all possible rotations of the given text in the English
    alphabet.
    """
    return [rotation(text, n) for n in range(1, len(string.lowercase))]
    
def words(sentence):
    return re.split("\s+", sentence)

def translation(problem, corpus):
    """Given a piece of text that has undergone the rotation cipher, figures
    out what the most likely translation is and returns it.
    """
    return argmax(rotations(problem), corpus.Psentence)

def main():
    corpus = Corpus(words(open(CORPUS_FILE, "r").read()))
    print translation(PROBLEM, corpus)

if __name__ == "__main__": main()
