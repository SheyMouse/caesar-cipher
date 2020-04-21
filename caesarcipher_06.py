#
#   CAESAR CIPHER - PART 6
#	Add a GUI
#
#


from tkinter import * # Import tkinter, our GUI framework

root = Tk()

# SET UP THE CANVAD



# SET UP THE BUTTONS

# Welcome message



# Encrypt / Decrypt user choices

# Alphabet choices
button_alpha1 = Button(root, text="Alphabet 1", padx = 50, pady =50)
button_alpha2 = Button(root, text="Alphabet 2", padx = 50, pady =50)
button_alpha3 = Button(root, text="Alphabet 3", padx = 50, pady =50)

# Message box with a heading instructing user to paste or type message

# Button to engage the encryption algo
# NB: Maybe make it say Encrypt or Decrypt based on the user choic above

button_go =  Button(root, text="GO!", padx = 50, pady =50)

#Output box

# Clear button and Copy to clipboard

# PUT THE BUTTONS ON THE SCREEN

button_alpha1.grid(row= 1, column=1)
button_alpha2.grid(row= 1, column=2)
button_alpha3.grid(row= 1, column=3)

button_go.grid(row= 2, column=2)

root.mainloop()
