from tkinter import *
import  tkinter as tk

class ideal_gas_law():
#Adapted from the tutorial found on https://www.geeksforgeeks.org/dropdown-menus-tkinter/ 
    def __init__(self):
        self.root = Tk() #If you want to keep using a class, initialize the function with only this
        self.root.geometry("2000x2000") #Sets the size of the window
        self.options = [ #Provides the options for the initial dropdown menu
        "Pressure", 
        "Volume", 
        "Moles", 
        "Temperature"]
        self.selection = StringVar() #Selection becomes string
        self.selection.set("What value would you like to find?") #Initial value for the dropdown menu
        self.drop = OptionMenu(self.root, self.selection, *self.options) #Displaying dropdown menu options
        self.drop.pack()
        self.button1 = Button(self.root, text="Select", command=self.show) #Displays the button that confirms dropdown option
        self.button1.pack()
        self.label = Label(self.root, text=" ") 
        self.label.pack()
        self.root.mainloop()
        self.canvas1 = tk.Canvas(self.root, width=400, height=300)
        self.canvas1.pack()
        self.entry1 = tk.Entry(self.root) 
        self.canvas1.create_window(200, 140, window=self.entry1)

    def show(self): 
        selected = self.selection.get()
        self.label.config(text=selected)

        if selected == "Pressure":
            root = tk.Tk()
            volume = tk.Label(root, text="Enter Volume in Liters")
            volume.pack()
            textbox1 = tk.Entry(root)
            textbox1.pack()

            moles = tk.Label(root, text="Enter Number of Moles")
            moles.pack()
            textbox2 = tk.Entry(root)
            textbox2.pack()

            temp = tk.Label(root, text="Enter Temperature in Kelvin")
            temp.pack()
            textbox3 = tk.Entry(root)
            textbox3.pack()
            
            print(pressure, 'bars')

        elif selected == "Volume":
            root = tk.Tk()
            pressure = tk.Label(root, text="Enter Pressure in Bars")
            pressure.pack()
            textbox1 = tk.Entry(root)
            textbox1.pack()

            moles = tk.Label(root, text="Enter Number of Moles")
            moles.pack()
            textbox2 = tk.Entry(root)
            textbox2.pack()

            temp = tk.Label(root, text="Enter Temperature in Kelvin")
            temp.pack()
            textbox3 = tk.Entry(root)
            textbox3.pack()

            volume = (moles*.0831446*temp)/pressure
            print(volume)

        elif selected == "Moles":
            root = tk.Tk()
            pressure = tk.Label(root, text="Enter Pressure in Bars")
            pressure.pack()
            textbox1 = tk.Entry(root)
            textbox1.pack()

            volume = tk.Label(root, text="Enter Volume in Liters")
            volume.pack()
            textbox2 = tk.Entry(root)
            textbox2.pack()

            temp = tk.Label(root, text="Enter Temperature in Kelvin")
            temp.pack()
            textbox3 = tk.Entry(root)
            textbox3.pack()

            moles = (pressure*volume)/(.0831446*temp)
            print(moles)

        elif selected == "Temperature":
            root = tk.Tk()
            pressure = tk.Label(root, text="Enter Pressure in Bars")
            pressure.pack()
            textbox1 = tk.Entry(root)
            textbox1.pack()

            moles = tk.Label(root, text="Enter Number of Moles")
            moles.pack()
            textbox2 = tk.Entry(root)
            textbox2.pack()

            volume = tk.Label(root, text="Enter Volume in Liters")
            volume.pack()
            textbox3 = tk.Entry(root)
            textbox3.pack()

            temp = (pressure*volume)/(.0831446*moles)
            print(temp)

ideal_gas_law()
