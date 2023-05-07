import sys
from PySide6.QtCore import Qt
import PySide6.QtWidgets as QtW

from file_manip import get_lines


class LogViewer(QtW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.log_file: str
        self.log_lines: list[str]
        self.initUI()
        
    def initUI(self):
        """
        Initialize the user interface.
        """
        # Set up the main window
        self.setWindowTitle('Log browser')
        self.resize(800, 600)

        # Create the central widget and layout
        central_widget = QtW.QWidget(self)
        grid = QtW.QGridLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        # Add the text box with the file path to the layout
        self.file_path_box = QtW.QLineEdit()
        self.file_path_box.setReadOnly(True)
        grid.addWidget(self.file_path_box, 0, 0, 1, 2)

        # Add the Open button to the layout
        open_button = QtW.QPushButton('Open')
        open_button.clicked.connect(self.show_logs)
        grid.addWidget(open_button, 0, 2)

        # Add the list box to the layout
        self.list_box = QtW.QListWidget()
        self.list_box.itemClicked.connect(self.display_log_details)
        grid.addWidget(self.list_box, 1, 0)

        # Add the detail box to the layout
        self.detail_box = QtW.QTextEdit()
        self.detail_box.setReadOnly(True)
        grid.addWidget(self.detail_box, 1, 1, 1, 2)
        
        self.previous_button = QtW.QPushButton('Previous')
        self.previous_button.clicked.connect(self.display_previous_log)
        grid.addWidget(self.previous_button, 2, 0)
        
        self.next_button = QtW.QPushButton('Next')
        self.next_button.clicked.connect(self.display_next_log)
        grid.addWidget(self.next_button, 2, 1)

    def show_logs(self):
        # Prompt the user to select a log file to open and get the log lines from the file
        log_file, _ = QtW.QFileDialog.getOpenFileName(self, 'Open Log File', filter='Log Files (*.log)')
        log_lines = get_lines(log_file)
        self.file_path_box.setText(log_file)
        
        # Clear the list box and populate it with the log lines
        self.list_box.clear()
        for line in log_lines:
            if line := line.strip():
                self.list_box.addItem(line)

        # Store the log file path and log lines for future use
        self.log_file = log_file
        self.log_lines = log_lines

    def display_log_details(self, item: QtW.QListWidgetItem):
        # Get the index of the selected item and display the corresponding line from the log file in the detail box
        self.current_index: int = self.list_box.row(item)      
        self.detail_box.setText(self.log_lines[self.current_index])
        
    def display_previous_log(self):
        previous_log = self.list_box.item(self.current_index - 1)
        self.display_log_details(previous_log)
        
    def display_next_log(self):
        next_log = self.list_box.item(self.current_index + 1)
        self.display_log_details(next_log)


def main():
    # Create the PySide application and main window
    app = QtW.QApplication(sys.argv)
    window = LogViewer()
    window.show()

    # Start the event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
