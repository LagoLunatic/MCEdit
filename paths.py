
import os

try:
  from sys import _MEIPASS
  ROOT_PATH = _MEIPASS
except ImportError:
  ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

MCLIB_PATH = os.path.join(ROOT_PATH, "mclib")
DATA_PATH = os.path.join(MCLIB_PATH, "data")
