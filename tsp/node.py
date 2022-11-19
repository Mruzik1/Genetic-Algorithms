import numpy as np


class Node:
    def __init__(self, number: int, nodes_list: np.ndarray):
        self.__number = number
        self.__distances = self.__init_node(nodes_list[np.where(nodes_list[:, :2] == number)[0]])
    

    # returns a dictionary with following structure:
    # {...number_of_node: distance...}
    def __init_node(self, nodes_list) -> dict:
        nodes_list = [[e[1], e[2]] if e[0] == self.__number else [e[0], e[2]] for e in nodes_list]

        return {e[0]: e[1] for e in nodes_list}


    # returns distance between this node and another (that is got as an argument, could be also a number)
    def get_distance(self, node) -> int:
        if isinstance(node, Node):
            return self.__distances[node.get_number()]
        return self.__distances[node]


    # returns a number of the node
    def get_number(self) -> int:
        return self.__number


    # string representation
    def __str__(self):
        return str(self.__number)