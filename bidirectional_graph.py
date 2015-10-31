import re
import string

# TODO choose between isinstance and .__class__ equality check
# TODO add match field to node and edge so that you can get it back on inclusion check
# TODO return node from add_node

class BidirectionalGraph:

    def __init__(self):
        self.nodes = set()

    def __str__(self):
        return str(self.nodes)

    def add_node(self, node):
        # if node.__class__ == BDNode and node not in self.nodes:
        #     self.nodes.add(node)
        #     return True
        # return False
        if node.__class__ == BDNode:
            if node in self.nodes:
                return node.__match
            else:
                # this node does not exist; add to self.nodes, return the node
                self.nodes.add(node)
                return node

    def add_node_with_value(self, value):
        return self.add_node(BDNode(value))

    def add_edge(self, source_node, dest_node):
        if isinstance(source_node, BDNode) and isinstance(dest_node, BDNode):
            # both nodes are confirmed as BDNodes
            if source_node not in self.nodes:
                # source_node hasn't been added yet
                self.add_node(source_node)
            if dest_node not in self.nodes:
                # dest_node hasn't been added yet
                self.add_node(dest_node)
            edge = BDEdge(source_node, dest_node)
            source_node.add_edge(edge, 'dest')
            dest_node.add_edge(edge, 'source')
            return True
        return False

    # def add_edge_with_values(self, source_value, dest_value):
        #do something eventually


class BDNode:

    def __init__(self, value):
        self.value = value
        self.dest_edges = set()
        self.source_edges = set()
        self.count = 1
        self.__match = None

    def __str__(self):
        ret = str(self.value)
        ret += '\nDest Edges:\n'
        for edge in self.dest_edges:
            ret += '\t' + str(edge) + '\n'
        ret += 'Source Edges:\n'
        for edge in self.source_edges:
            ret += '\t' + str(edge) + '\n'
        return ret

    def __eq__(self, other):
        if isinstance(other, BDNode):
            match = other.value == self.value
            # Trick to get the already existing node from a set when checking
            # for inclusion
            if match:
                self.__match = other
            return match
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def add_dest_edge(self, edge):
        if isinstance(edge, BDEdge) and edge not in self.dest_edges:
            self.dest_edges.add(edge)
            return True
        return False

    def add_source_edge(self, edge):
        if isinstance(edge, BDEdge) and edge not in self.source_edges:
            self.source_edges.add(edge)
            return True
        return False

    def add_edge(self, edge, _type):
        if isinstance(edge, BDEdge):
            if _type == 'source' and self.add_source_edge(edge):
                return True
            elif _type == 'dest' and self.add_dest_edge(edge):
                return True
            else:
                return False
        return False

    def get_in_degree(self):
        return len(self.source_edges)

    def get_out_degree(self):
        return len(self.dest_edges)

    def get_degree(self, _type):
        if _type == 'in':
            return self.get_in_degree
        elif _type == 'out':
            return self.get_out_degree
        else: return None

class BDEdge:

    def __init__(self, source_node, dest_node):
        self.source = source_node
        self.dest = dest_node
        self.count = 1
        self.__match = None

    def __str__(self):
        return str(self.source.value) + '-' + str(self.count) + '->' + str(self.dest.value)

    def __hash__(self):
        hs = str(self.source) + str(self.dest)
        return hash(hs)

    def __eq__(self, other):
        if other.__class__ == BDEdge:
            return self.source == other.source and self.dest == other.dest
        return False

    def increment_count(self):
        self.count += 1


if __name__ == '__main__':
    # graph = BidirectionalGraph()
    # source_node = BDNode('source')
    # dest_node = BDNode('dest')
    # other_source = BDNode('source')
    # graph.add_node(source_node)
    # graph.add_node(dest_node)
    # graph.add_node(other_source)
    # graph.add_edge(source_node, dest_node)
    # print source_node
    # print dest_node
    # print graph

    word_graph = BidirectionalGraph()
    passage = open('robin-passage.txt', 'r').read()
    split_passage = passage.translate(string.maketrans(string.punctuation, ' '*len(string.punctuation))).split()
    # for item in passage.split():
    #     word_graph.add_node_with_value(item.lower())
    previous_node = None
    for i in range(len(split_passage)):
        item = split_passage[i].lower()
        node = BDNode(item)
        if word_graph.add_node(node):
            if i > 0:
                # only add edges from current note to the previous node, and
                # from the previous node to the current node Because of this,
                # we can only do this after
                edge = BDEdge(previous_node, node)
                previous_node.add_dest_edge(edge)
                node.add_source_edge(edge)
            previous_node = node

    print len(split_passage)
    print len(word_graph.nodes)
    for node in word_graph.nodes:
        print node
