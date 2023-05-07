import sys
from PySide6.QtCore import Qt
import PySide6.QtWidgets as QtW

from file_manip import get_lines


class LogViewer(QtW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.log_file: str
        self.log_lines: list[str]
        
    def initUI(self):
        """
        Initialize the user interface.
        """
        # Set up the main window
        self.setWindowTitle('Log browser')
        self.resize(800, 600)

        # Create the central widget and layout
        central_widget = QtW.QWidget(self)
        layout = QtW.QGridLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Add the Open button to the layout
        open_button = QtW.QPushButton('Open')
        open_button.clicked.connect(self.show_log_file)
        layout.addWidget(open_button, 0, 1)
        
        # Add the text box with the file path to the layout
        self.file_path_box = QtW.QLineEdit()
        self.file_path_box.setReadOnly(True)
        layout.addWidget(self.file_path_box, 0, 0)

        # Add the list box to the layout
        self.list_box = QtW.QListWidget()
        self.list_box.itemClicked.connect(self.show_log_detail)
        layout.addWidget(self.list_box, 1, 0)

        # Add the detail box to the layout
        self.detail_box = QtW.QTextEdit()
        self.detail_box.setReadOnly(True)
        layout.addWidget(self.detail_box, 1, 1)

    def show_log_file(self):
        # Prompt the user to select a log file to open
        log_file, _ = QtW.QFileDialog.getOpenFileName(self, 'Open Log File', filter='Log Files (*.log)')
        log_lines = get_lines(log_file)
        self.file_path_box.setText(log_file)
        for line in log_lines:
            if line := line.strip():
                self.list_box.addItem(line)

        # Store the log file path and log lines for future use
        self.log_file = log_file
        self.log_lines = log_lines

    def show_log_detail(self, item: QtW.QListWidgetItem):
        # Get the index of the selected item and display the corresponding line from the log file in the detail box
        index: int = self.list_box.row(item)
        self.detail_box.setText(self.log_lines[index])


def main():
    # Create the PySide application and main window
    app = QtW.QApplication(sys.argv)
    window = LogViewer()
    window.show()

    # Start the event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
