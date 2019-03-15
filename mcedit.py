#!/usr/bin/python3.6

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import sys

from mcedit_ui.main_window import MCEditorWindow

# Allow keyboard interrupts on the command line to instantly close the program.
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

try:
  from sys import _MEIPASS
except ImportError:
  # Setting the app user model ID is necessary for Windows to display a custom taskbar icon when running from source.
  import ctypes
  app_id = "LagoLunatic.MinishCapEditor"
  try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
  except AttributeError:
    # Versions of Windows before Windows 7 don't support SetCurrentProcessExplicitAppUserModelID, so just swallow the error.
    pass

qApp = QApplication(sys.argv)
window = MCEditorWindow()
sys.exit(qApp.exec_())
