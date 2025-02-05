# The MDNavigationDrawer allows 
# users to swipe from the left to access a menu with app options.
# The MDNavigationDrawer in KivyMD allows you to create a side menu, similar to what you see in many mobile apps (like Gmail). It slides in from the left when activated.
# Basic Structure of MDNavigationDrawer

# MDNavigationDrawer works inside MDBoxLayout with two main sections:

#     MDNavigationLayout (The container for the drawer and main screen)
#     MDNavigationDrawer (The actual sliding menu)
#     MDBoxLayout (The main content area)

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

KV = '''
MDBoxLayout:

    MDNavigationLayout:

        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Navigation Drawer"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    MDRaisedButton:
                        text: "Press Me"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                orientation: 'vertical'
                spacing: "8dp"
                padding: "8dp"

                MDLabel:
                    text: "Menu"
                    font_style: "H5"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDBoxLayout:
                    MDIconButton:
                        icon: "home"
                    MDRaisedButton:
                        text: "Home"
                        on_release: nav_drawer.set_state("close")  

                MDBoxLayout:
                    MDIconButton:
                        icon: "account"
                    MDRaisedButton:
                        text: "Profile"
                        on_release: nav_drawer.set_state("close")

                MDBoxLayout:
                    MDIconButton:
                        icon: "cog"
                    MDRaisedButton:
                        text: "Settings"
                        on_release: nav_drawer.set_state("close")
'''


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()
