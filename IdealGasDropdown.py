from tkinter import *

class IdealGasLaw:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("2000x2000")
        self.options = ["Pressure", "Volume", "Moles", "Temperature"]
        self.selection = StringVar()
        self.selection.set("What value would you like to find?")
        self.drop = OptionMenu(self.root, self.selection, *self.options)
        self.drop.pack()
        self.button1 = Button(self.root, text="Select", command=self.show)
        self.button1.pack()
        self.label = Label(self.root, text=" ")
        self.label.pack()
        self.user_input_values = {}
        self.root.mainloop()

    def user_input(self, variable):
        label = Label(self.root, text=variable)
        label.pack()
        textbox = Entry(self.root)
        textbox.pack()
        return textbox

    def show(self):
        selected = self.selection.get()

        if selected not in self.user_input_values:
            if selected == "Pressure":
                variables = ["Volume", "Moles", "Temperature"]
            elif selected == "Volume":
                variables = ["Pressure", "Moles", "Temperature"]
            elif selected == "Moles":
                variables = ["Pressure", "Volume", "Temperature"]
            elif selected == "Temperature":
                variables = ["Pressure", "Moles", "Volume"]

            self.user_input_values[selected] = [self.user_input(f"Enter {param}") for param in variables]

        values = [float(entry.get()) for entry in self.user_input_values[selected]]

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