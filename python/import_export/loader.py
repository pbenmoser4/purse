from file_reader import FileReader
from python.structures import Digraph

class Loader:
    """
    A class designed to load data into a graph
    """

    def __init__(self, from_file, to_structure, **kwargs):
        """
        Initializing a Loader Object with a FileReader object and a structure

        @type   from_file: string
        @param  from_file: Filename of the file that you want to load

        @type   to_structure: structure
        @param  to_structure: Graph, tree, etc that you want to load data into
        """

        self.file_reader = FileReader(from_file)
        self.structure = to_structure

    def load(self):
        """
        Load information from the file_reader.read() iterator into structure
        """

    def __load_graph(self):
