from random import choice, random
from util import similar_looking_word

class Agent:
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.canonical_text = simulation.text[:]
        self.written_text = self.canonical_text[:]
        self.remembered_text = self.canonical_text[:]
        self.memory = simulation.sample_memory()
        self.arrogance = simulation.sample_arrogance()
        self.influence = simulation.sample_influence()
        self.vocabulary = simulation.sample_vocabulary()
    
    def skip_line(self, sentences):
        sentence, next_sentence = sentences
        if random.random() < self.arrogance: 
            return [next_sentence]
        
        for word in next_sentence:
            if word in sentence:
                start = sentence.index(word)
                end = next_sentence.index(word)
                return sentence[:start] + next_sentence[end:]

    def substitute_word(self, word):
        if random.random() > self.arrogance and word in self.vocab: 
            return word
        top_ten = self.embeddings.most_similar(positive=[word], topn=10)
        return random.choice(top_ten)

    def mutate_letter(self, word, alphabet):
        rnd_index = random.randint(0, len(word) - 1)
        letter = random.choice(alphabet)
        new_word = word[:rnd_index] + letter + word[rnd_index + 1:]
        if new_word in self.vocab: 
            return new_word
        else:
            return new_word if random.random() < self.arrogance else word

    def read_word(self, word, line):
        
        return word

    def make_canonical(self):
        self.canonical_text = self.written_text

    def write_word(self, word):
        if word not in self.simulation.embeddings: return word
        similar_word, similarity = closest_word(word, self.simulation.embeddings)
        return similar_word if similarity > 0.9 else word

    def read(self, agent):
        read_text = []
        for line in agent.canonical_text:
            read_line = []
            joined_line = " ".join(line)
            for word in line:
                read_line.append(self.read_word(word, joined_line))
            read_text.append(read_line)
        self.remembered_text = read_text

    def write(self):
        write_text = []
        for line in self.remembered_text:
            written_line = []
            for word in line:
                written_line.append(self.write_word(word))
            write_text.append(written_line)
        self.written_text = write_text

