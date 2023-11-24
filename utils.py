import json

def save(experiment, file_name):
  with open(f"ExperimentData/{file_name}.json", 'w') as fp:
    json.dump(experiment, fp)

def load(file_name):
  with open(f"ExperimentData/{file_name}.json", 'r') as fp:
    experiment = json.load(fp)
    return experiment
