from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit
from llm.inference import generate_response

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OneResume - Local AI Assistant")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.button = QPushButton("Generate Response")
        self.button.clicked.connect(self.handle_generate)

        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.output_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_generate(self):
        prompt = self.input_box.toPlainText().strip()
        if prompt:
            response = generate_response(prompt)
            self.output_box.setText(response)