from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

KV = '''
ScreenManager:
    Screen:
        name: "home"
        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                text: "Home Screen"
                halign: "center"
            MDRaisedButton:
                text: "Go to Settings"
                on_release: app.change_screen("settings")

    Screen:
        name: "settings"
        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                text: "Settings Screen"
                halign: "center"
            MDRaisedButton:
                text: "Back to Home"
                on_release: app.change_screen("home")
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name  # Switches screens

MyApp().run()
"""
Switching Screens with NavigationDrawer

You can also switch screens using the sidebar menu (MDNavigationDrawer) like this:

MDNavigationDrawer:
    MDList:
        OneLineListItem:
            text: "Home"
            on_release: 
                root.current = "home"
                nav_drawer.set_state("close")  # Close drawer after clicking
"""