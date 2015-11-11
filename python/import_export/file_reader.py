import os

class FileReader:
    """
    Class that reads files and creates input sources for graph implementation
    """

    PATH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
    PATH_PYTHON = os.path.abspath(os.path.join(PATH_ROOT, 'python'))
    PATH_SRC = os.path.abspath(os.path.join(PATH_ROOT, 'src'))
    PATH_VIZ = os.path.abspath(os.path.join(PATH_ROOT, 'viz'))

    def __init__(self, filename, filetype="text", loadtype="iter"):
        self.filename = filename
        self.filetype = filetype
        self.loadtype = loadtype
        self.file = None
        if self.__input_exists():
            self.file = open(os.path.abspath(os.path.join(self.PATH_SRC, self.filename)))

    def __input_exists(self):
        return self.filename in os.listdir(self.PATH_SRC)

    def read(self):
        """
        Read self.file
        """

        if self.filetype == 'text':
            return self.__read_text()

    def __read_text(self):
        """
        Custom read implementation for a text file

        @rtype  Generator
        @return A generator that goes through self.file and yields words
        """

        if self.file:
            for line in self.file:
                # loop through the lines in the file and return one item at a
                # time. Item is defined by a set of characters separated by
                # whitespace
                for item in line.split():
                    yield item
            # This is implicit I think, but why not
            raise StopIteration
        else:
            raise Exception

if __name__ == "__main__":
    fr = FileReader('robin-passage.txt')

    print fr.PATH_PYTHON

    print os.listdir(fr.PATH_SRC)

    for item in fr.read():
        print item
    # print os.path.join(fr._PATH_SRC, os.path.pardir, os.path.pardir)
