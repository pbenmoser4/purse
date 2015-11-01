import re
import string

# TODO choose between isinstance and .__class__ equality check

class BidirectionalGraph:

    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return str(self.nodes)

    def add_node(self, node):
        # if node.__class__ == BDNode:
        if isinstance(node, BDNode):
            if node.value in self.nodes:
                return self.nodes[node.value]
            else:
                # this node does not exist; add to self.nodes, return the node
                self.nodes[node.value] = node
                return node
        return None

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

    # Search Algs

    def depth_first_search(self, search, start):
        """ Depth first search of the graph, starting at start node """
        if start in self.nodes and search in self.nodes:
            # We know that the starting point and the item we're searching for
            # are both in the graph. Now we start looking beeeoooootch
            print 'something'
        else:
            return None

    def breadth_first_search(self, search, start):
        """ Breadth first search of the graph, starting at start ndoe """


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
        if isinstance(edge, BDEdge):
            if edge.value in self.edges:
                ret = self.edges[edge.value]
                ret.increment_count()
                return ret
            else:
                self.edges[edge.value] = edge
                return edge
        return None

    def get_degree(self):
        return len(self.edges)

    def get_neighbors(self):
        neighbors = set()
        for key in self.edges:
            neighbors.add(self.edges[key].dest)
        return neighbors


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

# Short reporting function to show first degree neighbors of the given word
def report_word(graph, word, min_count):
    if word in graph.nodes:
        node = graph.nodes[word]
        print node
        for key in node.edges:
            edge = node.edges[key]
            if edge.count > min_count:
                print edge


if __name__ == '__main__':

    word_graph = BidirectionalGraph()
    passage = open('robin.txt', 'r').read()
    split_passage = passage.translate(string.maketrans(string.punctuation, ' '*len(string.punctuation))).split()

    previous_node = None
    for i in range(len(split_passage)):
        item = split_passage[i].lower()
        _node = BDNode(item)
        node = word_graph.add_node(_node)
        if i > 0:
            edge = BDEdge(previous_node, node)
            previous_node.add_edge(edge)
        previous_node = node

    print len(split_passage)
    print len(word_graph.nodes)

    report_word(word_graph, 'robin', 0)
