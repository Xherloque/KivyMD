from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(MDApp):
    def build(self):
        layout = AnchorLayout()
        
        # Create button
        button = MDRaisedButton(
            text="Open Menu",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        # Menu items
        menu_items = [
            {"text": "Option 1", "on_release": lambda: self.menu_callback("Option 1")},
            {"text": "Option 2", "on_release": lambda: self.menu_callback("Option 2")},
            {"text": "Option 3", "on_release": lambda: self.menu_callback("Option 3")},
        ]

        # Create dropdown menu
        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4
        )

        # Corrected binding to prevent passing extra argument
        button.bind(on_release=lambda x: self.menu.open())

        layout.add_widget(button)
        return layout

    def menu_callback(self, option):
        print(f"Selected: {option}")
        self.menu.dismiss()

MyApp().run()
