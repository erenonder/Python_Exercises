
from collections import OrderedDict
from enum import Enum

class State(Enum):

    visited = 1
    unvisited = 2
    visiting = 3

class Node:

    def __init__(self, num):

        self.num = num
        self.status = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        string_rep = str(self.num) + ' ' + self.status.name
        return string_rep

class Graph():

    def __init__(self):

        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):

        node = Node(num)
        self.nodes[num] = node

        # return node

    def add_edge(self, src, dest, weight):

        if src not in self.nodes:

            self.add_node(src)

        if dest not in self.nodes:

            self.add_node(dest)

        self.nodes[src].adjacent[self.nodes[dest]] = weight


g = Graph()

g.add_edge(0, 1, 5)

print(g.nodes)
