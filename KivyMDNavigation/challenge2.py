# A personal to-watch movies store
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
import datetime
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class MovieItem(MDBoxLayout):
    title = StringProperty()  # This allows KV to use "text: root.title"


#Features:
    # A place to add a movie to alist which will be stored alongside the date and time it
        # was added #an Add Movie + / select if it is a series, where you've reached/ where 
            # to start & a textfield for comments on it
    # A list of all the stored movies with a checkbox to say if it has been watched or not
        #  plus 3 options buttons alongside each movie with 'delete' and 'edit' button
    # A pic if there is of that movie/series
    # Settings to change the themes...
    # In the navigation, an icon to change the way the movies are ordered
    
KV = '''
<MovieItem@MDBoxLayout>:
    orientation: "horizontal"
    spacing: dp(10)
    adaptive_height: True

    MDLabel:
        text: root.title
        size_hint_x: 0.6
    
    MDCheckbox:
        size_hint_x: 0.1
        on_active: app.toggle_watched(root.title)

    MDIconButton:
        icon: "dots-vertical"
        on_release: app.more_options()

ScreenManager:
    Screen:
        name: "home"
        
        MDBoxLayout:
            orientation: 'vertical'
            
            
            MDTopAppBar:
                title: "Home"
                pos_hint: {"top": 1}
                elevation: 4
                md_bg_color: app.theme_cls.primary_color
                specific_text_color: "black"
                left_action_items: [["menu", lambda x: app.open_nav_drawer()]]
                right_action_items: [["movie-plus", lambda x: app.add_new_movie()], ["dots-vertical", lambda x: app.more_options()]]
                id: topbar

            # Hidden button for dropdown caller
            MDRaisedButton:
                id: dropdown_caller
                opacity: 0  # Makes it invisible
                size_hint: None, None
                size: "1dp", "1dp"  # Minimal size

            MDBoxLayout:
                adaptive_height: True

                MDIconButton:
                    icon: 'magnify'

                MDTextField:
                    id: search_field
                    hint_text: 'Search icon'
                    on_text: app.search(self.text)

            RecycleView:
                id: rv
                viewclass: 'MovieItem'
                key_viewclass: 'viewclass'
                key_size: 'height'

                RecycleBoxLayout:
                    padding: dp(10)
                    default_size: None, dp(80)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'

                                
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 10, 10, 0)
            BoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"

                FitImage:
                    source: "media/profile.jpeg" 
                    size_hint_y: .35
                    pos_hint: {"center_x": 0.5}
                    radius: [100, 100, 100, 100] #Rounded pic

                MDSeparator:
                    height: "1dp"

                MDList:
                    OneLineIconListItem:
                        text: "Profile"
                        on_release: 
                            root.current = "profile"
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "account-edit"
                        

                    OneLineIconListItem:
                        text: "Settings"
                        on_release: 
                            root.current = "settings"
                            nav_drawer.set_state("close")
                            
                        IconLeftWidget:
                            icon: "cog"
                        

                    OneLineIconListItem:
                        text: "Exit"
                        on_release: nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: "exit-to-app"
            
    Screen:
        name: "profile"
        BoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "My Profile"
                md_bg_color: app.theme_cls.primary_color
                specific_text_color: "white"
                left_action_items: [["home", lambda x: app.change_screen("home")]]

            MDTabs:
                id: tabs
                on_tab_switch: app.on_tab_switch

                Tab:
                    title: "Personal Dets"
                    icon: "account-badge"
                    MDLabel:
                        text: "We Change Names, Pic, DOB will go here..."
                        halign: "center"

                Tab:
                    title: "Favorites"
                    icon: "file-star"
                    MDLabel:
                        text: "All the favorite films' list will go here"
                        halign: "center"

                Tab:
                    title: "Messages"
                    icon: "message-bookmark"
                    MDLabel:
                        text: "Messages and notifications"
                        halign: "center"
    Screen:
        name: "settings"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Profile"
            MDLabel:
                text: "Settings Screen"
                halign: "center"
            MDRaisedButton:
                text: "Back to Home"
                on_release: app.change_screen("home")
    Screen:
        name: "add_movie"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "ADD A NEW MOVIE"
            MDLabel:
                text: "A form will be added here"
                halign: "center"
            MDRaisedButton:
                text: "ADD"
                on_release:
                    app.apply_changes() 
                    app.change_screen("home")
            

'''
DUMMY_ITEMS = [{"title":"Merlin",
               "Series": True,
               "Seasons": 5,
               "More Details":"Very Age Friendly",
               "Date Recorded": "12/12/2024"},
               {"title":"Creed",
               "Series": False,
               "Seasons": None,
               "More Details":"Fierce-Action Packed",
               "Date Recorded": "02/02/2025"},
               {"title":"Love And Thunder",
               "Series": False,
               "Seasons": None,
               "More Details":"Best Marvels Work Yet",
               "Date Recorded": "1/08/2024"}]

class Tab(BoxLayout, MDTabsBase):
    pass

class MyMovies(MDApp):    
    def build(self):
        # We'll need a couple of constants to handle different logic
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    
    def change_screen(self, screen_name):
        self.root.current = screen_name 
        
    def open_nav_drawer(self):
        self.root.ids.nav_drawer.set_state("open")
        
    def search(self,text):
        print("Searching For.... {}".format(text))
        #  How to add stuff here?
    def add_new_movie(self):
        self.change_screen("add_movie")
        
    def apply_changes(self):
        print("applying changes")
    
    def on_start(self):
        """Populate RecycleView with movie data."""
        self.root.ids.rv.data = [
            {"viewclass": "MovieItem", "title": movie["title"]} for movie in DUMMY_ITEMS
        ]
        """Initialize the dropdown menu when the app starts."""
        # Define menu items
        menu_items = [
            {
                "text": f"Option {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Option {i}": self.menu_callback(x),
            } for i in range(3)
        ]
        
        # Create the dropdown menu with hidden caller
        self.menu = MDDropdownMenu(
            caller=self.root.ids.dropdown_caller,  # Hidden button as caller
            items=menu_items,
            width_mult=4
        )

    def more_options(self):
        """Position the hidden button and open menu."""
        # Position the hidden button near the "dots-vertical"
        toolbar = self.root.ids.topbar
        x, y = toolbar.to_window(toolbar.width - 0, toolbar.height+460)  # Adjust position
        self.root.ids.dropdown_caller.pos = (x, y)

        # Open menu
        self.menu.open()


    
    def menu_callback(self, text_item):
        print(text_item)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print(f"Switched to tab: {tab_text}")
    

    def toggle_watched(self, title):
        """Marks a movie as watched or unwatched."""
        print(f"Marked '{title}' as watched/unwatched")


   
    
MyMovies().run()