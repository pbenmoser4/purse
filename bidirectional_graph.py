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
            return other.value == self.value
        return False

    def __hash__(self):
        return hash(self.value)

    def add_dest_edge(self, edge):
        if isinstance(edge, BDEdge):
            self.dest_edges.add(edge)
            return True
        return False

    def add_source_edge(self, edge):
        if isinstance(edge, BDEdge):
            self.source_edges.add(edge)
            return True
        return False

    def add_edge(self, edge, _type):
        if isinstance(edge, BDEdge):
            if _type == 'source':
                self.add_source_edge(edge)
                return True
            elif _type == 'dest':
                self.add_dest_edge(edge)
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

    def __str__(self):
        return str(self.source.value) + '-' + str(self.count) + '->' + str(self.dest.value)

    def __hash__(self):
        hs = str(self.source) + str(self.dest)
        return hash(hs)

    def __eq__(self, other):
        if type(other) is BDEdge:
            return self.source == other.source and self.dest == other.dest
        return False

    def increment_count(self):
        self.count += 1


graph = BidirectionalGraph()
source_node = BDNode('source')
dest_node = BDNode('dest')
graph.add_node(source_node)
graph.add_node(dest_node)
graph.add_edge(source_node, dest_node)
print source_node
print dest_node