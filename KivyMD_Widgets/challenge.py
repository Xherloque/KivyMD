from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
"""# Challenge: Build a Simple UI
    Create a basic KivyMD app using MDLabel, MDRaisedButton, and MDTextField.
    Center the widgets using MDFloatLayout.
    When the button is clicked, print whatever is in the text field."""

std_marks = {
    "John Doe": 50,
    "John D2": 40,
    "Cliff Joe": 70,
    "Kevin NS": 99,
    "Lara FB": 100,
    "Rory JS": 88
}
def simple_searching(lst,search_item):
    r_value = []
    for string in lst:
        if search_item in string:
            r_value.append(string)
    return r_value
         
class StudentsGrades(MDApp):
    def build(self):
        self.layout = MDFloatLayout()
        
        self.student_labels = []  # Track created labels
        self.atEdit = []
        self.editGrid = []
        # The heading/ header
        label_1 = MDLabel(text="Students Marks",
                          halign="center",
                          pos_hint={
                              "center_x": 0.5, "center_y":0.97
                          }, underline=True,
                          bold=True,
                          font_size= 38)
        
        self.layout.add_widget(label_1)
        search_box = MDTextField(hint_text="Search For A Student",
                        pos_hint={"center_x": 0.5, "center_y": 0.9},
                        size_hint_x=0.4)
        self.layout.add_widget(search_box)
        search_but = MDRaisedButton(text="Search",
                                 pos_hint={
                                     "center_x":0.8,
                                     "center_y":0.9
                                 },size_hint_x=0.1)
        search_but.bind(on_release = lambda x: self.searched_student(search_box.text))
        self.layout.add_widget(search_but)
        
        switch_label = MDLabel(text="Show Student List",
                               font_size=30,
                               pos_hint={"center_x":0.8,
                                         "center_y": 0.8})
        show_list_switch = MDSwitch(pos_hint={"center_x":0.5,
                                         "center_y": 0.8})
        show_list_switch.bind(active=self.show_list)
        self.layout.add_widget(switch_label)
        self.layout.add_widget(show_list_switch)
        
    
        menu_items = [{"text": key, "on_release": lambda x=key: self.menu_callback(x)} for key in std_marks.keys()]

        menu_button = MDRaisedButton(text="Show List",
                                     pos_hint={"center_x":0.8,"center_y":0.5},
                                     )
        self.un_pettite_menu = MDDropdownMenu(caller=menu_button,
                                         items=menu_items, width_mult=4,
                                         pos_hint={"center_x":0.5,"center_y":0.5})
        menu_button.bind(on_release=lambda x: self.un_pettite_menu.open())
        self.layout.add_widget(menu_button)
        
        comp_list_label = MDLabel(text= "Satisfied?!", pos_hint={"center_x":0.6,
                                                                   "center_y":0.3})
        comp_list_check = MDCheckbox(pos_hint={"center_x":0.7,
                                                "center_y":0.3})
        self.layout.add_widget(comp_list_label)
        self.layout.add_widget(comp_list_check)
        return self.layout
    
    def menu_callback(self, option):
        print(f"Selected: {option}")
        self.un_pettite_menu.dismiss()
        
    def show_list(self, switch, value):
        # Store student labels in a list for easy removal
        if value:  # If switch is ON
            for std, mark in std_marks.items():
                lb = MDLabel(text=f"{std}: {mark}",
                            pos_hint={"center_x": 0.5, "center_y": 0.7 - (0.05 * list(std_marks).index(std))})
                self.layout.add_widget(lb)
                lb_btn = MDRaisedButton(text="Edit",pos_hint = lb.pos_hint)
                nom = lb.text.split(":")[0]
                # print(nom)
                lb_btn.bind(on_release=lambda x, name=nom: self.edit_student(name))
                self.layout.add_widget(lb_btn)
                self.student_labels.append(lb)  # Store label reference
                self.student_labels.append(lb_btn)  # Store label reference
        else:  # If switch is OFF
            for label in self.student_labels:
                self.layout.remove_widget(label)  # Remove only student labels
            self.student_labels.clear()  # Empty the list
    def edit_student(self, name):
        print("Editing:", name)
        self.atEdit.clear()
        
        # Remove previous editing grid if it exists
        if self.editGrid:
            self.layout.remove_widget(self.editGrid[0])
            self.editGrid.clear()

        self.atEdit.append(name)
        
        if name in std_marks.keys():
            small_grid = GridLayout(rows=4, cols=2,  # Fix: Increased rows to 4
                                    size_hint_y=0.5,
                                    pos_hint={"center_x": 0.5, "center_y": 0.35})
            self.editGrid.append(small_grid)

            # Store original values
            first_name, last_name = name.split(" ")
            marks = str(std_marks[name])

            # Create input fields
            self.fn_input = TextInput(text=first_name, size_hint_y=0.35)
            self.ln_input = TextInput(text=last_name, size_hint_y=0.35)
            self.marks_input = TextInput(text=marks, size_hint_y=0.35, input_filter="int")  # Restrict to numbers
            
            # Add widgets to GridLayout
            small_grid.add_widget(MDLabel(text="First Name:"))
            small_grid.add_widget(self.fn_input)
            small_grid.add_widget(MDLabel(text="Last Name:"))
            small_grid.add_widget(self.ln_input)
            small_grid.add_widget(MDLabel(text="Marks:"))
            small_grid.add_widget(self.marks_input)

            # Add Save button
            save_button = MDRaisedButton(text="Save Changes", size_hint_y=0.5)
            save_button.bind(on_release=lambda x: self.save_changes(name))
            small_grid.add_widget(save_button)

            # Add the small grid to the layout
            self.layout.add_widget(small_grid)

    def save_changes(self, old_name):
        new_fn = self.fn_input.text.strip()
        new_ln = self.ln_input.text.strip()
        new_marks = self.marks_input.text.strip()

        # Ensure valid input
        if not new_fn or not new_ln or not new_marks.isdigit():
            print("Invalid input! All fields must be filled correctly.")
            return

        new_name = f"{new_fn} {new_ln}"
        std_marks[new_name] = int(new_marks)  # Update marks dictionary

        # If name changed, remove old entry
        if new_name != old_name:
            del std_marks[old_name]

        print("Updated Student List:", std_marks)

        # Refresh UI
        self.layout.remove_widget(self.editGrid[0])  # Remove edit form
        self.editGrid.clear()
        self.show_list(None, True)  # Refresh student list

    def searched_student(self, search_text):
        # Clear previous search results
        for label in self.student_labels:
            self.layout.remove_widget(label)
        self.student_labels.clear()

        if search_text:
            rs = simple_searching(list(std_marks.keys()), search_text)
            if rs:
                for index, name in enumerate(rs): 
                    lb = MDLabel(text=f"{name}: {std_marks[name]}",
                                pos_hint={"center_x": 0.5, "center_y": 0.7 - (0.05 * index)})
                    self.layout.add_widget(lb)
                    self.student_labels.append(lb)  # Track labels
                return  # Exit early if we added results
        
        # Show "Not Found" if empty or no match
        lb = MDLabel(text=f"{search_text} Not Found",
                    pos_hint={"center_x": 0.5, "center_y": 0.7})
        self.layout.add_widget(lb)
        self.student_labels.append(lb)

StudentsGrades().run()
        
        
