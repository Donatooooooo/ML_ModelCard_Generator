from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import json, math, os

PATH = "docs/src/Templates"

def convertTime(unixTime):
    """
    Convert Unix time in Human time.
    """
    return datetime.fromtimestamp(unixTime/1000.0).strftime('%H:%M:%S %Y-%m-%d')

def extractInfoTags(tags):
    """
    Extract relevant info from tags tracked in MLflow experiment.
    """
    data_tags = json.loads(tags.get('mlflow.log-model.history', ''))
    flavors = data_tags[0]['flavors']
    py_version = flavors['python_function']['python_version']
    lib = str([key for key in flavors.keys() if key != 'python_function'][0])
    lib_version = flavors[lib].get(f'{lib}_version')
    return py_version, lib, lib_version

def extratDatasetName(data):
    """
    Extract a Dataset tracked in a MLflow experiment.
    """

    dataString = str(data)
    start = dataString.find("name='") + len("name='")
    end = dataString.find("'", start)
    return dataString[start:end]

def getPath(data):
    """
    Build a path for saving Model Cards file.
    """
    
    part = data.get("modelName").replace(" ", "")
    fname = f"{part}_v{data.get('version')}.md"
    root = os.path.abspath(os.path.join(os.path.join(
        os.path.dirname(__file__), '..'), '..'))
    ModelCards_directory = os.path.join(root, 'modelcards')
    path = os.path.join(ModelCards_directory, fname)
    return path, fname

def templateRender(template, data):
    """
    Render a template.
    """
    
    environment = Environment(loader = FileSystemLoader(PATH))
    template = environment.get_template(template)
    return template.render(data)

def refine(metrics):
    """
    Refine metrics retrieved from a MLflow's experiment.
    """
    refined = {}
    factor = 10 ** 5
    for key, value in metrics.items():
        refined[key] = math.trunc(value * factor) / factor
    return refined
