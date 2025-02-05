from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

#MDBoxLayout is similar to Kivy’s BoxLayout but styled for KivyMD.
# It organizes widgets horizontally or vertically.

class BoxLayoutExample(MDApp):
    def build(self):
        # Key Features
        # ✔ orientation="vertical" or "horizontal"
        # ✔ spacing=10 – Space between widgets
        # ✔ padding=20 – Space inside the layout
        
        layout = MDBoxLayout(orientation="horizontal", spacing=10, padding=20)
        
        label = MDLabel(text="Hello, KivyMD!", halign="center",pos_hint={
            "center_x":0.5, "center_y":0.8
        })
        layout.add_widget(label)
        for i in range(3):
            # pos_hint inside MDBoxLayout usually doesn't 
            # affect positioning since BoxLayout handles widget placement automatically.
            button = MDRaisedButton(text=f"Button {i+1}", size_hint_x=0.3)
            layout.add_widget(button)
        
        return layout

BoxLayoutExample().run()
