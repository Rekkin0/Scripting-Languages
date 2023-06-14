import PySide6.QtWidgets as QtW
from datetime import datetime

from Note import Note


class Notebook(QtW.QListWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__notes = []

    @property
    def notes(self) -> list[Note]:
        return self.__notes

    def __len__(self) -> int:
        return len(self.notes)

    def __iter__(self) -> iter:
        return iter(self.notes)

    def __getitem__(self, id: int) -> Note:
        return self.notes[id]

    def __setitem__(self, id: int, note: Note) -> None:
        self.notes[id] = note

    def index(self, note: Note) -> int:
        return self.notes.index(note)

    def add(
        self,
        title: str,
        scheduled: bool = False,
        scheduled_at: datetime = datetime.now(),
        content: str = "",
        tags: list[str] = [],
        created_at: datetime = datetime.now(),
    ) -> Note:
        note = Note(
            title=title,
            scheduled=scheduled,
            scheduled_at=scheduled_at,
            content=content,
            tags=tags,
            created_at=created_at,
        )
        self.addItem(note)
        self.notes.append(note)
        return note

    def update(self, id: int, note: Note) -> None:
        self.notes[id] = note

    def remove(self, id: int) -> Note:
        self.takeItem(id)
        return self.notes.pop(id)
    
    def relocate(self, note: Note) -> None:
        self.notes.remove(note)
        self.notes.insert(self.row(note), note)
