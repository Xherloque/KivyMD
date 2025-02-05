from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

KV = '''
Screen:

    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: "Gradient Navigation Drawer"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDLabel:
                        text: "Main Content Here"
                        halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            CustomGradientDrawer:
'''

class CustomGradientDrawer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            # First Color (Top)
            Color(0.2, 0.4, 0.8, 1)  # Dark Blue
            self.rect1 = Rectangle(size=self.size, pos=self.pos)

            # Second Color (Bottom)
            Color(0.5, 0.1, 0.7, 1)  # Purple
            self.rect2 = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect1.size = self.size
        self.rect1.pos = self.pos

        self.rect2.size = self.size
        self.rect2.pos = (self.x, self.y + self.height / 2)  # Start halfway down

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestApp().run()
