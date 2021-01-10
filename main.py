print("Handeling imports...")
import sys
from gensim.models import KeyedVectors
from simulation import Simulation
from util import similar_looking_word, set_edit_dist_function
from configparser import ConfigParser

def show_help():
    print("""
    Welcome to the text transmission simulation tool, you can use the following arguments:
    --settings      -s      .ini settings file location
    """)
    exit()

def load_lines(url):
    lines = []
    with open(url, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.replace('\r', '').replace('\n', '')
            if len(line) < 1: continue
            lines.append(line.split(' '))
    return lines

def parse_ini(url):
    config = ConfigParser()
    config.read(url)
    params = {}
    params['embeddings'] = config.get('simulation', 'embeddings')
    params['input'] = config.get('simulation', 'input')
    params['output'] = config.get('simulation', 'output_dir')
    params['population_size'] = config.getint('simulation', 'population_size')
    params['generations'] = config.getint('simulation', 'generations')
    params['edit_function'] = config.get('simulation', 'edit_function')
    return params

def parse_params():
    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if i + 1 < len(sys.argv): next_arg = sys.argv[i + 1]
        else: next_arg = None

        if arg in ('--settings', '-s'):
            return parse_ini(next_arg)

def start_simulation(params):
    print("Loading embeddings from: %s" % params['embeddings'])
    embeddings = KeyedVectors.load(params['embeddings'])
    print("Loading text from: %s" % params['input'])
    lines = load_lines(params['input'])
    set_edit_dist_function(params['edit_function'])

    simulation = Simulation(lines, embeddings, params)
    simulation.run(params['generations'])
    simulation.save_result(params['output'])

if __name__ == '__main__':

    if len(sys.argv) < 1:
        show_help()
    else:
        params = parse_params()
    if params is None: show_help()

    start_simulation(params)