from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDBoxLayout:

    MDNavigationLayout:

        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    pos_hint: {"top": 1}
                    MDTopAppBar:
                        title: "Navigation Drawer"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        
                        elevation: 4
                    MDRaisedButton:
                        text: "Press Me"
                      

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 10, 10, 0)

            BoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"

                FitImage:
                    source: "media/profile.jpeg"  # Replace with your image
                    size_hint_y: .35
                    pos_hint: {"center_x": 0.5}
                    radius: [100, 100, 100, 100] #Rounded pic

                MDSeparator:
                    height: "1dp"

                MDList:
                    OneLineIconListItem:
                        text: "Profile"
                        IconLeftWidget:
                            icon: "account"

                    OneLineIconListItem:
                        text: "Settings"
                        IconLeftWidget:
                            icon: "cog"

                    OneLineIconListItem:
                        text: "Logout"
                        on_release: nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "logout"

'''


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()
