
from io import BufferedReader
from gzip import GzipFile
def get(self, fp:GzipFile|BufferedReader):
    fp.read(1)
    pass

from typing import Literal
def setenv(env: Literal['prod', 'us', 'dev', 'staging'] = 'prod'):
    pass
