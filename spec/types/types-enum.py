
from io import BufferedReader
from gzip import GzipFile
def get(self, fp:GzipFile|BufferedReader):
    fp.read(1)
    pass
