from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout

KV = '''
BoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MDTabs Example"
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: "white"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch

        Tab:
            title: "Home"
            icon: "home"
            MDLabel:
                text: "Welcome to Home Tab"
                halign: "center"

        Tab:
            title: "Profile"
            icon: "account"
            MDLabel:
                text: "This is your Profile"
                halign: "center"

        Tab:
            title: "Settings"
            icon: "cog"
            MDLabel:
                text: "Settings Page"
                halign: "center"
        Tab:
            title: "Messages"
            icon: "message-bookmark"
            MDLabel:
                text: "Messages and notifications"
                halign: "center"
'''

class Tab(BoxLayout, MDTabsBase):
    pass

class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print(f"Switched to tab: {tab_text}")

TestApp().run()

