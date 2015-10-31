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
        self.assertIsInstance(graph.add_node(node), BDNode)

        # Adding a non-node returns None
        value_ret = graph.add_node(value)
        self.assertNotIsInstance(value_ret, BDNode)
        self.assertIsNone(value_ret)

        # Adding a duplicate node returns the original

if __name__ == '__main__':
    unittest.main()
