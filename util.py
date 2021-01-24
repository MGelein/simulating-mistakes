import numpy as np
from random import randint, choice
from tqdm import tqdm

matrix_size = 50
matrix = np.zeros((matrix_size, matrix_size), dtype='int8')
similar_words = {}

def similar_looking_word(word, vocab):
    global edit_dist_fn, similar_words
    if word in similar_words: return choice(similar_words[word])
    
    options = []
    word_len = len(word)
    for other_word in vocab:
        len_diff = len(other_word) - word_len
        if len_diff > 1 or len_diff < -1: continue
        if edit_dist_fn(other_word, word, len_diff) > 1: continue
        else: options.append(other_word)
    if len(options) == 0: 
        similar_words[word] = [word]
        return word
    similar_words[word] = options
    return choice(options)
    
def closest_word(word, embedding):
    return choice(embedding.most_similar(positive=[word], topn=10))

def levenshtein(word_a, word_b, diff_len):
    global matrix
    max_a = len(word_a) + 1
    max_b = len(word_b) + 1
    matrix[:] = 0
    for i in range(max_a): matrix[i, 0] = i
    for i in range(max_b): matrix[0, i] = i
    
    for i in range(max_a):
        for j in range(max_b):
            if word_a[i - 1] == word_b[j - 1]:
                matrix[i, j] = matrix[i - 1, j - 1]
            else:
                matrix[i, j] = min(matrix[i - 1, j - 1] + 1, matrix[i, j - 1] + 1, matrix[i - 1, j] + 1)

    return matrix[max_a - 1, max_b - 1]

def modified_hamming(word_a, word_b, diff_len):
    errors = abs(diff_len)
    for letter_a, letter_b in zip(word_a, word_b):
        if letter_a != letter_b: errors += 1
        if errors > 1: return 2
    return errors
edit_dist_fn = modified_hamming

def set_edit_dist_function(name):
    global edit_dist_fn
    if name == 'levenshtein': edit_dist_fn = edit_dist_fn
    else: edit_dist_fn = modified_hamming