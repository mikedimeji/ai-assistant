import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class GUIManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AI Voice Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Load and display character portrait
        self.label = QLabel(self)
        pixmap = QPixmap("src/assets/images/character.png")  # Replace with your character's image path
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUIManager()
    window.show()
    sys.exit(app.exec_())
