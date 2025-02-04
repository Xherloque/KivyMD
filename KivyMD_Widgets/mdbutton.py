from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp

# MDButton comes in different styles like FlatButton, RaisedButton, IconButton, and FAB.
class MyApp(MDApp):
    def build(self):
        return MDRaisedButton(
            text="Click Me",pos_hint = {
                "center_x": 0.5, "center_y": 0.5
                },
            on_release=lambda x: print("Button Pressed!")
        )

MyApp().run()
