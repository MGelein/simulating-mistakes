import numpy as np
from tqdm import tqdm
from numpy import dot
from numpy.linalg import norm

def term_frequency(texts):
    words_collection = []

    # Split each text into list of words
    for text in texts:
        words_collection.append(text.split(' '))
    
    # Make a set of all unique terms in every doc
    terms = set()
    for words in words_collection:
        for word in words: terms.add(word)

    # Create the empty vectors for every text
    terms_collection = []
    for _ in words_collection:
        terms_collection.append(np.zeros(len(terms)))

    # Count every word in every text
    for i, term in enumerate(terms):
        for words, text_terms in zip(words_collection, terms_collection):
            text_terms[i] = count_words(words, term)

    return terms_collection
    
def cosine_similarity(terms_a, terms_b):
    return dot(terms_a, terms_b) / (norm(terms_a) * norm(terms_b))

def count_words(words, term):
    total = 0
    for word in words:
        if word == term:
            total += 1
    return total

def load_textfile(url):
    lines = []
    try:
        with open(url + ".txt", 'r', encoding='utf8') as f:
            for line in f.readlines():
                lines.append(line.replace('\n', ''))
    except:
        pass
    return " ".join(lines)

files = []
for i in range(5):
    files.append(load_textfile('agent_%d' % i))
tfs = term_frequency(files)

print(cosine_similarity(tfs[0], tfs[1]))