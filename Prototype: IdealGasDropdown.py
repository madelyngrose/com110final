from tkinter import *

class IdealGasLaw:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("2000x2000") #Sets window size
        self.root.title("Ideal Gas Law Calculator") #Titles window
        self.options = ["Pressure", "Volume", "Moles", "Temperature"] #Provides options for the initial dropdown menu
        self.selection = StringVar()
        self.selection.set("What value would you like to find?") #Initial prompt for user
        self.drop = OptionMenu(self.root, self.selection, *self.options)
        self.drop.pack()
        self.button1 = Button(self.root, text="Select", command=self.show) #Button that confirms the user's choice from the dropdown menu
        self.button1.pack()
        self.label = Label(self.root, text=" ")
        self.label.pack()
        self.user_input_values = {} #Creates a dictionary that the user values will be stored in
        self.root.mainloop()

    def user_input(self, variable):
        label = Label(self.root, text=variable) #Provides labels based on what values the user should have, given what they want to solve
        label.pack()
        textbox = Entry(self.root)
        textbox.pack()
        return textbox

    def show(self):
        selected = self.selection.get()

        if selected not in self.user_input_values:
            if selected == "Pressure":
                variables = ["Volume in Liters", "Number of Moles", "Temperature in Kelvin"]
            elif selected == "Volume":
                variables = ["Pressure in Bars", "Number of Moles", "Temperature in Kelvin"]
            elif selected == "Moles":
                variables = ["Pressure in Bars", "Volume in Liters", "Temperature in Kelvin"]
            elif selected == "Temperature":
                variables = ["Pressure in Bars", "Number of Moles", "Volume in Liters"]

            self.user_input_values[selected] = [self.user_input(f"Enter {param}") for param in variables]

        values = [float(entry.get()) for entry in self.user_input_values[selected]] #Obtains the values input by the user
        
#Solves for the selected variable 
        if selected == "Pressure":
            volume, moles, temp = values
            pressure = (moles * 0.0831446 * temp) / volume
            output = ("The pressure is",pressure,"bars")

        elif selected == "Volume":
            pressure, moles, temp = values
            volume = (moles * 0.0831446 * temp) / pressure
            output = ("The volume is",volume,"liters")

        elif selected == "Moles":
            pressure, volume, temp = values
            moles = (pressure * volume) / (0.0831446 * temp)
            output = ("There are",moles,"moles present")

        elif selected == "Temperature":
            pressure, moles, volume = values
            temp = (pressure * volume) / (0.0831446 * moles)
            output = ("The temperature is",temp,"Kelvin")

        self.label.config(text=output) Prints the output of the variable of interest

IdealGasLaw()

"""
References:
https://docs.python.org/3/library/tkinter.html
How to create dropdown menu using tkinter: https://www.geeksforgeeks.org/dropdown-menus-tkinter/
"""
