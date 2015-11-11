from file_reader import FileReader
from python.structures import Digraph

class Loader:
    """
    A class designed to load data into a graph
    """

    def __init__(self, file_reader, structure):
        """
        Initializing a Loader Object with a FileReader object and a structure

        @type   file_reader: FileReader
        @param  file_reader: A FileReader object used to read desired file

        @type   structure: structure
        @param  structure: graph, tree, etc
        """

        self.file_reader = file_reader
        self.structure = structure
