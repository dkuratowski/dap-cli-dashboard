from typing import Optional

from textual.app import ComposeResult
from textual.widget import Widget


class Panel(Widget):
    def __init__(
        self,
        *children: Widget,
        caption: Optional[str] = None,
        name: Optional[str] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ) -> None:
        super().__init__(
            *children,
            name=name,
            id=id,
            classes=classes,
        )
        self.caption = caption

    def compose(self) -> ComposeResult:
        for child in self.children:
            yield child
