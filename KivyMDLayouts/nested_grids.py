from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDGridLayout:
    cols: 1  # Main grid has 1 column to hold sections

    MDLabel:
        text: "Main Grid - Section 1"
        halign: "center"

    MDGridLayout:  # Nested Grid
        cols: 2
        spacing: dp(10)

        MDRaisedButton:
            text: "Button 1"
        
        MDRaisedButton:
            text: "Button 2"

        MDRaisedButton:
            text: "Button 3"

        MDRaisedButton:
            text: "Button 4"
    
    MDLabel:
        text: "Main Grid - Section 2"
        halign: "center"
'''

class NestedGridApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

NestedGridApp().run()
