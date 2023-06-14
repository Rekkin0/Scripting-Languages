import sys
import PySide6.QtWidgets as QtW
import PySide6.QtCore as QtC
import PySide6.QtGui as QtG
from datetime import datetime

import resources.styling as styling
import resources.constants as const

from Note import Note
from NotebookGUI import NotebookGUI
import NotebookDB


class NotebookApp(NotebookGUI):
    def __init__(self):
        super().__init__()
        self.note: Note
        self.note_selected: bool = False
        self.note_count = 0

        self.connect_signals()
        self.theme_button.toggle()

        NotebookDB.load_notes(self)

    def connect_signals(self):
        self.tray_restore.triggered.connect(self.show)
        self.tray_quit.triggered.connect(self.quit)
        self.tray_icon.activated.connect(self.tray_icon_activated)

        self.search_edit.textChanged.connect(self.search_notes)
        self.add_button.clicked.connect(self.add_note)
        self.delete_button.clicked.connect(self.delete_note)
        self.quit_button.clicked.connect(self.quit)

        self.scheduled_button.toggled.connect(self.toggle_scheduled)
        self.theme_button.toggled.connect(self.toggle_theme)
        self.discard_button.clicked.connect(self.update_note_editor)
        self.save_button.clicked.connect(self.edit_note)

        self.notebook.itemSelectionChanged.connect(self.update_note_editor)
        self.notebook.dropEvent = self.dropEvent

    def closeEvent(self, event: QtG.QCloseEvent):
        event.ignore()
        self.hide()

    def dropEvent(self, event: QtG.QDropEvent):
        super(QtW.QListWidget, self.notebook).dropEvent(event)
        self.notebook.relocate(self.note)
        NotebookDB.save_notes(self)

    def tray_icon_activated(self, reason: QtW.QSystemTrayIcon.ActivationReason):
        if reason == QtW.QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show()
            self.activateWindow()

    def quit(self):
        NotebookDB.save_notes(self)
        QtC.QCoreApplication.instance().quit()

    @QtC.Slot(str)
    def search_notes(self, query: str):
        query = query.strip().lower()
        for note in self.notebook:
            to_show = query in note.title.lower() or query in note.content.lower()
            in_tags = False
            for tag in note.tags:
                if query in tag.lower():
                    in_tags = True
                    break
            note.setHidden(not to_show and not in_tags)

    def add_note(self):
        self.note_count += 1
        self.note = self.notebook.add(
            title=f"New Note {self.note_count}",
            scheduled_at=datetime.now(),
            created_at=datetime.now(),
        )
        self.notebook.addItem(self.note)
        self.notebook.setCurrentItem(self.note)

    def delete_note(self):
        self.notebook.remove(self.notebook.currentRow())

    def update_note_editor(self):
        self.note = self.notebook.currentItem()
        if self.note is None:
            self.title_edit.clear()
            self.scheduled_button.setChecked(False)
            self.scheduled_edit_date.setDate(const.DEFAULT_INITIAL_DATE)
            self.scheduled_edit_time.setTime(const.DEFAULT_INITIAL_TIME)
            self.content_edit.clear()
            self.tags_edit.clear()
            self.created_at_edit.setDateTime(const.DEFAULT_INITIAL_DATETIME)
            self.update_interactability()
            return
        self.title_edit.setText(self.note.title)
        self.scheduled_button.setChecked(self.note.scheduled)
        self.scheduled_edit_date.setDate(
            QtC.QDate.fromString(
                self.note.scheduled_at.strftime(const.DEFAULT_DATE_FORMAT),
                const.DEFAULT_DATE_EDIT_CONVERSION_FORMAT,
            )
        )
        self.scheduled_edit_time.setTime(
            QtC.QTime.fromString(
                self.note.scheduled_at.strftime(const.DEFAULT_TIME_FORMAT),
                const.DEFAULT_TIME_EDIT_CONVERSION_FORMAT,
            )
        )
        self.content_edit.setText(self.note.content)
        self.tags_edit.setText(", ".join(self.note.tags))
        self.created_at_edit.setDateTime(
            QtC.QDateTime.fromString(
                self.note.created_at.strftime(const.DEFAULT_DATETIME_FORMAT),
                const.DEFAULT_DATETIME_CONVERSION_FORMAT,
            )
        )
        self.update_interactability()

    def update_interactability(self):
        note_selected = self.note is not None
        if self.note_selected == note_selected:
            return
        self.note_selected = note_selected
        self.delete_button.setEnabled(note_selected)
        self.title_label.setEnabled(note_selected)
        self.title_edit.setEnabled(note_selected)
        self.scheduled_button.setEnabled(note_selected)
        self.content_label.setEnabled(note_selected)
        self.content_edit.setEnabled(note_selected)
        self.tags_label.setEnabled(note_selected)
        self.tags_edit.setEnabled(note_selected)
        self.created_at_label.setEnabled(note_selected)
        self.created_at_edit.setEnabled(note_selected)
        self.discard_button.setEnabled(note_selected)
        self.save_button.setEnabled(note_selected)

    def edit_note(self):
        title = self.title_edit.text()
        scheduled = self.scheduled_button.isChecked()
        scheduled_at = datetime.combine(
            self.scheduled_edit_date.date().toPython(),
            self.scheduled_edit_time.time().toPython(),
        )
        content = self.content_edit.toPlainText()
        tags = self.tags_edit.text().split(", ")
        self.note.update(
            title=title,
            scheduled=scheduled,
            scheduled_at=scheduled_at,
            content=content,
            tags=tags,
        )
        NotebookDB.save_notes(self)

    def toggle_scheduled(self, checked: bool):
        self.scheduled_edit_date.setEnabled(checked)
        self.scheduled_edit_time.setEnabled(checked)

    def toggle_theme(self, checked: bool):
        if checked:
            app.setPalette(styling.DARK_PALETTE)
        else:
            app.setPalette(styling.LIGHT_PALETTE)


def main():
    global app
    app = QtW.QApplication(sys.argv)
    app.setStyle(styling.STYLE)
    app.setFont(const.DEFAULT_APP_FONT)
    notebook_app = NotebookApp()
    notebook_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
