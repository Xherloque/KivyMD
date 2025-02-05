from kivy.lang import Builder
from kivymd.app import MDApp

"""
It creates a persistent bottom bar that lets users switch between different screens.

💡 Example Structure:

    Each tab has an icon and text label.
    Uses MDBottomNavigationItem to define sections.
    
"""

KV = '''
BoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Bottom Navigation Example"
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: "white"

    MDBottomNavigation:
        panel_color: app.theme_cls.primary_dark  # Background color

        MDBottomNavigationItem:
            name: "home"
            text: "Home"
            icon: "home"

            MDLabel:
                text: "Welcome to Home Screen"
                halign: "center"

        MDBottomNavigationItem:
            name: "profile"
            text: "Profile"
            icon: "account"

            MDLabel:
                text: "This is your Profile"
                halign: "center"

        MDBottomNavigationItem:
            name: "settings"
            text: "Settings"
            icon: "cog"

            MDLabel:
                text: "Settings Page"
                halign: "center"
'''

class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

TestApp().run()
