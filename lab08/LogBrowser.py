import sys
import PySide6.QtWidgets as QtW
import PySide6.QtGui as QtG

import resources.constants as const
import resources.log_retrieval as lr
import resources.log_processing as lp
import resources.styling as styling


class LogBrowser(QtW.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        # Create log line cache needed for functionality
        self.log_lines: list[str] = []
        self.complete_log_lines: list[str] = []

    def initialize_ui(self):
        """
        Initializes the UI elements.
        """
        # Set the locale to the English (US) locale
        self.setLocale(const.LOCALE)
        
        # Set the application style and palette
        application.setStyle(styling.STYLE)
        application.setPalette(styling.LIGHT_PALETTE)
        
        # Set the window title and size
        self.setWindowTitle(const.WINDOW_TITLE)
        self.setWindowIcon(QtG.QIcon('lab08\\resources\\icon.png'))
        self.resize(const.WINDOW_SIZE)

        # Create the central widget
        self.central_widget = QtW.QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Create the main layout
        self.main_layout = QtW.QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(const.MAIN_LAYOUT_SPACING)
        self.main_layout.setContentsMargins(const.MAIN_LAYOUT_MARGINS)
        
        # Create the splitter
        self.splitter = QtW.QSplitter(self.central_widget)
        self.splitter.setChildrenCollapsible(const.SPLITTER_COLLAPSIBLE)
        
        # Set other elements of the UI
        self.set_file_selection()
        self.set_log_browser()
        self.set_navigation_buttons()

    def set_file_selection(self):
        """
        Sets up the file selection UI elements.
        """
        # Create a layout for the file selection
        self.file_selection_layout = QtW.QHBoxLayout()
        
        # Create the file selection file path textbox
        self.file_path_textbox = QtW.QLineEdit()
        self.file_path_textbox.setReadOnly(const.FILE_PATH_TEXTBOX_READ_ONLY)
        self.file_selection_layout.addWidget(self.file_path_textbox)

        # Create the file selection open button
        self.file_open_button = QtW.QPushButton(const.OPEN_BUTTON_LABEL)
        self.file_open_button.setMinimumSize(const.OPEN_BUTTON_MIN_SIZE)
        self.file_open_button.clicked.connect(self.open_log_file)
        self.file_selection_layout.addWidget(self.file_open_button)
        
        # Add the file selection layout to the main layout
        self.main_layout.addLayout(self.file_selection_layout)
        
    def set_log_list_filter(self):
        """
        Sets up the log list and date filter UI elements.
        """
        self.left_widget = QtW.QWidget(self.splitter)

        # Create a layout for the log list and filter
        self.left_layout = QtW.QVBoxLayout(self.left_widget)
        self.left_layout.setContentsMargins(const.LEFT_LAYOUT_MARGINS)
        
        # Create a layout for the date filter
        self.date_layout = QtW.QHBoxLayout()
        
        # Create the 'date from' filter
        self.date_from_label = QtW.QLabel(const.DATE_FROM_LABEL)
        self.date_layout.addWidget(self.date_from_label)
        self.date_from_datebox = QtW.QDateTimeEdit()
        self.date_from_datebox.setSizePolicy(const.DATE_FROM_DATEBOX_SIZE_POLICY)
        self.date_from_datebox.setDisplayFormat(const.DATE_FROM_DATEBOX_FORMAT)
        self.date_from_datebox.setDateTime(const.DATE_FROM_DATEBOX_DEFAULT_DATETIME)
        self.date_layout.addWidget(self.date_from_datebox)
        
        # Create a spacer between the two date filter boxes
        self.date_spacer = QtW.QSpacerItem(const.DATE_SPACER_WIDTH, 
                                           const.DATE_SPACER_HEIGHT, 
                                           const.DATE_SPACER_HORIZONTAL_SIZE_POLICY, 
                                           const.DATE_SPACER_VERTICAL_SIZE_POLICY)
        self.date_layout.addItem(self.date_spacer)
        
        # Create the 'date to' filter
        self.date_to_label = QtW.QLabel(const.DATE_TO_LABEL)
        self.date_layout.addWidget(self.date_to_label)
        self.date_to_datebox = QtW.QDateTimeEdit()
        self.date_to_datebox.setSizePolicy(const.DATE_TO_DATEBOX_SIZE_POLICY)
        self.date_to_datebox.setDisplayFormat(const.DATE_TO_DATEBOX_FORMAT)
        self.date_to_datebox.setDateTime(const.DATE_TO_DATEBOX_DEFAULT_DATETIME)
        self.date_layout.addWidget(self.date_to_datebox)
        
        # Add the date filter layout to the primary layout
        self.left_layout.addLayout(self.date_layout)
        
        # Create a filter and reset buttons and add it to the layout
        self.filter_layout = QtW.QHBoxLayout()
        
        self.filter_button = QtW.QPushButton(const.FILTER_BUTTON_LABEL)
        self.filter_button.clicked.connect(self.filter_logs)
        self.filter_layout.addWidget(self.filter_button)
        
        self.reset_button = QtW.QPushButton(const.RESET_BUTTON_LABEL)
        self.reset_button.clicked.connect(self.reset_log_list)
        self.filter_layout.addWidget(self.reset_button)
        
        self.left_layout.addLayout(self.filter_layout)

        # Create the log list and add it to the layout
        self.log_list = QtW.QListWidget()
        self.log_list.itemSelectionChanged.connect(self.update_log_details)
        self.left_layout.addWidget(self.log_list)

    def set_log_details(self):
        """
        Sets up the log details UI elements.
        """
        self.right_widget = QtW.QWidget(self.splitter)
        
        # Create a layout for the log details
        self.right_layout = QtW.QVBoxLayout(self.right_widget)
        self.right_layout.setContentsMargins(const.RIGHT_LAYOUT_MARGINS)
        
        # Create the details label
        self.details_label = QtW.QLabel(const.DETAILS_LABEL)
        self.details_label.setMinimumSize(const.DETAILS_LABEL_MIN_SIZE)
        self.details_label.setSizePolicy(const.DETAILS_LABEL_SIZE_POLICY)
        self.details_label.setAlignment(const.DETAILS_LABEL_ALIGNMENT)
        self.details_label.setFont(const.DETAILS_LABEL_BOLD_FONT)
        self.right_layout.addWidget(self.details_label)

        # Create the date layout
        self.date_layout = QtW.QHBoxLayout()
        
        self.date_label = QtW.QLabel(const.DATE_LABEL)
        self.date_label.setMinimumSize(const.DATE_LABEL_MIN_SIZE)
        self.date_label.setAlignment(const.DATE_LABEL_ALIGNMENT)
        self.date_layout.addWidget(self.date_label)
        
        self.date_textbox = QtW.QLineEdit()
        self.date_textbox.setReadOnly(const.DATE_TEXTBOX_READ_ONLY)
        self.date_layout.addWidget(self.date_textbox)
        
        self.right_layout.addLayout(self.date_layout)
        
        # Create the time layout
        self.time_layout = QtW.QHBoxLayout()
        
        self.time_label = QtW.QLabel(const.TIME_LABEL)
        self.time_label.setMinimumSize(const.TIME_LABEL_MIN_SIZE)
        self.time_label.setAlignment(const.TIME_LABEL_ALIGNMENT)
        self.time_layout.addWidget(self.time_label)
        
        self.time_textbox = QtW.QLineEdit()
        self.time_textbox.setReadOnly(const.TIME_TEXTBOX_READ_ONLY)
        self.time_layout.addWidget(self.time_textbox)
        
        self.right_layout.addLayout(self.time_layout)
        
        # Create the hostname layout
        self.hostname_layout = QtW.QHBoxLayout()
        
        self.hostname_label = QtW.QLabel(const.HOSTNAME_LABEL)
        self.hostname_label.setMinimumSize(const.HOSTNAME_LABEL_MIN_SIZE)
        self.hostname_label.setAlignment(const.HOSTNAME_LABEL_ALIGNMENT)
        self.hostname_layout.addWidget(self.hostname_label)
        
        self.hostname_textbox = QtW.QLineEdit()
        self.hostname_textbox.setReadOnly(const.HOSTNAME_TEXTBOX_READ_ONLY)
        self.hostname_layout.addWidget(self.hostname_textbox)
        
        self.right_layout.addLayout(self.hostname_layout)
        
        # Create the process ID layout
        self.process_id_layout = QtW.QHBoxLayout()
        
        self.process_id_label = QtW.QLabel(const.PROCESS_ID_LABEL)
        self.process_id_label.setMinimumSize(const.PROCESS_ID_LABEL_MIN_SIZE)
        self.process_id_label.setAlignment(const.PROCESS_ID_LABEL_ALIGNMENT)
        self.process_id_layout.addWidget(self.process_id_label)
        
        self.process_id_textbox = QtW.QLineEdit()
        self.process_id_textbox.setReadOnly(const.PROCESS_ID_TEXTBOX_READ_ONLY)
        self.process_id_layout.addWidget(self.process_id_textbox)
        
        self.right_layout.addLayout(self.process_id_layout)
        
        # Create the IP address layout
        self.ip_address_layout = QtW.QHBoxLayout()
        
        self.ip_address_label = QtW.QLabel(const.IP_ADDRESS_LABEL)
        self.ip_address_label.setMinimumSize(const.IP_ADDRESS_LABEL_MIN_SIZE)
        self.ip_address_label.setAlignment(const.IP_ADDRESS_LABEL_ALIGNMENT)
        self.ip_address_layout.addWidget(self.ip_address_label)
        
        self.ip_address_textbox = QtW.QLineEdit()
        self.ip_address_textbox.setReadOnly(const.IP_ADDRESS_TEXTBOX_READ_ONLY)
        self.ip_address_layout.addWidget(self.ip_address_textbox)
        
        self.right_layout.addLayout(self.ip_address_layout)
        
        # Create the username layout
        self.username_layout = QtW.QHBoxLayout()
        
        self.username_label = QtW.QLabel(const.USERNAME_LABEL)
        self.username_label.setMinimumSize(const.USERNAME_LABEL_MIN_SIZE)
        self.username_label.setAlignment(const.USERNAME_LABEL_ALIGNMENT)
        self.username_layout.addWidget(self.username_label)
        
        self.username_textbox = QtW.QLineEdit()
        self.username_textbox.setReadOnly(const.USERNAME_TEXTBOX_READ_ONLY)
        self.username_layout.addWidget(self.username_textbox)
        
        self.right_layout.addLayout(self.username_layout)
        
        # Create the category layout
        self.category_layout = QtW.QHBoxLayout()
        
        self.category_label = QtW.QLabel(const.CATEGORY_LABEL)
        self.category_label.setMinimumSize(const.CATEGORY_LABEL_MIN_SIZE)
        self.category_label.setAlignment(const.CATEGORY_LABEL_ALIGNMENT)
        self.category_layout.addWidget(self.category_label)
        
        self.category_textbox = QtW.QLineEdit()
        self.category_textbox.setReadOnly(const.CATEGORY_TEXTBOX_READ_ONLY)
        self.category_layout.addWidget(self.category_textbox)
        
        self.right_layout.addLayout(self.category_layout)

        # Create the message layout
        self.message_layout = QtW.QHBoxLayout()
        
        self.message_label = QtW.QLabel(const.MESSAGE_LABEL)
        self.message_label.setMinimumSize(const.MESSAGE_LABEL_MIN_SIZE)
        self.message_label.setAlignment(const.MESSAGE_LABEL_ALIGNMENT)
        self.message_layout.addWidget(self.message_label)
        
        self.message_textbox = QtW.QTextEdit()
        self.message_textbox.setReadOnly(const.MESSAGE_TEXTBOX_READ_ONLY)
        self.message_textbox.setMaximumSize(const.MESSAGE_TEXTBOX_MAX_SIZE)
        self.message_layout.addWidget(self.message_textbox)
        
        self.right_layout.addLayout(self.message_layout)

        # Create the size layout
        self.size_layout = QtW.QHBoxLayout()
        
        self.size_label = QtW.QLabel(const.SIZE_LABEL)
        self.size_label.setMinimumSize(const.SIZE_LABEL_MIN_SIZE)
        self.size_label.setAlignment(const.SIZE_LABEL_ALIGNMENT)
        self.size_layout.addWidget(self.size_label)
        
        self.size_textbox = QtW.QLineEdit()
        self.size_textbox.setReadOnly(const.SIZE_TEXTBOX_READ_ONLY)
        self.size_layout.addWidget(self.size_textbox)
        
        self.right_layout.addLayout(self.size_layout)
        
    def set_log_browser(self):
        """
        Sets up the log browser widget.
        """
        self.main_layout.addWidget(self.splitter)
        
        self.set_log_list_filter()
        self.set_log_details()
        
    def set_navigation_buttons(self):
        """
        Sets up the navigation buttons.
        """
        self.buttons_layout = QtW.QHBoxLayout()
        
        self.previous_button = QtW.QPushButton(const.PREVIOUS_BUTTON_LABEL)
        self.previous_button.setMinimumSize(const.PREVIOUS_BUTTON_MIN_SIZE)
        self.previous_button.setEnabled(const.PREVIOUS_BUTTON_ENABLED)
        self.previous_button.clicked.connect(self.select_previous_log)
        self.buttons_layout.addWidget(self.previous_button, 0, const.PREVIOUS_BUTTON_LABEL_ALIGNMENT)
        
        self.dark_theme_button = QtW.QRadioButton(const.DARK_THEME_BUTTON_LABEL)
        self.dark_theme_button.toggled.connect(self.toggle_dark_theme)
        self.dark_theme_button.toggle()
        self.buttons_layout.addWidget(self.dark_theme_button, 0, const.DARK_THEME_BUTTON_ALIGNMENT)

        self.next_button = QtW.QPushButton(const.NEXT_BUTTON_LABEL)
        self.next_button.setMinimumSize(const.NEXT_BUTTON_MIN_SIZE)
        self.next_button.setEnabled(const.NEXT_BUTTON_ENABLED)
        self.next_button.clicked.connect(self.select_next_log)
        self.buttons_layout.addWidget(self.next_button, 0, const.NEXT_BUTTON_LABEL_ALIGNMENT)

        self.main_layout.addLayout(self.buttons_layout)

    def open_log_file(self):
        """
        Opens a log file and immediately populates the log list.
        """
        self.log_file_path, _ = QtW.QFileDialog.getOpenFileName(self, 
                                                                const.OPEN_LOG_FILE_DIALOG_TITLE, 
                                                                const.OPEN_LOG_FILE_DIALOG_DIRECTORY, 
                                                                const.OPEN_LOG_FILE_DIALOG_FILTER)
        try:
            self.log_lines = lr.get_lines(self.log_file_path)
            self.complete_log_lines = self.log_lines
            self.file_path_textbox.setText(self.log_file_path)
            self.reset_log_list()
        except FileNotFoundError:
            ...
        
    def update_log_list(self):
        """
        Updates the log list.
        """
        self.log_list.clear()
        for line in self.log_lines:
            if line := line.strip():
                self.log_list.addItem(line)
                
    def reset_log_list(self):
        """
        Resets the log list to its state with complete unfiltered logs.
        """
        if not self.complete_log_lines:
            return
        self.log_lines = self.complete_log_lines
        self.date_from_datebox.setDateTime(const.DATE_FROM_DATEBOX_DEFAULT_DATETIME)
        self.date_to_datebox.setDateTime(const.DATE_TO_DATEBOX_DEFAULT_DATETIME)
        self.update_log_list()            
                
    def filter_logs(self):
        """
        Filters the log list based on selected date/time range.
        """
        from_datetime = self.date_from_datebox.dateTime().toPython()
        to_datetime = self.date_to_datebox.dateTime().toPython()
        
        self.log_list.clear()
        self.filtered_logs_lines: list[str] = []
        if not self.log_lines:
            return
        for line in self.log_lines:
            timestamp = lp.parse_log(line)['timestamp']
            if timestamp > to_datetime or not (line := line.strip()):
                break
            if from_datetime <= timestamp:
                self.filtered_logs_lines.append(line)
        self.log_lines = self.filtered_logs_lines
        self.update_log_list()
                      
    def update_log_details(self):
        """
        Updates the log details.
        """
        selected_log = self.log_lines[self.log_list.currentRow()]
        if not selected_log:
            return
        detailed_log = lp.parse_log(selected_log)
        self.date_textbox.setText(detailed_log['timestamp'].strftime(const.DATETIME_DATE_FORMAT))
        self.time_textbox.setText(detailed_log['timestamp'].strftime(const.DATETIME_TIME_FORMAT))
        self.hostname_textbox.setText(detailed_log['hostname'])
        self.process_id_textbox.setText(str(detailed_log['process']))
        self.ip_address_textbox.setText(ip_addrs[0] if (ip_addrs := lp.get_ipv4s_from_log(detailed_log)) 
                                        else const.NOT_AVAILABLE_MESSAGE)
        self.username_textbox.setText(username if (username := lp.get_user_from_log(detailed_log)) 
                                      else const.NOT_AVAILABLE_MESSAGE)
        self.category_textbox.setText(lp.get_message_type(detailed_log['message']))
        self.message_textbox.setText(detailed_log['message'])
        self.size_textbox.setText(str(detailed_log['bytes']) + ' bytes')
        self.update_navigation_buttons()
        
    def update_navigation_buttons(self):
        """
        Updates the avalibility of navigation buttons.
        """
        self.current_row = self.log_list.currentRow()
        self.previous_button.setEnabled(self.current_row > 0)
        self.next_button.setEnabled(self.current_row < self.log_list.count() - 1)
        
    def select_previous_log(self):
        """
        Selects the previous log in the log list.
        """
        self.log_list.setCurrentRow(self.current_row - 1)
        
    def select_next_log(self):
        """
        Selects the next log in the log list.
        """
        self.log_list.setCurrentRow(self.current_row + 1)
        
    def toggle_dark_theme(self, checked: bool):
        """
        Toggles the dark theme.
        """
        if checked:
            self.setPalette(styling.DARK_PALETTE)
        else:
            self.setPalette(styling.LIGHT_PALETTE)
        
    # def get_colors(self):

    #     for role in QtG.QPalette.ColorRole:
    #         role_colors = []
    #         for group in QtG.QPalette.ColorGroup:
    #             color = self.palette().color(group, role).toRgb()
    #             role_colors.append((group, color.red(), color.green(), color.blue(), color.alpha()))
                
    #         different = False
    #         for i in range(1, 5):
    #             color_set = set()
    #             for j in range(len(role_colors)):
    #                 color_set.add(role_colors[j][i])
    #             if len(color_set) > 1:
    #                 different = True
    #                 break
    #         if not different:
    #             color = role_colors[0]
    #             print(f'DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.{role}, QtG.QColor({color[1]}, {color[2]}, {color[3]}, {color[4]}))')
    #         else:
    #             for group in role_colors:
    #                 print(f'DARK_PALETTE.setColor(QtG.QPalette.{group[0]}, QtG.QPalette.{role}, QtG.QColor({group[1]}, {group[2]}, {group[3]}, {group[4]}))')
      

if __name__ == "__main__":
    application = QtW.QApplication(sys.argv)
    window = LogBrowser()
    window.show()
    sys.exit(application.exec())
