from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton

KV = '''
Screen:
    MDTopAppBar:
        title: "My App"
        pos_hint: {"top": 1}
        elevation: 4
        right_action_items: [["magnify", lambda x: app.search()], ["dots-vertical", lambda x: app.menu_open()]]
    MDRaisedButton:
        id: button
        text: "Open Menu"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.menu_open()
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        """Initialize menu after KV file is loaded."""
        menu_items = [
            {
                "text": f"Option {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]

        # Accessing 'button' ID is now safe
        self.menu = MDDropdownMenu(
            caller=self.root.ids.button,  
            items=menu_items,
            width_mult=4
        )

    def menu_open(self):
        """Opens the dropdown menu."""
        self.menu.open()

    def menu_callback(self, text_item):
        """Handles menu item selection."""
        print(f"Selected: {text_item}")
        self.menu.dismiss()  

TestApp().run()
