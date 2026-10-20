import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __int__(self):
        super().__init__()

        self.setWindowTitle("ControlGS")
        self.resize(1000, 650)

        self.setCentralWidget(QWidget())
        main_layout = QVBoxLayout(QWidget())
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(16)

        title = QLabel("ControlGS")
        title.setStyleSheet("font-size: 26px; font-weight: bold;")

        subtitle = QLabel("Controller to keyboard and mouse")
        subtitle.setStyleSheet("font-size: 13px; color: #999999;")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        mapping_area = QLabel("Control mapping will appear here")
        mapping_area.setAligment(Qt.AlignmentFlag.AlignCenter)
        mapping_area.setStyleSheet("""
            background-color: #222222;
            border: 1px solid #383838;
            border-radius: 10px;
            color: #999999;
            font-size: 15px;
        """)

        main_layout.addWidget(mapping_area, 1)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #171717;
                color: white;
            }

            QWidget {
                color: white;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())