from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *

class FinalWin(QWidget):
   def __init__(self):
       ''' окно, в котором проводится опрос '''
       super().__init__()
