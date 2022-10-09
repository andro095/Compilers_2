from Quadruples import Quadruples, make_quadruple

class InterCode:
    def __init__(self):
        self.__quadruples = Quadruples()
        self.temps = 0
        self.if_count = 0
        self.while_count = 0
        self.let_count = 0
        
    def gen_label(self, flow: str = None, label: str = None) -> str:
        """ 
        Función que genera un label.
        """
        if flow == 'if':
            self.if_count += 1
            return f'if{self.if_count}'
        elif flow == 'while':
            self.while_count += 1
            return f'while{self.while_count}'
        elif flow == 'let':
            self.let_count += 1
            return f'let{self.let_count}'
        elif label:
            return label
        else:
            raise Exception('No se puede generar un label.')