import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFrame, QHBoxLayout, QGridLayout, QLineEdit
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ControlGS")
        self.resize(1000, 650)
        self.setMinimumSize(800,500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(16)

        header_layout = QHBoxLayout()
        title_layout = QVBoxLayout()

        title = QLabel("ControlGS")
        title.setStyleSheet("font-size: 26px; font-weight: bold;")

        subtitle = QLabel("Controller to keyboard and mouse")
        subtitle.setStyleSheet("font-size: 13px; color: #999999;")

        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        self.status_label = QLabel("Controller disconnected")
        self.status_label.setStyleSheet("color: #F0B44D; font-size: 13px;")

        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        header_layout.addWidget(self.status_label)

        main_layout.addLayout(header_layout)

        mapping_frame = QFrame()
        mapping_frame.setObjectName("mappingFrame")

        mapping_layout = QHBoxLayout(mapping_frame)
        mapping_layout.setContentsMargins(20, 20, 20, 20)
        mapping_layout.setSpacing(20)

        controller_panel = QFrame()
        controller_layout = QVBoxLayout(controller_panel)

        controller_title = QLabel("Controller Layout")
        controller_title.setStyleSheet(
            "font-size: 17px; font-weight: bold;"
        )

        controller_description = QLabel(
            "Select a controller button to configure its mapping."
        )

        controller_description.setStyleSheet(
            "font-size: 12px; color: #999999;"
        )
        controller_description.setWordWrap(True)

        self.controller_placeholder = QLabel(
            "\n\n\n\n\n\n"
            "Xbox360 Controller\n\n"
            "Controller diagram will go here"
        )
        self.controller_placeholder.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.controller_placeholder.setStyleSheet("""
            background-color: #252525;
            border: 1px solid #383838;
            border-radius: 10px;
            color: #AAAAAA;
            font-size: 15px;
        """)

        controller_layout.addWidget(controller_title)
        controller_layout.addWidget(controller_description)
        controller_layout.addWidget(self.controller_placeholder, 1)

        mapping_panel = QFrame()
        button_mapping_layout = QVBoxLayout(mapping_panel)

        mapping_title = QLabel("Button Mappings")
        mapping_title.setStyleSheet(
            "font-size: 17px; font-weight: bold;"
        )

        mapping_description = QLabel(
            "Controller buttons and their assigned keys."
        )
        mapping_description.setStyleSheet(
            "font-size: 12px; color: #999999;"
        )
        mapping_description.setWordWrap(True)

        button_mapping_layout.addWidget(mapping_title)
        button_mapping_layout.addWidget(mapping_description)

        self.mapping_row = QGridLayout()
        self.mapping_row.setHorizontalSpacing(12)
        self.mapping_row.setVerticalSpacing(10)

        button_mapping = {
            "A": "Space",
            "B": "Left Ctrl",
            "X": "E",
            "Y": "R",
            "LB": "Q",
            "RB": "F",
            "LT": "Right click",
            "RT": "Left click",
            "Left stick": "W/A/S/D",
            "Right stick": "Camera"
        }

        for row, (button_name, key_name) in enumerate(
            button_mapping.items()
        ):
            button_label = QLabel(button_name)
            button_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            button_label.setStyleSheet("""
                background-color: #303030;
                border-radius: 6px;
                padding: 8px;
            """)

            key_label = QLabel(key_name)
            key_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            key_label.setStyleSheet("""
                background-color: #252525;
                border: 1px solid #383838;
                border-radius: 6px;
                padding: 8px;
                color: #DDDDDD;
            """)

            self.mapping_row.addWidget(button_label, row, 0)
            self.mapping_row.addWidget(key_label, row, 1)

        button_mapping_layout.addLayout(self.mapping_row)
        button_mapping_layout.addStretch()

        mapping_layout.addWidget(controller_panel, 3)
        mapping_layout.addWidget(mapping_panel, 2)

        main_layout.addWidget(mapping_panel, 1)

        controls_layout = QHBoxLayout()

        self.start_button = QPushButton("Start Mapping")
        self.stop_button = QPushButton("Stop Mapping")
        self.stop_button.setEnabled(False)

        controls_layout.addStretch()
        controls_layout.addWidget(self.start_button)
        controls_layout.addWidget(self.stop_button)

        main_layout.addLayout(controls_layout)

        self.start_button.clicked.connect(self.start_mapping)
        self.stop_button.clicked.connect(self.stop_mapping)

        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #171717;
                color: #F5F5F5;
            }

            QFrame{
                border: none;
            }

            QFrame#mappingFrame {
                background-color: #202020;
                border: 1px solid #383838;
                border-radius: 10px;
            }

            QpushButton {
                background-color: #303030;
                border: 1px solid #454545; 
                border-radius: 7px;
                padding: 10px 18px;
                font-size: 13px;
            }

            QPushButton:hover {
                background-color: #414141;
            }

            QPushButton:disabled {
                color: #777777;
                background-color: #252525;
            }

        """)

    def start_mapping(self):
        self.status_label.setText("Mapping started")
        self.status_label.setStyleSheet("color: #4ADE80; font-size: 13px;")

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_mapping(self):
        self.status_label.setText("Mapping stopped")
        self.status_label.setStyleSheet("color: #F0B44D; font-size: 13px;")

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())