import math
import tkinter as tk

from Approximator import Approximator

class App:
    def __init__(self, master):
        self.master = master
        master.title("Aprroximate sin(x)")

        # Input field
        self.input_label = tk.Label(master, text="Enter your input:")
        self.input_label.pack()
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        # Dropdown menu for units
        self.units_label = tk.Label(master, text="Select units:")
        self.units_label.pack()
        self.selected_units = tk.StringVar(master, "radians")
        self.units_dropdown = tk.OptionMenu(master, self.selected_units, "radians", "degrees")
        self.units_dropdown.pack()

        # Approximation degree field
        self.approx_label = tk.Label(master, text="Enter approximation degree:")
        self.approx_label.pack()
        self.approx_entry = tk.Entry(master)
        self.approx_entry.pack()

        # Button
        self.button = tk.Button(master, text="Submit", command=self.display_output)
        self.button.pack()

        # Output field
        self.output_label = tk.Label(master, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(master)
        self.output_text.pack()

    def display_output(self):
        approximator = Approximator() # long time no programming in python, i do not remeber how to make it global for class

        input_value = self.input_entry.get()
        units = self.selected_units.get()
        approx_degree = self.approx_entry.get()
        self.output_text.delete('1.0', tk.END)  # Clear previous output
        for i in range(1,int(approx_degree)):
            aproximatedValue = approximator.approx(float(input_value),int(i),units)
            realValue = math.sin(float(input_value))
            difference = abs(aproximatedValue-realValue)
            #casting it to only show 2 after decimal point
            aproximatedValue = f"{aproximatedValue:.4f}"
            realValue = f"{realValue:.4f}"
            difference = f"{difference:.6f}"
            output_value = f"my approximation is : {aproximatedValue}" \
                           f"\tTrue value is: {realValue}" \
                           f"\tdifference by: {difference}\n"
            #self.output_text.insert(tk.END, output_value)




root = tk.Tk()
app = App(root)
root.mainloop()
