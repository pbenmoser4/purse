import unittest
from exceptions import AttributeError, KeyError
from digraph import Digraph, DNode, DEdge

# class DigraphTestCase(unittest.TestCase):
#     """
#     Tests for the Digraph class
#     """

class DNodeTestCase(unittest.TestCase):
    """
    Tests for the digraph DNode class
    """

    def test_str(self):
        node = DNode('value')
        self.assertEqual(str(node), 'value')

    def test_eq(self):
        node = DNode('val')
        other = DNode('val')
        self.assertEqual(node, other)
        self.assertIsNot(node, other)

    def test_ne(self):
        node = DNode('val')
        other = DNode('other')
        self.assertNotEqual(node, other)

    def test_hash(self):
        node = DNode('val')
        other = DNode('val')
        self.assertEqual(hash(node), hash(other))

if __name__ == '__main__':
    unittest.main()
