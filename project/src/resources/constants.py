import PySide6.QtCore as QtC
import PySide6.QtWidgets as QtW
import PySide6.QtGui as QtG
from pathlib import Path


# LOCALE
LOCALE = QtC.QLocale(QtC.QLocale.Language.English, QtC.QLocale.Country.UnitedStates)

# ALIGNMENT FLAGS
LEFT_ALIGN = QtC.Qt.AlignmentFlag.AlignLeft
RIGHT_ALIGN = QtC.Qt.AlignmentFlag.AlignRight
CENTER_ALIGN = QtC.Qt.AlignmentFlag.AlignCenter
TOP_ALIGN = QtC.Qt.AlignmentFlag.AlignTop
VERT_CENTER_ALIGN = QtC.Qt.AlignmentFlag.AlignVCenter

# SIZE POLICIES
FIXED_SIZE = QtW.QSizePolicy.Policy.Fixed
EXPANDING_SIZE = QtW.QSizePolicy.Policy.Expanding
MINIMUM_SIZE = QtW.QSizePolicy.Policy.Minimum
PREFERRED_SIZE = QtW.QSizePolicy.Policy.Preferred

# COMMONS
DEFAULT_APP_FONT = QtG.QFont("Segoe UI", 10)
DEFAULT_LABEL_SIZE = QtC.QSize(60, 0)
DEFAULT_LABEL_ALIGNMENT = LEFT_ALIGN | VERT_CENTER_ALIGN
DEFAULT_LABEL_FONT = QtG.QFont("Segoe UI", 11, QtG.QFont.Weight.Bold)
DEFAULT_SPACER_PARAMETERS = (0, 0, QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Minimum)
DEFAULT_INITIAL_DATETIME = QtC.QDateTime.currentDateTime()
DEFAULT_INITIAL_DATE = QtC.QDate.currentDate()
DEFAULT_INITIAL_TIME = QtC.QTime.currentTime()
DEFAULT_BUTTON_SIZE = QtC.QSize(125, 0)
DEFAULT_BUTTON_SIZE_POLICY = QtW.QSizePolicy(FIXED_SIZE, FIXED_SIZE)
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_DATE_EDIT_CONVERSION_FORMAT = "yyyy-MM-dd"
DEFAULT_TIME_FORMAT = "%H:%M:%S"
DEFAULT_TIME_EDIT_CONVERSION_FORMAT = "hh:mm:ss"
DEFAULT_DATETIME_FORMAT = f"{DEFAULT_DATE_FORMAT} {DEFAULT_TIME_FORMAT}"
DEFAULT_DATETIME_CONVERSION_FORMAT = (
    f"{DEFAULT_DATE_EDIT_CONVERSION_FORMAT} {DEFAULT_TIME_EDIT_CONVERSION_FORMAT}"
)
DEFAULT_DATE_EDIT_FORMAT = "d MMMM yyyy"
DEFAULT_TIME_EDIT_FORMAT = "hh:mm"
DEFAULT_DATETIME_EDIT_FORMAT = f"{DEFAULT_DATE_EDIT_FORMAT} {DEFAULT_TIME_EDIT_FORMAT}"
DEFAULT_INITIAL_ENABLED_STATE = False

# MAIN WINDOW
MAIN_WINDOW_TITLE = "Notebook"
MAIN_WINDOW_ICON = str(Path(__file__).parent / "icon.png")
MAIN_WINDOW_SIZE = QtC.QSize(800, 600)

# MAIN LAYOUT
MAIN_LAYOUT_MARGINS = QtC.QMargins(10, 5, 10, 10)

# SPLITTER
SPLITTER_COLLAPSIBLE = False

# SEARCH
SEARCH_LABEL = "Search"
SEARCH_LABEL_SIZE = DEFAULT_LABEL_SIZE
SEARCH_LABEL_ALIGNMENT = DEFAULT_LABEL_ALIGNMENT
SEARCH_LABEL_FONT = DEFAULT_LABEL_FONT

# NOTE LIST
NOTE_LIST_LABEL = "Notes"
NOTE_LIST_LABEL_SIZE = DEFAULT_LABEL_SIZE
NOTE_LIST_LABEL_ALIGNMENT = DEFAULT_LABEL_ALIGNMENT
NOTE_LIST_LABEL_FONT = DEFAULT_LABEL_FONT

# QUIT BUTTON
QUIT_BUTTON_LABEL = "Quit"

# ADD/DEL BUTTONS
ADD_BUTTON_LABEL = "+"
DEL_BUTTON_LABEL = "–"
DEL_BUTTON_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
ADD_DEL_BUTTON_SIZE = QtC.QSize(30, 25)
ADD_DEL_BUTTON_FONT = QtG.QFont("Segoe UI", 11)

# TITLE
TITLE_LABEL = "Title"
TITLE_LABEL_SIZE = DEFAULT_LABEL_SIZE
TITLE_LABEL_ALIGNMENT = DEFAULT_LABEL_ALIGNMENT
TITLE_LABEL_FONT = QtG.QFont("Segoe UI", 13, QtG.QFont.Weight.Bold)
TITLE_LABEL_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
TITLE_EDIT_FONT = QtG.QFont("Segoe UI", 11)
TITLE_EDIT_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# SCHEDULED
SCHEDULED_BUTTON_LABEL = "Scheduled At"
SCHEDULED_BUTTON_SIZE_POLICY = DEFAULT_BUTTON_SIZE_POLICY
SCHEDULED_BUTTON_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
SCHEDULED_LABEL_FONT = DEFAULT_LABEL_FONT
SCHEDULED_EDIT_DATE = DEFAULT_INITIAL_DATE
SCHEDULED_EDIT_DATE_FORMAT = DEFAULT_DATE_EDIT_FORMAT
SCHEDULED_EDIT_DATE_CALENDAR_POPUP = True
SCHEDULED_EDIT_DATE_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
SCHEDULED_EDIT_TIME = DEFAULT_INITIAL_TIME
SCHEDULED_EDIT_TIME_FORMAT = DEFAULT_TIME_EDIT_FORMAT
SCHEDULED_EDIT_TIME_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# CONTENT
CONTENT_LABEL = "Content"
CONTENT_LABEL_SIZE = DEFAULT_LABEL_SIZE
CONTENT_LABEL_ALIGNMENT = DEFAULT_LABEL_ALIGNMENT
CONTENT_LABEL_FONT = DEFAULT_LABEL_FONT
CONTENT_LABEL_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
CONTENT_EDIT_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# TAGS
TAGS_LABEL = "Tags"
TAGS_LABEL_SIZE = DEFAULT_LABEL_SIZE
TAGS_LABEL_ALIGNMENT = DEFAULT_LABEL_ALIGNMENT
TAGS_LABEL_FONT = DEFAULT_LABEL_FONT
TAGS_LABEL_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
TAGS_EDIT_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# CREATED AT
CREATED_AT_LABEL = "Created At"
CREATED_AT_LABEL_SIZE = DEFAULT_LABEL_SIZE
CREATED_AT_LABEL_ALIGNMENT = DEFAULT_LABEL_ALIGNMENT
CREATED_AT_LABEL_FONT = DEFAULT_LABEL_FONT
CREATED_AT_LABEL_ENABLED = DEFAULT_INITIAL_ENABLED_STATE
CREATED_AT_EDIT_DEFAULT_DATETIME = DEFAULT_INITIAL_DATETIME
CREATED_AT_EDIT_SIZE = DEFAULT_BUTTON_SIZE
CREATED_AT_EDIT_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# DISCARD BUTTON
DISCARD_BUTTON_LABEL = "Discard"
DISCARD_BUTTON_SIZE = DEFAULT_BUTTON_SIZE
DISCARD_BUTTON_SIZE_POLICY = DEFAULT_BUTTON_SIZE_POLICY
DISCARD_BUTTON_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# SAVE BUTTON
SAVE_BUTTON_LABEL = "Save"
SAVE_BUTTON_SIZE = DEFAULT_BUTTON_SIZE
SAVE_BUTTON_SIZE_POLICY = DEFAULT_BUTTON_SIZE_POLICY
SAVE_BUTTON_ENABLED = DEFAULT_INITIAL_ENABLED_STATE

# THEME BUTTON
THEME_BUTTON_LABEL = "Dark theme"
THEME_BUTTON_ALIGNMENT = CENTER_ALIGN
