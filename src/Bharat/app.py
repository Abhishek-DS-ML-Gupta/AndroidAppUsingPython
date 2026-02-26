import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class SurakshakApp(toga.App):
    def __init__(self, formal_name, app_id):
        super().__init__(formal_name=formal_name, app_id=app_id)
    
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Outer box (vertical)
        outer_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                align_items="center",
                flex=1,
                margin=30,
                background_color="#f5f5f5"  # soft milky background
            )
        )

        # Title
        label = toga.Label(
            "Welcome to Bharat!",
            style=Pack(
                font_size=28,
                font_weight="bold",
                color="#333333",
                margin=(0,0,20,0)
            )
        )
        outer_box.add(label)

        # Subtitle
        subtitle = toga.Label(
            "Your modern milky-themed Toga app",
            style=Pack(
                font_size=16,
                color="#666666",
                margin=(0,0,30,0)
            )
        )
        outer_box.add(subtitle)

        # Buttons row
        buttons_box = toga.Box(style=Pack(direction=ROW, align_items="center"))

        button1 = toga.Button(
            "Click Me",
            on_press=self.on_click,
            style=Pack(
                padding=(12,25),
                background_color="#ffffff",
                color="#007acc",
                font_size=16,
                font_weight="bold",
                margin=(0, 10, 0, 0)  # right margin for spacing
            )
        )

        button2 = toga.Button(
            "Secondary",
            on_press=self.on_click_secondary,
            style=Pack(
                padding=(12,25),
                background_color="#e0e0e0",
                color="#333333",
                font_size=16,
                font_weight="bold",
                margin=(0, 0, 0, 10)  # left margin for spacing
            )
        )

        buttons_box.add(button1)
        buttons_box.add(button2)

        outer_box.add(buttons_box)

        # Footer
        footer = toga.Label(
            "Made with ❤️ by Abhishek",
            style=Pack(font_size=12, color="#999999", margin=(30,0,0,0))
        )
        outer_box.add(footer)

        self.main_window.content = outer_box
        self.main_window.show()

    def on_click(self, widget):
        self.main_window.info_dialog("Milky UI", "Primary button clicked!")

    def on_click_secondary(self, widget):
        self.main_window.info_dialog("Milky UI", "Secondary button clicked!")

def main():
    return SurakshakApp("Bharat", "com.abhishekgupta.bharat")