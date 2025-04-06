from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Local LLM App")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        label = QLabel("Hello! This is your offline LLM app GUI.")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)