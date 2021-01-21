import sys
from configparser import ConfigParser
from types import SimpleNamespace

def parse_range(s):
    parts = s.split(":")
    if len(parts) < 2: return float(s)
    minimum = float(parts[0])
    maximum = float(parts[1])
    return (minimum, maximum)

def parse_ini(url):
    config = ConfigParser()
    config.read(url)
    params = {}
    params['embeddings'] = config.get('files', 'embeddings')
    params['input'] = config.get('files', 'input')
    params['output'] = config.get('files', 'output_dir')
    params['population_size'] = config.getint('simulation', 'population_size')
    params['iterations'] = config.getint('simulation', 'iterations')
    params['edit_function'] = config.get('simulation', 'edit_function')
    params['dist_randomness'] = config.getfloat('simulation', 'distribution_randomness')
    params['simulation_space'] = config.getint('simulation', 'space')
    params['agent_arrogance'] = parse_range(config.get('agent', 'arrogance'))
    params['agent_influence'] = parse_range(config.get('agent', 'influence'))
    params['agent_memory'] = parse_range(config.get('agent', 'memory'))
    params['agent_vocabulary'] = parse_range(config.get('agent', 'vocabulary'))
    return SimpleNamespace(**params)

def parse_params():
    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if i + 1 < len(sys.argv): next_arg = sys.argv[i + 1]
        else: next_arg = None
 
        if arg in ('--settings', '-s'):
            return parse_ini(next_arg)
