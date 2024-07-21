import os 
import yaml
import sys


def _set_environ(name, value):
    github_environ_filename = os.environ['GITHUB_ENV']
    with open(github_environ_filename, 'at') as outfile:
        outfile.write(f"{name} = {value}\n")

file_path = os.environ.get('FILE_PATH')
input_type = os.environ.get('INPUT_TYPE')

with open(file_path,'r') as file:
    data = yaml.safe_load(file)

if input_type in data:
    env_details = data[input_type]
    _set_environ("NAME", env_details.get('name'))
    _set_environ("LOCATION", env_details.get('location'))
    _set_environ("WORK", env_details.get('work'))
    
