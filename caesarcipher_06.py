#
#   CAESAR CIPHER - PART 6 
#   Add a GUI
#   - by JeffGames
#   
#
#
# ToDo: 
# 1. Add JeffGames icon

from tkinter import * # Import tkinter, our GUI framework

root = Tk()

# Define what happens when the go button is clicked

def clickAlpha():
    if btnAlpha1:
        print ("Alpha 1 clicked")
        return
    else:
        print ("Other button")
        return

def clickGo():
    msgOutput.insert(0, msgInput)
    print("Clicked go button") # Log button click 

def clickClear():
    msgInput.delete(0, END)
    msgOutput.delete(0, END)
    print("Cleared all messages")

def clickCopy():
    return
    
def clickQuit(): # Created to have a pop-up to confirm quit.
    btnExit(command=root.quit) # This doesn't work. Need to figure out why

# SET UP THE CANVAS
root.title("Caeser Cipher by JeffGames")


#   ---------------------------------------------------
#   SET UP THE BUTTONS, Message boxes, and input areas
#   ---------------------------------------------------

# Welcome message

# Welcome to the Caesar Cypher program. Please choose below if you would 
# like to encrypt or decrypt a message



# Encrypt / Decrypt user choices
lblWelcome = Label(root, text="STEP 1 - Press a button to Encrypt or Decrypt a message")
btnCrypt1 = Button(root, text="Encrypt", command=ACTIVE) 
btnCrypt2 = Button(root, text="Decrypt") 


# Alphabet choices
lblAlphaChoice = Label(root, text=" STEP 2 - Now choose your encryption algo")
btnAlpha1 = Button(root, text="Alphabet 1", command=clickAlpha) 
btnAlpha2 = Button(root, text="Alphabet 2", command=clickAlpha) 
btnAlpha3 = Button(root, text="Alphabet 3", command=clickAlpha) 

# Input message box with a heading instructing user to paste or type message
lblMsgIn = Label(root, text="STEP 3 - Copy or paste your message here")
msgInput = Entry(root)

# Button to engage the encryption algo
# NB: Maybe make it say Encrypt or Decrypt based on the user choice above

btnGo =  Button(root, text="GO!", command=clickGo)

#Output box
msgOutput = Entry(root)

# Clear, Copy to clipboard, and Exit  buttons
btnClear = Button(root, text="Clear All", command=clickClear)   
btnCopy = Button(root, text="Copy to clipboard", command=clickCopy)
btnExit = Button(root, text="Quit", command=root.quit)

#   -----------------------------
#   PUT THE BUTTONS ON THE SCREEN
#   -----------------------------

# ROW 0 - Welcome message
lblWelcome.grid(row=0, column=0, columnspan =3)

# ROW 1 - Encrypt Decrypt button placement
btnCrypt1.grid(row= 1, column=0)
btnCrypt2.grid(row= 1, column=1)

# ROW 2 - Choose Alphabet message
lblAlphaChoice.grid(row=2, column=0, columnspan =3)

# ROW 3- Alphabet button placement
btnAlpha1.grid(row= 3, column=0)
btnAlpha2.grid(row= 3, column=1)
btnAlpha3.grid(row= 3, column=2)

# ROW 4 - Message input heading
lblMsgIn.grid(row=4, column=0, columnspan =3)
# ROW 5 - Message input area 
msgInput.grid(row =5, column=0, columnspan =3)

# ROW 6 - Go button placement
btnGo.grid(row= 6, column=1)

# ROW 7 - Message output heading


# ROW 8 - Message output area
msgOutput.grid(row =8, column=0, columnspan =3)

# ROW 9 - Clear Messages & Copy to clipboard, Exit program button placement
btnClear.grid(row =9, column=0)
btnCopy.grid(row=9, column=1)
btnExit.grid(row=9, column=2)

# tkinter mainloop
root.mainloop()
