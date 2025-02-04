from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

# This is the KivyMD version of a label. It supports theme colors and different text styles.
class MyApp(MDApp):
    def build(self):
        return MDLabel(
            text="Hello, KivyMD!",
            halign="center",  # Centers the text
            theme_text_color="Primary"  # Uses the primary theme color
        )

MyApp().run()
