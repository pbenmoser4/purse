import re
import string

# TODO choose between isinstance and .__class__ equality check

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
        # passed into the method
        source = None
        dest = None
        if isinstance(source_node, BDNode) and isinstance(dest_node, BDNode):
            # both nodes are confirmed as BDNodes
            if source_node.value not in self.nodes or dest_node.value not in self.nodes:
                # if either of the nodes haven't been added, return None
                return None

            source = self.nodes[source_node.value]
            dest = self.nodes[dest_node.value]
            edge = BDEdge(source, dest)
            return source.add_edge(edge)

        return None

class BDNode:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __str__(self):
        ret = str(self.value)
        return ret

    def __eq__(self, other):
        if isinstance(other, BDNode):
            return other.value == self.value
        return False

    def __hash__(self):
        return hash(self.value)

    def add_edge(self, edge):
        print 'adding edge'
        if isinstance(edge, BDEdge):
            print 'input is a BDEdge'
            if edge.value in self.edges:
                print 'the edge exists'
                ret = self.edges[edge.value]
                ret.increment_count()
                return ret
            else:
                print 'the edge does not exist'
                self.edges[edge.value] = edge
                return edge
        return None

    def get_degree(self, _type):
        return len(self.edges)

class BDEdge:

    def __init__(self, source_node, dest_node):
        self.value = str(source_node) + str(dest_node)
        self.source = source_node
        self.dest = dest_node
        self.count = 1

    def __str__(self):
        return str(self.source.value) + '-' + str(self.count) + '->' + str(self.dest.value)

    def __hash__(self):
        hs = str(self.source.value) + str(self.dest.value)
        return hash(hs)

    def __eq__(self, other):
        if other.__class__ == BDEdge:
            return self.source == other.source and self.dest == other.dest
        return False

    def increment_count(self):
        self.count = self.count + 1


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
                previous_node.add_out_edge(edge)
                node.add_in_edge(edge)
            previous_node = node

    print len(split_passage)
    print len(word_graph.nodes)
    for key in word_graph.nodes:
        print word_graph.nodes[key]
