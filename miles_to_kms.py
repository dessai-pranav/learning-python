from tkinter import *
window = Tk()
is_equal_label = Label(text = "is equal to")
is_equal_label.grid(row = 1, column = 0)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text = f"{km}")


window.title("Miles to kilometer Converter")

miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="km")
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2, column=1)































window.mainloop()