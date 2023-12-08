import json
import os.path

def save(experiment, file_name):
  with open(f"ExperimentData/{file_name}.json", 'w') as fp:
    json.dump(experiment, fp)

def load(file_name):
  with open(f"ExperimentData/{file_name}.json", 'r') as fp:
    experiment = json.load(fp)
    return experiment
  
def saveGraph(experiment, file_name):
  pass

def loadGraph(file_name):
  pass

def exists(file_name):
  return os.path.isfile(f"ExperimentData/{file_name}.json")

