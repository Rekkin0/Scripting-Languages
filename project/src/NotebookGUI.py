import sys
import PySide6.QtWidgets as QtW
import PySide6.QtGui as QtG

import resources.constants as const
from Notebook import Notebook


class NotebookGUI(QtW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setLocale(const.LOCALE)

        self.icon = QtG.QIcon(const.MAIN_WINDOW_ICON)
        self.setWindowTitle(const.MAIN_WINDOW_TITLE)
        self.setWindowIcon(self.icon)
        self.resize(const.MAIN_WINDOW_SIZE)
        self.setCentralWidget(QtW.QWidget())

        main_layout = QtW.QVBoxLayout(self.centralWidget())
        main_layout.setContentsMargins(const.MAIN_LAYOUT_MARGINS)
        self.splitter = QtW.QSplitter(self.centralWidget())
        self.splitter.setChildrenCollapsible(const.SPLITTER_COLLAPSIBLE)
        main_layout.addWidget(self.splitter)

        self.initialize_system_tray()
        self.initialize_list()
        self.initialize_editor()   

    def initialize_system_tray(self):
        self.tray_icon = QtW.QSystemTrayIcon(self.icon, self)
        self.tray_icon.setToolTip(const.MAIN_WINDOW_TITLE)
        self.tray_icon.show()

        tray_menu = QtW.QMenu(self)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_restore = tray_menu.addAction("Restore")
        self.tray_quit = tray_menu.addAction("Quit")

    def initialize_list(self):
        list_widget = QtW.QWidget(self.splitter)
        list_layout = QtW.QVBoxLayout(list_widget)
        
        spacer = QtW.QSpacerItem(0, 3, QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Fixed)
        list_layout.addItem(spacer)

        # Create the note search layout
        search_label = QtW.QLabel(const.SEARCH_LABEL)
        search_label.setFont(const.SEARCH_LABEL_FONT)
        list_layout.addWidget(search_label, alignment=const.SEARCH_LABEL_ALIGNMENT)

        self.search_edit = QtW.QLineEdit()
        list_layout.addWidget(self.search_edit)

        # Create the notes layout
        list_button_layout = QtW.QHBoxLayout()
        list_layout.addLayout(list_button_layout)

        list_label = QtW.QLabel(const.NOTE_LIST_LABEL)
        list_label.setFont(const.NOTE_LIST_LABEL_FONT)
        list_button_layout.addWidget(
            list_label, alignment=const.NOTE_LIST_LABEL_ALIGNMENT
        )

        spacer = QtW.QSpacerItem(*const.DEFAULT_SPACER_PARAMETERS)
        list_button_layout.addItem(spacer)

        self.add_button = QtW.QPushButton(const.ADD_BUTTON_LABEL)
        self.add_button.setMaximumSize(const.ADD_DEL_BUTTON_SIZE)
        self.add_button.setFont(const.ADD_DEL_BUTTON_FONT)
        list_button_layout.addWidget(self.add_button)
        self.delete_button = QtW.QPushButton(const.DEL_BUTTON_LABEL)
        self.delete_button.setMaximumSize(const.ADD_DEL_BUTTON_SIZE)
        self.delete_button.setFont(const.ADD_DEL_BUTTON_FONT)
        self.delete_button.setEnabled(const.DEL_BUTTON_ENABLED)
        list_button_layout.addWidget(self.delete_button)

        # Create the note list
        self.notebook = Notebook()
        self.notebook.setDragDropMode(QtW.QListWidget.DragDropMode.InternalMove)
        self.notebook.setAcceptDrops(True)
        list_layout.addWidget(self.notebook)
        
        # Create the quit button
        self.quit_button = QtW.QPushButton(const.QUIT_BUTTON_LABEL)
        list_layout.addWidget(self.quit_button)

    def initialize_editor(self):
        editor_widget = QtW.QWidget(self.splitter)
        editor_layout = QtW.QVBoxLayout(editor_widget)

        # Create the title edit layout
        self.title_label = QtW.QLabel(const.TITLE_LABEL)
        self.title_label.setFont(const.TITLE_LABEL_FONT)
        self.title_label.setEnabled(const.TITLE_LABEL_ENABLED)
        editor_layout.addWidget(self.title_label)

        self.title_edit = QtW.QLineEdit()
        self.title_edit.setFont(const.TITLE_EDIT_FONT)
        self.title_edit.setEnabled(const.TITLE_EDIT_ENABLED)
        editor_layout.addWidget(self.title_edit)

        # Create the scheduled edit layout
        self.scheduled_button = QtW.QCheckBox(const.SCHEDULED_BUTTON_LABEL)
        self.scheduled_button.setFont(const.SCHEDULED_LABEL_FONT)
        self.scheduled_button.setEnabled(const.SCHEDULED_BUTTON_ENABLED)
        editor_layout.addWidget(self.scheduled_button)

        scheduled_edit_layout = QtW.QHBoxLayout()
        editor_layout.addLayout(scheduled_edit_layout)
        self.scheduled_edit_date = QtW.QDateEdit(const.SCHEDULED_EDIT_DATE)
        self.scheduled_edit_date.setDisplayFormat(const.SCHEDULED_EDIT_DATE_FORMAT)
        self.scheduled_edit_date.setCalendarPopup(const.SCHEDULED_EDIT_DATE_CALENDAR_POPUP)
        self.scheduled_edit_date.setEnabled(const.SCHEDULED_EDIT_DATE_ENABLED)
        scheduled_edit_layout.addWidget(self.scheduled_edit_date)
        self.scheduled_edit_time = QtW.QTimeEdit(const.SCHEDULED_EDIT_TIME)
        self.scheduled_edit_time.setDisplayFormat(const.SCHEDULED_EDIT_TIME_FORMAT)
        self.scheduled_edit_time.setEnabled(const.SCHEDULED_EDIT_TIME_ENABLED)
        scheduled_edit_layout.addWidget(self.scheduled_edit_time)

        # Create the content edit layout
        self.content_label = QtW.QLabel(const.CONTENT_LABEL)
        self.content_label.setFont(const.CONTENT_LABEL_FONT)
        self.content_label.setEnabled(const.CONTENT_LABEL_ENABLED)
        editor_layout.addWidget(
            self.content_label, alignment=const.CONTENT_LABEL_ALIGNMENT
        )

        self.content_edit = QtW.QTextEdit()
        self.content_edit.setEnabled(const.CONTENT_EDIT_ENABLED)
        editor_layout.addWidget(self.content_edit)

        # Create layout for the tags and created at
        tags_created_at_layout = QtW.QHBoxLayout()
        editor_layout.addLayout(tags_created_at_layout)

        # Create the tags edit layout
        tags_layout = QtW.QVBoxLayout()
        tags_created_at_layout.addLayout(tags_layout)

        self.tags_label = QtW.QLabel(const.TAGS_LABEL)
        self.tags_label.setFont(const.TAGS_LABEL_FONT)
        self.tags_label.setEnabled(const.TAGS_LABEL_ENABLED)
        tags_layout.addWidget(self.tags_label, alignment=const.TAGS_LABEL_ALIGNMENT)

        self.tags_edit = QtW.QLineEdit()
        self.tags_edit.setEnabled(const.TAGS_EDIT_ENABLED)
        tags_layout.addWidget(self.tags_edit)

        # Create the 'created at' label layout
        created_at_layout = QtW.QVBoxLayout()
        tags_created_at_layout.addLayout(created_at_layout)

        self.created_at_label = QtW.QLabel(const.CREATED_AT_LABEL)
        self.created_at_label.setFont(const.CREATED_AT_LABEL_FONT)
        self.created_at_label.setEnabled(const.CREATED_AT_LABEL_ENABLED)
        created_at_layout.addWidget(
            self.created_at_label, alignment=const.CREATED_AT_LABEL_ALIGNMENT
        )

        self.created_at_edit = QtW.QDateTimeEdit(const.CREATED_AT_EDIT_DEFAULT_DATETIME)
        self.created_at_edit.setMinimumSize(const.CREATED_AT_EDIT_SIZE)
        self.created_at_edit.setReadOnly(True)
        self.created_at_edit.setEnabled(const.CREATED_AT_EDIT_ENABLED)
        created_at_layout.addWidget(self.created_at_edit)

        # Create the button layout
        button_layout = QtW.QHBoxLayout()
        editor_layout.addLayout(button_layout)

        self.discard_button = QtW.QPushButton(const.DISCARD_BUTTON_LABEL)
        self.discard_button.setMinimumSize(const.DISCARD_BUTTON_SIZE)
        self.discard_button.setSizePolicy(const.DISCARD_BUTTON_SIZE_POLICY)
        self.discard_button.setEnabled(const.DISCARD_BUTTON_ENABLED)
        button_layout.addWidget(self.discard_button)

        self.theme_button = QtW.QCheckBox(const.THEME_BUTTON_LABEL)
        button_layout.addWidget(
            self.theme_button, alignment=const.THEME_BUTTON_ALIGNMENT
        )

        self.save_button = QtW.QPushButton(const.SAVE_BUTTON_LABEL)
        self.save_button.setMinimumSize(const.SAVE_BUTTON_SIZE)
        self.save_button.setSizePolicy(const.SAVE_BUTTON_SIZE_POLICY)
        self.save_button.setEnabled(const.SAVE_BUTTON_ENABLED)
        button_layout.addWidget(self.save_button)


if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)
    notebook_gui = NotebookGUI()
    notebook_gui.show()
    sys.exit(app.exec())
