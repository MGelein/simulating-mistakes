import numpy as np
from random import randint, choice
from tqdm import tqdm

matrix_size = 50
matrix = np.zeros((matrix_size, matrix_size), dtype='int8')

def similar_looking_word(word, vocab):
    global edit_dist_fn
    options = []
    for other_word in vocab:
        if abs(len(other_word) - len(word)) > 1: continue
        if edit_dist_fn(other_word, word) > 1: continue
        else: options.append(other_word)
    if len(options) == 0: return word
    return choice(options)
    
def mutate_word(word, line):
    mutated_index = randint(0, len(word) - 1) if len(word) > 1 else 0
    new_letter = line[randint(0, len(line) - 1)]
    new_word = word[:mutated_index] + new_letter + word[mutated_index + 1:]
    return new_word.replace(' ', '')
    
def closest_word(word, embedding):
    return choice(embedding.most_similar(positive=[word], topn=10))

def levenshtein(word_a, word_b):
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

def modified_hamming(word_a, word_b):
    errors = abs(len(word_a) - len(word_b))
    for letter_a, letter_b in zip(word_a, word_b):
        if letter_a != letter_b: errors += 1
        if errors > 1: return 2
    return errors
edit_dist_fn = modified_hamming

def set_edit_dist_function(name):
    global edit_dist_fn
    if name == 'levenshtein': edit_dist_fn = edit_dist_fn
    else: edit_dist_fn = modified_hamming