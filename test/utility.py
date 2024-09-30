"""
Helper functions used to help with testing
"""
import pathlib
import random

RESOURCE_DIRECTORY = pathlib.Path(__file__).parent / "resources"
RANDOM_VALUE_SEED = 987654321

def apply_seed():
    random.seed(RANDOM_VALUE_SEED)

