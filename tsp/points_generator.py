import numpy as np
import matplotlib.pyplot as plt
from random import randint
from .node import Node


class NodesGenerator:
    # self.__axis_nodes - points (nodes) with random x and y
    def __init__(self, count: int):
        self.__axis_nodes = np.array([(randint(0, 500), randint(0, 500)) for _ in range(count)])
    
    # generate typical txt file with distances between the nodes
    def generate_distances(self, path: str):
        fp = open(path, 'w')
        for i, n1 in enumerate(self.__axis_nodes):
            for j, n2 in enumerate(self.__axis_nodes[i+1:]):
                fp.write(f'{i+1} {i+j+2} {int(np.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2))}\n')
        fp.close()

    # reads nodes from the generated file, preprocess data 
    def __read_from_file(self, path: str) -> np.ndarray:
        with open(path) as fp:
            nodes_raw = np.array([e.split() for e in fp.read().split('\n') if len(e) != 0]).astype(object)
            nodes_raw = nodes_raw.astype(np.int32)
        return nodes_raw

    # returns nodes dictionary (consisting of the Node objects)
    # {...number_of_node: node...}
    def get_nodes_dict(self, path: str) -> dict:
        nodes_raw = self.__read_from_file(path)
        return {i: Node(i, nodes_raw) for i in range(1, nodes_raw.T[:2].max()+1)}
    
    # visualization using matplotlib
    def draw_algorithm(self, path):
        plt.scatter(self.__axis_nodes[:, 0], self.__axis_nodes[:, 1])

        for i in range(0, len(path)):
            x1, x2 = self.__axis_nodes[path[i]-1][0], self.__axis_nodes[path[i-1]-1][0]
            y1, y2 = self.__axis_nodes[path[i]-1][1], self.__axis_nodes[path[i-1]-1][1]
            plt.plot((x1, x2), (y1, y2), color='r')
        
        plt.show()