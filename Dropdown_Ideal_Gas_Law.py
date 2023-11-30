from tkinter import *
class ideal_gas_law():
    def __init__(self):
        self.root = Tk() 
        self.root.geometry("2000x2000")
        self.options = [ 
        "Pressure", 
        "Volume", 
        "Moles", 
        "Temperature"]
        self.selection = StringVar()
        self.selection.set("What value would you like to find?")
        self.drop = OptionMenu(self.root, self.selection, *self.options)
        self.drop.pack()
        self.button = Button(self.root, text="Select", command=self.show)
        self.button.pack()
        self.label = Label(self.root, text=" ")
        self.label.pack
        self.root.mainloop()
    
    def show(self): 
        selected = self.selection.get()
        self.label.config(text=selected)
        if selected == "Pressure":
            volume = int(input('Enter volume in L: '))
            moles = int(input('Enter number of moles: '))
            temp = int(input('Emter temperature in Kelvin: '))
            pressure = (moles*.0831446*temp)/volume
            print(pressure, 'bars')
        elif selected == "Volume":
            pressure = int(input('Enter pressure in bars: '))
            moles = int(input('Enter number of moles: '))
            temp = int(input('Enter temperature in Kelvin: '))
            volume = (moles*.0831446*temp)/pressure
            print(volume)
        elif selected == "Moles":
            pressure = int(input('Enter pressure in bars: '))
            volume = int(input('Enter volume in L: '))
            temp = int(input('Enter temperature in Kelvin: '))
            moles = (pressure*volume)/(.0831446*temp)
        elif selected == "Temperature":
                pressure = int(input('Enter pressure in bars: '))
                moles = int(input('Enter number of moles: '))
                volume = int(input('Enter volume in L: '))
                temp = (pressure*volume)/(.0831446*moles)
                print(temp)

ideal_gas_law()