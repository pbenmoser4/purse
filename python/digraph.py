import re
import string
import os

class Digraph:

    def __init__(self):
        """
        Initialize the directional graph
        """

        """
        The nodes attribute is a map of nodes to their neighbors. Instead of an
        array of neighbors for each node key, there will be a dictionary, with
        the "node" key mapping to the neighboring node, and the "edge" key
        mapping to the associated edge object, along with attributes
        """
        self.nodes = {}

    #TODO def get_edge(source, dest) checks for the source key, and then checks for dest, returns associated edge if available

class Node:

    def __init__(self, attrs):
        """
        Initialize a node to be added to the directional graph

        @type attrs: dictionary
        @param attrs: A dictionary of attributes to be associated with the node
        """

        # The value associated with this node
        self.val = attrs['val']

        # The other attributes of this node
        _attrs = dict(attrs)
        del _attrs['val']
        self.attrs = _attrs

class Edge:

    def __init__(self):
        """

        """
