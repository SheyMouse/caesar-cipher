#
#   CAESAR CIPHER - PART 6
#	Add a GUI
#
#


from tkinter import * # Import tkinter, our GUI framework

root = Tk()

# Define what happens when the go button is clicked

def clickAlpha():
	return

def clickGo():
	msgOutput.insert(0, "You clicked go")

def clickClear():
	msgInput.delete(0, END)

# SET UP THE CANVAS
root.title("Caeser Cipher by JeffGames")

# 	---------------------------------------------------
# 	SET UP THE BUTTONS, Message boxes, and input areas
# 	---------------------------------------------------

# Welcome message

# Welcome to the Caesar Cypher program. Please choose below if you would 
# like to encrypt or decrypt a message

#lblWelcome = (root, "Test")


# Encrypt / Decrypt user choices
btnCrypt1 = Button(root, text="Encrypt") 
btnCrypt2 = Button(root, text="Decrypt") 

# Alphabet choices
btnAlpha1 = Button(root, text="Alphabet 1") 
btnAlpha2 = Button(root, text="Alphabet 2") 
btnAlpha3 = Button(root, text="Alphabet 3") 

# Input message box with a heading instructing user to paste or type message
msgInput = Entry(root)

# Button to engage the encryption algo
# NB: Maybe make it say Encrypt or Decrypt based on the user choice above

btnGo =  Button(root, text="GO!", command=clickGo) #, padx = 50, pady =25)

#Output box
msgOutput = Entry(root)

# Clear, Copy to clipboard, and Exit  buttons
btnClear = Button(root, text="Clear", command=clickClear)	

# 	-----------------------------
# 	PUT THE BUTTONS ON THE SCREEN
# 	-----------------------------

# ROW 0 - Welcome message
#lblWelcome.grid(row=0, column=0)

# ROW 1 - Encrypt Decrypt button placement
btnCrypt1.grid(row= 1, column=0)
btnCrypt2.grid(row= 1, column=1)

# ROW 2 - Choose Alphabet message

# ROW 3- Alphabet button placement
btnAlpha1.grid(row= 3, column=0)
btnAlpha2.grid(row= 3, column=1)
btnAlpha3.grid(row= 3, column=2)

# ROW 4 - Message input heading

# ROW 5 - Message input area 
msgInput.grid(row =5, column=0, columnspan =3)

# ROW 6 - Go button placement
btnGo.grid(row= 6, column=1)

# ROW 7 - Message output heading


# ROW 8 - Message output area
msgOutput.grid(row =8, column=0, columnspan =3)

# ROW 9 - Clear Messages & Copy to clipboard, Exit program button placement
btnClear.grid(row =9, column=0)

# tkinter mainloop
root.mainloop()
