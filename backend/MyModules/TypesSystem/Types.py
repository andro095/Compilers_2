import json
from .Constants import types_sys_constants

class Types:
    def __init__(self):
        self.individual_types = {}
        self.complex_types = {}
        self.read_individual_types()
        self.read_complex_types()

    def read_individual_types(self):
        with open(types_sys_constants.INDIVIDUAL_RULES, 'r') as f:
            self.individual_types = json.load(f)

    def read_complex_types(self):
        with open(types_sys_constants.COMPLEX_RULES, 'r') as f:
            self.complex_types = json.load(f)


types_sys = Types()
