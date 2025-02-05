from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton

KV = '''
MDGridLayout:
    cols: 3  # Two columns
    spacing: dp(10)
    padding: dp(20)

    MDRaisedButton:
        text: "Button 1"
    
    MDRaisedButton:
        text: "Button 2"

    MDRaisedButton:
        text: "Button 3"
    
    MDRaisedButton:
        text: "Button 4"
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()
