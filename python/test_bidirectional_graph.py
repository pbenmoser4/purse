import unittest
from bidirectional_graph import BidirectionalGraph, BDNode, BDEdge

class BidirectionalGraphTestCase(unittest.TestCase):
    """Tests for the BidirectionalGraph class"""

    def test_add_node(self):
        value = 'val'
        node = BDNode(value)
        duplicate_node = BDNode(value)
        graph = BidirectionalGraph()

        # Adding a node returns BDNode instance
        node_ret = graph.add_node(node)
        self.assertIsInstance(node_ret, BDNode)

        # Adding a non-node returns None
        value_ret = graph.add_node(value)
        self.assertNotIsInstance(value_ret, BDNode)
        self.assertIsNone(value_ret)

        # Adding a duplicate node returns the original
        duplicate_ret = graph.add_node(duplicate_node)
        self.assertIsInstance(duplicate_ret, BDNode)
        self.assertIs(duplicate_ret, node_ret)

    def test_add_edge(self):
        graph = BidirectionalGraph()
        source = BDNode('source')
        dest = BDNode('dest')
        fake_source = 'source'
        fake_dest = 'dest'

        # Trying to add an edge with non-nodes returns None
        self.assertIsNone(graph.add_edge(source, fake_dest))
        self.assertIsNone(graph.add_edge(fake_source, dest))
        self.assertIsNone(graph.add_edge(fake_source, fake_dest))

        # Trying to add an edge when both nodes aren't in the graph returns None
        self.assertIsNone(graph.add_edge(source, dest))
        graph.add_node(source)
        self.assertIsNone(graph.add_edge(source, dest))
        graph.add_node(dest)

        # Adding an edge with both nodes in the graph returns a new edge,
        # if the edge doesn't yet exist in the graph
        res = graph.add_edge(source, dest)
        self.assertIsInstance(res, BDEdge)
        self.assertEqual(res.count, 1)

        # Adding an edge with both nodes in the graph increments the count of
        # the edge that already exists
        inc = graph.add_edge(source, dest)
        self.assertIsInstance(inc, BDEdge)
        self.assertEqual(inc, res)
        self.assertEqual(inc.count, 2)


class BDNodeTestCase(unittest.TestCase):
    """ Tests for the BDNode class """

class BDEdgeTestCase(unittest.TestCase):
    """ Tests for the BDEdge class """

if __name__ == '__main__':
    unittest.main()
