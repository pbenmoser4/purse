import re
import string
import os

class Digraph:

    def __init__(self):
        """
        Initialize the directional graph

        This is going to be a purely adjacency list representation. Built for
        use with d3.js
        """

        # map of nodes to neighbors
        self.nodes = {}


    def get_nodes(self):
        """
        Get the nodes of this graph

        @rtype:     list
        @return:    A list of all the nodes in this graph
        """

        return list(self.nodes.keys())

    def get_neighbors(self, node):
        """
        Get the neighbors of the given node

        @type   node: DNode
        @param  node: The node for which we're finding neighbors

        @rtype:     list
        @return:    A list of nodes neighboring the given node
        """

        return self.nodes[node]

    def get_edges(self):
        """
        Get the edges of the current graph

        @rtype:     list
        @return:    A list of touples representing the edges of the graph
        """

        return [edge for edge in self._edges()]

    def _edges(self):
        """
        Creates a Generator for the edges in the graph
        """
        for node, neighbors in self.nodes.iteritems():
            for neighbor in neighbors:
                yield (node, neighbor)

    def has_node(self, node):
        """
        Determine whether the given node is in the graph

        @type   node: node
        @param  node: The node to check for inclusion

        @rtype:     boolean
        @return:    A boolean representing whether the given node is in the graph
        """

        return node in self.nodes

    def has_edge(self, edge):
        """
        Determine whether the given edge is a part of the graph

        @type   edge: touple
        @param  edge: The edge to check for inclusion

        @rtype:     boolean
        @return:    A boolean representing whether the given edge is in the graph
        """

        return edge in self.get_edges()

    def add_node(self, node):
        """
        Add the given node to the graph, if it is not a part of it already

        @type   node: node
        @param  node: The node to add to the graph
        """

        if self.has_node(node):
            raise Exception
        else:
            self.nodes[node] = []

    def add_edge(self, edge):
        """
        Add the given edge to the graph, if it is not a part of it already

        @type   edge: touple
        @param  edge: The edge to add to the graph
        """
        u, v = edge

        for n in [u,v]:
            if n not in self.nodes:
                raise Exception

        if v in self.nodes[u]:
            raise Exception
        else:
            self.nodes[u].append(v)

    def del_node(self, node):
        """
        Remove the given node from the graph, if it is in the graph, and then
        remove its edges

        @type   node: nodes
        @param  node: The node to delete from the graph
        """

        if self.has_node(node):
            del self.nodes[node]
        else:
            raise Exception

    def del_edge(self, edge):
        """
        Remove the given edge from the graph, it is in the graph

        @type   edge: touple
        @param  edge: The edge to delete from the graph
        """
        u, v = edge

        if self.has_node(u) and self.has_node(v):
            if v in self.nodes[u]:
                self.nodes[u].remove(v)
        else:
            raise Exception

    def get_node_order(self, node):
        """
        Get the degree of the given node, if it is in the graph

        @type   node: node
        @param  node: The node to get the order for

        @rtype:     number
        @return:    The order of the given node
        """

        if self.has_node(node):
            return len(self.nodes[node])
        else:
            raise Exception

if __name__ == "__main__":
    dg = Digraph()
    dg.add_node('hello')
    dg.add_node('goodbye')
    print dg.nodes
    dg.add_edge(('hello', 'goodbye'))
    print dg.nodes
