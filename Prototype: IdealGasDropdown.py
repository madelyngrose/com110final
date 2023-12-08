from tkinter import *

class IdealGasLaw:
    def __init__(self):
        self.root = Tk()
        self.root.title("Ideal Gas Law Calculator")
        self.root.geometry("2000x2000") #Set window size
        self.options = ["Pressure", "Volume", "Moles", "Temperature"] #Variable options for the dropdown menu
        self.selection = StringVar()
        self.selection.set("What value would you like to find?") #Starting selected variable that prompts the user to select a variable
        self.drop = OptionMenu(self.root, self.selection, *self.options)
        self.drop.pack()
        self.submission = Button(self.root, text="Select", command=self.show) #Creates a button for the user to confirm their selection choice
        self.submission.pack()
        self.label = Label(self.root, text=" ")
        self.label.pack()
        self.user_input_values = {} #Creates a dictionary to store the user inputs (utilized in line 29)
        self.root.mainloop()

    def user_input(self, variable):
        label = Label(self.root, text=variable) #Will label each of the text boxes according to the known variables
        label.pack()
        textbox = Entry(self.root) #Creates text box for users to import their known variables
        textbox.pack()
        return textbox

    def show(self):
        selected = self.selection.get()

        if selected not in self.user_input_values: #If what is selected is not in the dictionary (empty dictionary, so this should apply to everything)
            if selected == "Pressure": #Selected dropdown variable
                variables = ["Volume in Liters", "Number of Moles", "Temperature in Kelvin"] #Prompts for known user variables
            elif selected == "Volume":
                variables = ["Pressure in Bars", "Number of Moles", "Temperaturein Kelvin"]
            elif selected == "Moles":
                variables = ["Pressure in Bars", "Volume in Liters", "Temperature in Kelvin"]
            elif selected == "Temperature":
                variables = ["Pressure in Bars", "Number of Moles", "Volume in Liters"]

            self.user_input_values[selected] = [self.user_input("Enter", param) for param in variables]

        values = [float(entry.get()) for entry in self.user_input_values[selected]] #Retrieve entry

        #Calculate the selected variable using the ideal gas law
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

        self.label.config(text=output)

IdealGasLaw()

"""
References:
https://docs.python.org/3/library/tkinter.html
How to create dropdown menu using tkinter: https://www.geeksforgeeks.org/dropdown-menus-tkinter/
"""
