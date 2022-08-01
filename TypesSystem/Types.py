import json
from pprint import pprint


class Types:
    def __init__(self):
        self.individual_types = {}
        self.complex_types = {}
        self.read_individual_types()
        self.read_complex_types()

    def read_individual_types(self):
        with open('./TypesSystem/Rules/individual_rules.json', 'r') as f:
            self.individual_types = json.load(f)
        print("Individual Types:\n")
        pprint(self.individual_types)

    def read_complex_types(self):
        with open('./TypesSystem/Rules/complex_rules.json', 'r') as f:
            self.complex_types = json.load(f)

        print("Complex Types:\n")
        pprint(self.complex_types)


types_sys = Types()
