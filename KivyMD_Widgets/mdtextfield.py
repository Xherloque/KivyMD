from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField

class MyAPP(MDApp):
    def build(self):
        layout = MDFloatLayout()
        button = MDRoundFlatButton(
                    text="Click Me",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
        # Used to take user input with a modern material style.
        txtfield = MDTextField(
                        hint_text="Enter your name",
                        pos_hint={"center_x": 0.5, "center_y": 0.6},
                        size_hint_x=0.8
                        )
        layout.add_widget(button)
        layout.add_widget(txtfield)
        return layout
    
MyAPP().run()
        