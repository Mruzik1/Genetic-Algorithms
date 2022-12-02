import numpy as np
import matplotlib.pyplot as plt
from .node import Node


class NodesGenerator:
    # self.__axis_nodes - points (nodes) with random x and y
    def __init__(self, count: int, saved_axis = False):
        if not saved_axis:
            x = np.random.choice(range(count), count, replace=False)
            y = np.random.choice(range(count), count, replace=False)
            self.__axis_nodes = np.array([x, y]).T
            
            self.__generate_file('./data/distances.txt')
            self.__save_axis('./data/axis.txt')

        else:
            self.__axis_nodes = self.__read_from_file('./data/axis.txt')
    

    # generates a file with distances between the nodes
    def __generate_file(self, path: str):
        fp = open(path, 'w')
        for i, n1 in enumerate(self.__axis_nodes):
            for j, n2 in enumerate(self.__axis_nodes[i+1:]):
                fp.write(f'{i+1} {i+j+2} {int(np.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2))}\n')
        fp.close()


    # generates a file with axis
    def __save_axis(self, path: str):
        fp = open(path, 'w')
        for x, y in self.__axis_nodes:
            fp.write(f'{x} {y}\n')
        fp.close()


    # reads nodes or axis from the generated file, data preprocess
    def __read_from_file(self, path: str) -> np.ndarray:
        with open(path) as fp:
            raw = np.array([e.split() for e in fp.read().split('\n') if len(e) != 0]).astype(object)
            raw = raw.astype(np.int32)
        return raw


    # returns nodes list (consisting of the Node objects)
    def get_nodes_list(self, path: str) -> list:
        nodes_raw = self.__read_from_file(path)
        return [Node(i, nodes_raw) for i in range(1, nodes_raw.T[:2].max()+1)]


    # counts total cost of the way (it is also a fitness function)
    def total_cost(self, nodes: list) -> int:
        total_cost = 0
        for i in list(range(1, len(nodes))) + [0]:
            total_cost += nodes[i].get_distance(nodes[i-1])
        return total_cost
    

    # visualization using matplotlib
    def draw_path(self, nodes: list):
        plt.scatter(self.__axis_nodes[:, 0], self.__axis_nodes[:, 1])

        for i in range(0, len(nodes)):
            node, prev_node = nodes[i].get_number()-1, nodes[i-1].get_number()-1
            x1, x2 = self.__axis_nodes[node][0], self.__axis_nodes[prev_node][0]
            y1, y2 = self.__axis_nodes[node][1], self.__axis_nodes[prev_node][1]
            plt.plot((x1, x2), (y1, y2), color='r')
        
        plt.show()