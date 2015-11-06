import unittest
from exceptions import AttributeError, KeyError
from digraph import Digraph

# class DigraphTestCase(unittest.TestCase):
#     """
#     Tests for the Digraph class
#     """

class DigraphTestCase(unittest.TestCase):

    def test_init(self):
        """
        Digraph initialization creates an empty dictionary for .nodes
        """
        dgraph = Digraph()
        self.assertEquals(dgraph.nodes, {})

    def test_get_nodes(self):
        """
        test get_nodes

        We will add a bunch of nodes and make sure it returns all of them. We're
        using a set comparison, because
        """

        dgraph = Digraph()
        node_list = ['one', 'two', 'three']
        for n in node_list:
            dgraph.add_node(n)
        self.assertEquals(set(dgraph.get_nodes()), set(node_list))


    def test_get_neighbors(self):
        """
        test get_neighbors

        Add a few nodes to a graph, and then add a few neighbors to that node,
        and check whether get_neighbors returns the expected result
        """

        dgraph = Digraph()
        node_list = ['one', 'two', 'three']
        for n in node_list:
            dgraph.add_node(n)
            if n != 'one':
                dgraph.add_edge(('one', n))
        self.assertEquals(dgraph.get_neighbors('one'), ['two', 'three'])

    def test_get_edges(self):
        """
        test get_edges

        Add a few nodes to a graph, and then add a few edges to the graph. Check
        whether get_edges returns the expected edges
        """

        dgraph = Digraph()
        node_list = ['one', 'two', 'three']
        for n in node_list:
            dgraph.add_node(n)
            if n != 'one':
                dgraph.add_edge(('one', n))
        edges = [('one', 'two'), ('one', 'three')]
        self.assertEquals(dgraph.get_edges(), edges)

    def test_has_node(self):
        """
        test has_node
        """

    def test_has_edge(self):
        """
        test has_edge
        """

    def test_add_node(self):
        """
        test add_node
        """

    def test_add_edge(self):
        """
        test add_edge
        """

    def test_del_node(self):
        """
        test del_node
        """

    def test_del_edge(self):
        """
        Test del_edge
        """

    def test_get_node_order(self):
        """
        Test get_node_order
        """

if __name__ == '__main__':
    unittest.main()
