import imp
from antlr4.tree.Tree import TerminalNodeImpl
from Global import global_constants

def is_terminal_node(node) -> bool:
    return isinstance(node, TerminalNodeImpl)

def evaluate_terminal_children(nodes) -> list[bool]:
    return list(map(lambda node: is_terminal_node(node), nodes))
            
def get_no_terminal_indexes(nodes: list[bool]) -> list[int]:
    return [index for index, value in enumerate(nodes) if not value]

def some_error_type(types: list[str]) -> bool:
    return any(map(lambda type: type == global_constants.results_types.ERROR_TYPE, types))