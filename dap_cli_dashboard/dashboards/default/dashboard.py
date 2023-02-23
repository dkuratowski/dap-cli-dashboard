from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Footer, Header, Static

from .views.panel import Panel


class DefaultDashboard(App):
    CSS_PATH = "dashboard.css"
    # BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Panel(
                Vertical(
                    Static("access_tokens"),
                    Static("account_users"),
                    Static("accounts"),
                    Static("courses"),
                    Static("favourites"),
                    Static("quizzes"),
                    Static("submissions"),
                    Static("users"),
                ),
                caption="Tables",
                id="table_list",
            ),
            Vertical(
                Static("Meta", id="meta"),
                Static("Job", id="job"),
                Static("Objects", id="objects"),
                id="table_details",
            ),
            id="main_container",
        )
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
