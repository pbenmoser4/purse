import re
import string

# TODO choose between isinstance and .__class__ equality check
# TODO add match field to node and edge so that you can get it back on inclusion check
# TODO return node from add_node

class BidirectionalGraph:

    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return str(self.nodes)

    def add_node(self, node):
        if node.__class__ == BDNode:
            if node.value in self.nodes:
                return self.nodes[node.value]
            else:
                # this node does not exist; add to self.nodes, return the node
                self.nodes[node.value] = node
                return node
        return None

    def add_node_with_value(self, value):
        return self.add_node(BDNode(value))

    def add_edge(self, source_node, dest_node):
        # Holders for the source node and the destination node. We use these
        # holder variables so that if the graph already contains the node, we
        # can refer to the already existing node, rather than the node that was
        # passed into the methodd
        source = None
        dest = None
        if isinstance(source_node, BDNode) and isinstance(dest_node, BDNode):
            # both nodes are confirmed as BDNodes
            if source_node.value not in self.nodes or dest_node.value not in self.nodes:
                # if either of the nodes haven't been added, return None
                return None
            edge = BDEdge(source_node, dest_node)
            source_node.add_edge(edge, 'dest')
            dest_node.add_edge(edge, 'source')
            return True
        return None

    # def add_edge_with_values(self, source_value, dest_value):
        #do something eventually


class BDNode:

    def __init__(self, value):
        self.value = value
        # self.dest_edges = set()
        # self.source_edges = set()
        self.out_edges = {}
        self.in_edges = {}
        self._match = None

    def __str__(self):
        ret = str(self.value)
        ret += '\nOut Edges:\n'
        for key in self.out_edges:
            ret += '\t' + str(self.out_edges[key]) + '\n'
        ret += 'In Edges:\n'
        for key in self.in_edges:
            ret += '\t' + str(self.in_edges[key]) + '\n'
        return ret

    def __eq__(self, other):
        if isinstance(other, BDNode):
            return other.value == self.value
        return False

    def __hash__(self):
        return hash(self.value)

    def add_out_edge(self, edge):
        if isinstance(edge, BDEdge):
            if edge.value in self.out_edges:
                return self.out_edges[edge.value]
            else:
                self.out_edges[edge.value] = edge
                return edge
        return None

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
        self.value = str(source_node) + str(dest_node)
        self.source = source_node
        self.dest = dest_node
        self.count = 1
        self._match = None

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
