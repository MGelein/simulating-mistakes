from agent import Agent
from random import choice
from tqdm import tqdm

class Simulation:

    def __init__(self, text, embeddings, params):
        self.text = text
        self.embeddings = embeddings
        self.params = params
        self.population = [Agent(self) for _ in range(params['population_size'])]

    def run(self, num_generations):
        for _ in tqdm(range(num_generations), desc="Generations"): self.single_generation()

    def single_generation(self):
        available_agents = self.population[:]
        for agent in self.population:
            available_agents.remove(agent)
            if agent in available_agents:
                written_text = agent.write()
                reader_agent = choice(available_agents)
                reader_agent.read(written_text)
                available_agents.remove(reader_agent)

    def save_result(self, url):
        for agent_num in range(len(self.population)):
            agent = self.population[agent_num]   
            with open(url + "/agent_%d.txt" % agent_num, 'w', encoding='utf8') as f:
                lines  = [" ".join(line) for line in self.text]
                f.write("\n".join(lines))