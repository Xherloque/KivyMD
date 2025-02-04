from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.floatlayout import MDFloatLayout

class MyApp(MDApp):
    def build(self):
        layout = MDFloatLayout()
        switch = MDSwitch(pos_hint={"center_x": 0.5, "center_y": 0.8})
        check = MDCheckbox(pos_hint={"center_x": 0.5, "center_y": 0.1})
        but = MDIconButton(text="I'm an icon Button",pos_hint = {
                "center_x": 0.6, "center_y": 0.9
                },
            on_release=lambda x: print("Button Pressed!")
        )
        layout.add_widget(switch)
        layout.add_widget(check)
        layout.add_widget(but)
        
        return layout
    
    
MyApp().run()
