import json
import argparse
import os
    
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
        raise argparse.ArgumentTypeError(f'Valor inválido: {val} El valor debe ser entero.')
    return val