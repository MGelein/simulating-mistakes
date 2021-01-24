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
        self.population = [Agent(self, i) for i in range(params.population_size)]

    def run(self, num_generations):
        for _ in tqdm(range(num_generations), desc="Generations"): self.single_generation()

    def single_generation(self):
        # We map every agent's loop to a single thread, this makes the simulation a LOT faster
        # with ThreadPoolExecutor(max_workers = cpu_count()) as executor:
        #     results = executor.map(self.simulate_agent, range(len(self.population)))
        for i, agent in enumerate(self.population): self.simulate_agent(i)
        for agent in self.population: agent.make_canonical()

    def simulate_agent(self, index):
        # For each agent, we choose a source manuscript, read it, and then write our own copy
        agent = self.population[index]
        chosen_source = self.choose_source(agent)
        agent.read(chosen_source)
        agent.write()

    def choose_source(self, agent):
        possible_sources = []
        for source in self.population:
            diff = abs(source.position - agent.position)
            influence = source.influence * self.params.simulation_space
            if influence > diff: possible_sources.append(source)
        srt = sorted(possible_sources, key=lambda x: x.influence)
        print('--')
        for s in srt: print(s.influence)
        return srt[0]

    def save_result(self, url):
        for agent_num in range(len(self.population)):
            agent = self.population[agent_num]   
            with open(url + "/agent_%d.txt" % agent_num, 'w', encoding='utf8') as f:
                lines  = [" ".join(line) for line in agent.canonical_text]
                f.write("\n".join(lines))

    def sample_position(self, number):
        rnd_value = self.sample_range((0, self.params.simulation_space))
        div_value = (self.params.simulation_space / self.params.population_size) * number
        return rnd_value * self.params.dist_randomness + div_value * (1 - self.params.dist_randomness)

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
