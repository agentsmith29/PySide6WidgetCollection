# Add the src to path
import os
import sys
from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

# Import the necessary modules
from WidgetCollection.Dialogs.AboutDialog import AboutDialog
from WidgetCollection.Tools.PyProjectExtractor import extract_pyproject_info

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app_name = "TestApplication"

    app_version = extract_pyproject_info(Path(__file__).parent.parent, "version")
    app_author = extract_pyproject_info(Path(__file__).parent.parent, "author")
    app_url = extract_pyproject_info(Path(__file__).parent.parent, "url")
    app_description = extract_pyproject_info(Path(__file__).parent.parent, "description")
    app_licence = extract_pyproject_info(Path(__file__).parent.parent, "license")


    dialog = AboutDialog("TestApplication",
                         app_description,
                         app_version,
                         f"2024 {app_author}",
                         app_url,
                         f"This project is open source and contributions are highly welcome.<br>"
                         f"<br>The project is licensed under <br>{app_licence}.",
                         QPixmap("testapp_icon.png"))
    dialog.exec()
    sys.exit(app.exec())
