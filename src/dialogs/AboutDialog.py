import webbrowser

from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

class AboutDialog(QDialog):
    def __init__(self,
                 app_name: str,
                 app_description: str,
                 app_version: str,
                 app_developer: str,
                 app_git_url: str,
                 licence: str,
                 pixmap: QPixmap,
                 parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setWindowTitle("About")

        # Main layout
        layout = QVBoxLayout()

        # Application image
        app_image = QLabel(self)
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        app_image.setPixmap(pixmap)
        app_image.setAlignment(Qt.AlignCenter)
        layout.addWidget(app_image)


        # Application name header
        app_name_label = QLabel(f"{app_name}", self)  # Replace with your application name
        app_name_font = QFont()
        app_name_font.setBold(True)
        app_name_font.setPointSize(16)
        app_name_label.setFont(app_name_font)
        app_name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(app_name_label)

        # App Description
        app_desc = QLabel(f"{app_description}", self)
        app_desc_font = QFont()
        app_desc_font.setPointSize(8)
        app_desc.setFont(app_desc_font)
        app_desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(app_desc)

        # Version number
        version_label = QLabel(f"Version: {app_version}", self)
        version_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(version_label)

        # Developer
        developer_label = QLabel(f"(c) {app_developer}", self)
        developer_label_font = QFont()
        developer_label_font.setPointSize(8)
        developer_label.setFont(developer_label_font)
        developer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(developer_label)

        # Add a horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)


        # Developer
        licence_label = QLabel(f"{licence}", self)
        licence_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(licence_label)


        # Git URL
        self.git_label = QLabel(f'Visit <a href="{app_git_url}">{app_git_url}</a> for more information<br>'
                                f'or to report a bug or to suggest new features.', self)
        self.git_label.setOpenExternalLinks(True)
        self.git_label.setAlignment(Qt.AlignCenter)
        self.git_label.linkActivated.connect(self.open_url)
        layout.addWidget(self.git_label)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)



        # Close button
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def open_url(self, url):
        print(url)
        webbrowser.open(url)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = AboutDialog("TestApplication",
                         "This is a test application",
                         "1.0",
                         "2024 John Doe",
                         "github.com",
                            "This project is open source and <br>contributions are highly welcome."
                            "<br>The project is licensed under {licence}.",
                         QPixmap("adscopecontrol_icon.png"))
    dialog.exec()
    sys.exit(app.exec())
