import json
import argparse

def read_config():
    try:
        with open('config.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('[ERROR] : Archivo de configuración no encontrado.')
    except:
        return {}
    
def get_section(name):
    try:
        config = read_config()
        return config['sections'].get(name)
    except:
        return ''
    
def validate_condition(input: str) -> bool:
    return input in ['y','Y','s','S','n','N']

def affirmative_condition(input: str) -> bool:
    return input in ['y','Y','s','S']

def validate_file_type(input: int) -> bool:
    return input in [0,1]

def validate_time(input: int) -> bool:
    return input >= 0 and input <= 60

def reject_negatives(val):
    val = int(val)
    if val < 0:
        raise argparse.ArgumentTypeError(f'Invalid value: {val} The value must be non-negative.')
    return val