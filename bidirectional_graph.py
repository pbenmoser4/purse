class BidirectionalGraph:

    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        if type(node) is BDNode:
            self.nodes.add(node)
            return True
        return False

    def add_node_with_value(self, value):
        if value == None:
            return False
        self.nodes.add(BDNode(value))
        return True

    def add_edge(self, source_node, dest_node):


class BDNode:

    def __init__(self, value):
        self.value = value
        self.next = set()
        self.prev = set()
        self.count = 1

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if type(other) is BDNode:
            return other.value == self.value
        return False

class BDEdge:

    def __init__(self, source_node, dest_node):
        self.source = source_node
        self.dest = dest_node
        self.count = 1

    def __str__(self):
        return str(self.source) + '-->' + str(self.dest)

    def __eq__(self, other):
        if type(other) is BDEdge:
            return self.source == other.source and self.dest == other.dest
        return False
