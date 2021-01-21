from agent import Agent
from random import choice, random
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from os import cpu_count


class Simulation:

    def __init__(self, text, embeddings, params):
        self.text = text
        self.embeddings = embeddings
        self.params = params
        self.population = [Agent(self) for _ in range(params.population_size)]

    def run(self, num_generations):
        for _ in tqdm(range(num_generations), desc="Generations"): self.single_generation()

    def single_generation(self):
        # For each agent, we choose a source manuscript, read it, and then write our own copy
        with ThreadPoolExecutor(max_workers = cpu_count()) as executor:
            results = executor.map(self.simulate_agent, range(len(self.population)))

    def simulate_agent(self, index):
        agent = self.population[index]
        chosen_source = choice(self.population)
        agent.read(chosen_source)
        agent.write()

    def save_result(self, url):
        for agent_num in range(len(self.population)):
            agent = self.population[agent_num]   
            with open(url + "/agent_%d.txt" % agent_num, 'w', encoding='utf8') as f:
                lines  = [" ".join(line) for line in agent.text]
                f.write("\n".join(lines))

    def sample_range(self, number_range):
        return random() * (number_range[1] - number_range[0]) + number_range[0]

    def sample_memory(self):
        return self.sample_range(self.params.agent_memory)

    def sample_influence(self):
        return self.sample_range(self.params.agent_influence)

    def sample_arrogance(self):
        return self.sample_range(self.params.agent_arrogance)

    def sample_vocabulary(self):
        return self.sample_range(self.params.agent_vocabulary)
