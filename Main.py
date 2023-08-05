# Link to helpful plugin and existing code
# https://copyassignment.com/get-any-country-date-and-time-using-python/
# This program is a Time Zone Converter
# Input one "other" person's location/time zone, and then input your location/timezone
# The program will tell you what their time is relevant to you

# Requirements: 9/9
# The user can view instructions if they click the associated button
# The user can provide input by selecting from the drop downs and pressing buttons
# A GUI and the information it contains is output to the display
# This program uses variables of type String, Boolean, and Integer
# The GUI has 4 Menu Buttons for user options
# This file has 12 functions, including TimeZoneConverter's constructor and main()
# self.time_zones is a saved List of all common timezones from the pytz package
# This program uses 2 while and 3 for loops
# This program uses the pytz, datetime, and tkinter package/library

# Package for timezones
import pytz
# Package for printing current dates and times
from datetime import datetime
# Package for GUIs
import tkinter as tk
import tkinter.font as tk_text

# Defines the GUI elements
class TimeZoneConverter(tk.Frame):
    def __init__(self, parent_window):
        super().__init__(parent_window)

        # Variables to track data and changes in the program
        self.time_zones = pytz.common_timezones
        self.is_day_before_month = True
        self.current_other_location = ""
        self.current_your_location = ""
        self.current_time_difference = 0

        # Data type of menu text
        self.clicked_other_zone = tk.StringVar()
        # Initial dropdown text
        self.clicked_other_zone.set("Africa/Abidjan")

        self.clicked_your_zone = tk.StringVar()
        self.clicked_your_zone.set("Africa/Abidjan")

        # Sets the name, color, and size of the top level widget
        self.parent_window = parent_window
        self.parent_window.title("Time Zone Converter")
        self.parent_window.geometry("1350x490")
        self.parent_window.minsize(1350, 490)
        self.parent_window.maxsize(1350, 490)
        self.parent_window.configure(bg = "Cyan")

        # Creates the frames other widgets are grouped into
        self.left_frame = tk.Frame(self.parent_window, bg = "DarkCyan", padx = 10, pady = 10)
        self.left_frame.place(anchor = 'w', relx = 1, rely = 1)
        self.left_frame.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.upper_right_frame = tk.Frame(self.parent_window, bg = "DarkCyan", padx = 10, pady = 10)
        self.upper_right_frame.place(anchor = 'n', relx = 1, rely = 1)
        self.upper_right_frame.pack(side = tk.TOP, padx = 10, pady = 10)

        self.lower_right_frame = tk.Frame(self.parent_window, bg = "DarkCyan", padx = 10, pady = 10)
        self.lower_right_frame.place(anchor = 'n', relx = 1, rely = 1)
        self.lower_right_frame.pack(side = tk.TOP, padx = 10, pady = 10)

        # Font that will be used for the widgets
        self.font_family = tk_text.Font(family = "Helvetica")
        self.font_size = 15

        # Empty space to go between the left frame widgets, 1 space
        self.left_widget_spacing1 = tk.Label(self.left_frame, text = " ", bg = "DarkCyan")
        self.left_widget_spacing2 = tk.Label(self.left_frame, text = " ", bg = "DarkCyan")

        # Create the text boxes in the left frame
        self.general_info_output = tk.Text(self.left_frame, wrap = tk.WORD, fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 15, width = 75)
        self.general_info_output.insert(tk.INSERT, "\t  _____________Welcome to the Time Zone Converter!_____________\n\n")
        self.general_info_output.config(state = tk.DISABLED)
        self.general_info_output.grid(row = 0, column = 0)
        self.left_widget_spacing1.grid(row = 1, column = 0)

        self.other_date_time_output = tk.Text(self.left_frame, wrap = tk.WORD, fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 75)
        self.other_date_time_output.insert(tk.INSERT, "Other Date/Time Will Appear Here")
        self.other_date_time_output.config(state = tk.DISABLED)
        self.other_date_time_output.grid(row = 2, column = 0)
        self.left_widget_spacing2.grid(row = 3, column = 0)

        self.your_date_time_output = tk.Text(self.left_frame, wrap = tk.WORD, fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 75)
        self.your_date_time_output.insert(tk.INSERT, "Your Date/Time Will Appear Here")
        self.your_date_time_output.config(state = tk.DISABLED)
        self.your_date_time_output.grid(row = 4, column = 0)

        # Empty space to go between the upper right widget buttons, 1 space
        self.button_spacing1 = tk.Label(self.upper_right_frame, text = " ", bg = "DarkCyan")
        self.button_spacing2 = tk.Label(self.upper_right_frame, text = " ", bg = "DarkCyan")
        self.button_spacing3 = tk.Label(self.upper_right_frame, text = " ", bg = "DarkCyan")

        # Button that explains the program
        self.tutorial_button = tk.Button(self.upper_right_frame, text = "Tutorial", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8, command = self.Tutorial)
        self.tutorial_button.grid(row = 0, column = 0)
        self.button_spacing1.grid(row = 0, column = 1)

        # Button that displays all selectable locations
        self.all_locations_button = tk.Button(self.upper_right_frame, text = "Regions", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8, command = self.DisplayLocations)
        self.all_locations_button.grid(row = 0, column = 2)
        self.button_spacing2.grid(row = 0, column = 3)

        # Button that swaps day/month for user readability
        self.day_month_button = tk.Button(self.upper_right_frame, text = "D/M", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8, command = self.SwapDayMonth)
        self.day_month_button.grid(row = 0, column = 4)
        self.button_spacing3.grid(row = 0, column = 5)

        # Button that exits the application
        self.quit_button = tk.Button(self.upper_right_frame, text = "Quit", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8, command = self.Quit)
        self.quit_button.grid(row = 0, column = 6)

        # Empty space to go between the lower right frame widgets, 1 space
        self.right_widget_spacing1 = tk.Label(self.lower_right_frame, text = " ", bg = "DarkCyan")
        self.right_widget_spacing2 = tk.Label(self.lower_right_frame, text = " ", bg = "DarkCyan")
        self.right_widget_spacing3 = tk.Label(self.lower_right_frame, text = " ", bg = "DarkCyan")
        self.right_widget_spacing4 = tk.Label(self.lower_right_frame, text = " ", bg = "DarkCyan")

        # Creates the drop down menu for selecting the other time zone
        self.other_dropdown_name = tk.Label(self.lower_right_frame, text = "Other:", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8)
        self.other_dropdown_name.grid(row = 0, column = 0)
        self.other_dropdown_label = tk.Label(self.lower_right_frame, text = "Nothing Selected", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 29)
        self.other_dropdown_label.grid(row = 0, column = 1)
        self.right_widget_spacing1.grid(row = 1, column = 0)

        self.other_dropdown_menu = tk.OptionMenu(self.lower_right_frame, self.clicked_other_zone, *self.time_zones)
        self.other_dropdown_menu.grid(row = 2, column = 1)

        self.other_dropdown_button = tk.Button(self.lower_right_frame, text = "Select", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8, command = self.UpdateOtherLocationDropdownText)
        self.other_dropdown_button.grid(row = 2, column = 0)
        self.right_widget_spacing2.grid(row = 3, column = 0)

        # Creates the drop down menu for selecting your time zone
        self.your_dropdown_name = tk.Label(self.lower_right_frame, text = "You:", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8)
        self.your_dropdown_name.grid(row = 4, column = 0)
        self.your_dropdown_label = tk.Label(self.lower_right_frame, text = "Nothing Selected", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 29)
        self.your_dropdown_label.grid(row = 4, column = 1)
        self.right_widget_spacing3.grid(row = 5, column = 0)

        self.other_dropdown_menu = tk.OptionMenu(self.lower_right_frame, self.clicked_your_zone, *self.time_zones)
        self.other_dropdown_menu.grid(row = 6, column = 1)

        self.your_dropdown_button = tk.Button(self.lower_right_frame, text = "Select", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8, command = self.UpdateYourLocationDropdownText)
        self.your_dropdown_button.grid(row = 6, column = 0)
        self.right_widget_spacing4.grid(row = 7, column = 0)

        # Creates the label to display the difference in time between time zones
        self.time_difference_name = tk.Label(self.lower_right_frame, text = "Result:", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 8)
        self.time_difference_name.grid(row = 8, column = 0)
        self.time_difference = tk.Label(self.lower_right_frame, text = "Can't Determine Yet", fg = "white", bg = "DarkSlateGrey",
            font = (self.font_family, self.font_size), height = 1, width = 29)
        self.time_difference.grid(row = 8, column = 1)

    # Changes text in general info output to explain the app
    def Tutorial(self):
        self.general_info_output.config(state = tk.NORMAL)
        self.general_info_output.delete("1.0", tk.END)
        self.general_info_output.insert(tk.INSERT, "\t  _____________Welcome to the Time Zone Converter!_____________\n\n" +
            "Here's a short tutorial on my program, Time Zone Coverter! The Regions button pulls up " +
            "every country and time zone you could select, the D/M button toggles the Day/Month " +
            "appearance, and the Quit button will exit this program.\n\n" +
            "The dropdowns below the buttons are where you select the times zones that will be compared. " +
            "Give it your time zone and one other time zone, and the program will give you back " +
            "how many hours ahead or behind you are!")
        self.general_info_output.config(state = tk.DISABLED)

    # Changes text in general info output to view all the selectable regions
    def DisplayLocations(self):
        self.general_info_output.config(state = tk.NORMAL)
        self.general_info_output.delete("1.0", tk.END)
        self.general_info_output.insert(tk.INSERT, "\t  _____________Welcome to the Time Zone Converter!_____________\n\n" +
            f"{self.time_zones}")
        self.general_info_output.config(state = tk.DISABLED)

    # Swaps the day & month position everywhere they are printed
    def SwapDayMonth(self):
        self.general_info_output.config(state = tk.NORMAL)
        self.general_info_output.delete("1.0", tk.END)
        self.general_info_output.insert(tk.INSERT, "\t  _____________Welcome to the Time Zone Converter!_____________\n\n" +
            "The position of the day and the month in the labels below have been swapped. Look at the D/M button if you " +
            "happen to forget the order.")
        self.general_info_output.config(state = tk.DISABLED)

        # If true, make it false, and vice versa
        self.is_day_before_month = not self.is_day_before_month
        
        if self.is_day_before_month:
            self.day_month_button["text"] = "D/M"
        else:
            self.day_month_button["text"] = "M/D"

        self.UpdateOtherDateTime()
        self.UpdateYourDateTime()

    # Destroys every widget, stops mainloop(), terminates program
    def Quit(self):
        self.parent_window.destroy()

    # Changes the text shown on the other location dropdown menu
    def UpdateOtherLocationDropdownText(self):
        self.other_dropdown_label.config(text = self.clicked_other_zone.get())
        self.UpdateOtherDateTime()
        self.UpdateTimeDifferenceResult()

    # Changes the text shown on the your location dropdown menu
    def UpdateYourLocationDropdownText(self):
        self.your_dropdown_label.config(text = self.clicked_your_zone.get())
        self.UpdateYourDateTime()
        self.UpdateTimeDifferenceResult()

    # Changes the text for the other date/time if a location is selected
    def UpdateOtherDateTime(self):
        # Get text from selected location to compare
        text = self.other_dropdown_label.cget("text")

        for x in self.time_zones:
            # If selected location is one of the pytz time zones
            if text == x:
                # Save the current location to be used for calculating the time difference
                self.current_other_location = text
                # Find the date and time of that time zone
                zone = pytz.timezone(text)
                time = datetime.now(zone)
                full_string = ""

                if self.is_day_before_month:
                    full_string = time.strftime(f"In {text} the Day is %d/%m/%y and the Time is %H:%M:%S")
                else:
                    full_string = time.strftime(f"In {text} the Day is %m/%d/%y and the Time is %H:%M:%S")

                self.other_date_time_output.config(state = tk.NORMAL)
                self.other_date_time_output.delete("1.0", tk.END)
                self.other_date_time_output.insert(tk.INSERT, full_string)
                self.other_date_time_output.config(state = tk.DISABLED)
                return

    # Changes the text for your date/time if a location is selected
    def UpdateYourDateTime(self):
        text = self.your_dropdown_label.cget("text")

        for x in self.time_zones:
            if text == x:
                self.current_your_location = text
                zone = pytz.timezone(text)
                time = datetime.now(zone)
                full_string = ""

                if self.is_day_before_month:
                    full_string = time.strftime(f"In {text} the Day is %d/%m/%y and the Time is %H:%M:%S")
                else:
                    full_string = time.strftime(f"In {text} the Day is %m/%d/%y and the Time is %H:%M:%S")

                self.your_date_time_output.config(state = tk.NORMAL)
                self.your_date_time_output.delete("1.0", tk.END)
                self.your_date_time_output.insert(tk.INSERT, full_string)
                self.your_date_time_output.config(state = tk.DISABLED)
                return

    # Determines if the other and your location have been selected before updating the time difference text
    def UpdateTimeDifferenceResult(self):
        is_other_flag_cleared = False
        is_your_flag_cleared = False

        for x in self.time_zones:
            if self.current_other_location == x:
                is_other_flag_cleared = True
            if self.current_your_location == x:
                is_your_flag_cleared = True;

        if is_other_flag_cleared and is_your_flag_cleared:
            self.CalculateTimeDifference()

    # Calculates how many hours you are ahead or behind the other location
    def CalculateTimeDifference(self):
        is_behind = False
        full_string = ""

        other_zone = pytz.timezone(self.current_other_location)
        other_time = datetime.now(other_zone)
        other_hour = int(other_time.strftime(f"%H"))
        other_day = int(other_time.strftime(f"%d"))

        your_zone = pytz.timezone(self.current_your_location)
        your_time = datetime.now(your_zone)
        your_hour = int(your_time.strftime(f"%H"))
        your_day = int(your_time.strftime(f"%d"))

        self.current_time_difference = other_hour - your_hour
        self.current_time_difference = abs(self.current_time_difference)

        # In this case, we can simply go with the difference between the hours
        if other_day == your_day:
            if other_hour <= your_hour:
                is_behind = False
            else:
                is_behind = True

        # Can't go with the difference, the hours ahead/behind will be off
        # Must count up from the time zone that is behind until they are equal
        # The number of times it was incremented is the real hour difference
        elif other_day < your_day:
            is_behind = False
            i = 0

            while other_hour != your_hour:
                other_hour = other_hour + 1
                i = i + 1

                if other_hour == 24:
                    other_hour = 0

            self.current_time_difference = i

        elif your_day < other_day:
            is_behind = True
            i = 0

            while other_hour != your_hour:
                your_hour = your_hour + 1
                i = i + 1

                if your_hour == 24:
                    your_hour = 0

            self.current_time_difference = i

        if is_behind:
            full_string = f"You are {self.current_time_difference} hours behind."
        else:
            full_string = f"You are {self.current_time_difference} hours ahead."

        self.time_difference.config(text = full_string)

def main():
    parent_window = tk.Tk()
    time_zone_converter = TimeZoneConverter(parent_window)
    # Causes tkinter to run and update visually
    time_zone_converter.mainloop()

if __name__ == "__main__":
    main()