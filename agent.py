from random import randint

class Agent:
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.text = simulation.text[:]

    def read_word(self, word, line):
        mutated_word = self.mutate_word(word, line)
        if mutated_word in self.simulation.embeddings:
            return mutated_word
        else:
            return word

    def write_word(self, word):
        if word not in self.simulation.embeddings: return word
        similar_word, similarity = self.closest_word(word)
        return similar_word if similarity > 0.9 else word

    def read(self, text):
        read_text = []
        for line in text:
            read_line = []
            joined_line = " ".join(line)
            for word in line:
                
                read_line.append(self.read_word(word, joined_line))
            read_text.append(read_line)
        self.text = read_text

    def write(self):
        written_text = []
        for line in self.text:
            written_line = []
            for word in line:
                written_line.append(self.write_word(word))
            written_text.append(written_line)
        return written_text

    def closest_word(self, word):
        return self.simulation.embeddings.most_similar(positive=[word], topn=1)[0]

    def mutate_word(self, word, line):
        mutated_index = randint(0, len(word) - 1)
        new_letter = line[randint(0, len(line) - 1)]
        new_word = word[:mutated_index] + new_letter + word[mutated_index + 1:]
        return new_word.replace(' ', '')
