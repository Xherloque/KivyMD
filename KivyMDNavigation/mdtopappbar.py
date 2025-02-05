# We're now at **MDTopAppBar**, which is part of **Navigation Components**.  

# ### **📌 MDTopAppBar (Previously Known as MDToolbar)**
# The **MDTopAppBar** is the top navigation bar in an app. It usually contains:  
# - A **title** (app name or section title).  
# - **Navigation button** (like a menu button to open `MDNavigationDrawer`).  
# - **Action buttons** (like search, settings, notifications).  


from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDTopAppBar

KV = '''
MDNavigationLayout:
    ScreenManager:
        Screen:
            MDTopAppBar:
                title: "My App"
                pos_hint: {"top": 1}
                elevation: 4
                md_bg_color: app.theme_cls.primary_color
                specific_text_color: "black"
                left_action_items: [["menu", lambda x: app.open_nav_drawer()], ["arrow-left", lambda x: app.go_back()]]
                right_action_items: [["magnify", lambda x: app.search()], ["dots-vertical", lambda x: app.show_options()]]

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

    def open_nav_drawer(self):
        self.root.ids.nav_drawer.set_state("open")

    def search(self):
        print("Search Clicked")

    def show_options(self):
        print("Options Clicked")
        
    def go_back(self):
        print("Going BAck")

TestApp().run()

# 1. **`MDTopAppBar`** creates the top navigation bar.
# 2. **`pos_hint: {"top": 1}`** makes sure it sticks to the top.
# 3. **`left_action_items`** adds a **menu** button that can open a drawer.
# 4. **`right_action_items`** adds icons for **search** and **more options**.
# 5. **When buttons are clicked**, they call the app's methods (`open_nav_drawer()`, `search()`, `show_options()`).

# ---

# ### **🔥 Customization**
# - **Change background color** → `md_bg_color: app.theme_cls.primary_color`
# - **Make it floating** → Add `specific_text_color: "white"`
# - **Add a back button** → `left_action_items: [["arrow-left", lambda x: app.go_back()]]`
