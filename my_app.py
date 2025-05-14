from inst import*
class MainWin(Qwidget):
    def __init__(self):
        super().__init__(self):
        self.set_appear()
        self.unitUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt.instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.Layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self)