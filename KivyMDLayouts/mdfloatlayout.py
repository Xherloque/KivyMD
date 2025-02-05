from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRoundFlatButton

# Unlike BoxLayout, MDFloatLayout lets you place widgets at absolute positions using pos_hint.
class MyAPP(MDApp):
    def build(self):
        layout = MDFloatLayout()
        button = MDRoundFlatButton(
                    text="Click Me",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
        layout.add_widget(button)
        return layout
    
MyAPP().run()
        