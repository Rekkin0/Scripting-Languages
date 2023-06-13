import PySide6.QtWidgets as QtW
from datetime import datetime


class Note(QtW.QListWidgetItem):
    def __init__(
        self,
        title: str,
        scheduled: bool = False,
        scheduled_at: datetime = datetime.now(),
        content: str = "",
        tags: list[str] = [],
        created_at: datetime = datetime.now(),
    ) -> None:
        super().__init__(title)
        self.__title = title
        self.__scheduled = scheduled
        self.__scheduled_at = scheduled_at
        self.__content = content
        self.__tags = tags
        self.__created_at = created_at

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def scheduled(self) -> bool:
        return self.__scheduled
    
    @property
    def scheduled_at(self) -> datetime:
        return self.__scheduled_at

    @property
    def content(self) -> str:
        return self.__content

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def tags(self) -> list[str]:
        return self.__tags

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title
        
    @scheduled.setter
    def scheduled(self, scheduled: bool) -> None:
        self.__scheduled = scheduled
        
    @scheduled_at.setter
    def scheduled_at(self, scheduled_at: datetime) -> None:
        self.__scheduled_at = scheduled_at

    @content.setter
    def content(self, content: str) -> None:
        self.__content = content

    @tags.setter
    def tags(self, tags: list[str]) -> None:
        self.__tags = tags
        
    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)
        
    def remove_tag(self, tag: str) -> None:
        self.tags.remove(tag)

    def update(
        self,
        title: str = None,
        scheduled: bool = None,
        scheduled_at: datetime = None,
        content: str = None,
        tags: list[str] = None,
    ) -> None:
        if title:
            self.setText(title)
            self.title = title
        if scheduled:
            self.scheduled = scheduled
        if scheduled_at:
            self.scheduled_at = scheduled_at
        if content:
            self.content = content
        if tags:
            self.tags = tags
