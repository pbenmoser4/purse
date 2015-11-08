import os

class FileReader:
    """
    Class that reads files and creates input sources for graph implementation
    """

    PATH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
    PATH_PYTHON = os.path.abspath(os.path.join(PATH_ROOT, 'python'))
    PATH_SRC = os.path.abspath(os.path.join(PATH_ROOT, 'src'))
    PATH_VIZ = os.path.abspath(os.path.join(PATH_ROOT, 'viz'))

    def __init__(self, filename, filetype="txt", loadtype="iter"):
        self.filename = filename
        self.filetype = filetype
        self.loadtype = loadtype
        self.file = None
        if self.__input_exists():
            self.file = open(os.path.abspath(os.path.join(self.PATH_SRC, self.filename)))

    def __input_exists(self):
        return self.filename in os.listdir(self.PATH_SRC)

if __name__ == "__main__":
    fr = FileReader('robin.txt')

    print fr.PATH_PYTHON

    print os.listdir(fr.PATH_SRC)
    # print os.path.join(fr._PATH_SRC, os.path.pardir, os.path.pardir)
