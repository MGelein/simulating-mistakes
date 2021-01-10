import numpy as np

def levenshtein(word_a, word_b):
    max_a = len(word_a) + 1
    max_b = len(word_b) + 1
    matrix = np.zeros((max_a, max_b), dtype='int8')
    for i in range(max_a): matrix[i, 0] = i
    for i in range(max_b): matrix[0, i] = i
    
    for i in range(max_a):
        for j in range(max_b):
            if word_a[i - 1] == word_b[j - 1]:
                matrix[i, j] = matrix[i - 1, j - 1]
            else:
                matrix[i, j] = min(matrix[i - 1, j - 1] + 1, matrix[i, j - 1] + 1, matrix[i - 1, j] + 1)

    return matrix[max_a - 1, max_b - 1]

if __name__ == '__main__':
    """This is a simple test to see if this module actually works"""
    print(levenshtein('cat', 'cat'))