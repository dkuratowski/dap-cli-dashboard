from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class DefaultDashboard(App):
    # BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
