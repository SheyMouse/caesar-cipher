#
#   CAESAR CIPHER - PART 6 
#   Add a GUI
#   - by JeffGames
#   
#
#
# ToDo: 
# 1. Add JeffGames icon


# Import tkinter, our GUI framework
from tkinter import * # Import tkinter, our GUI framework

root = Tk()

# Variables used by the main program.
alphabet01 = 'GjlZCMaQKU"/-Xf$£\\mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k\'@hnIuVWsp'
alphabet02 = 'hkS*F>ucL/l-)VPB£iR\\ZUdI\'CQ$z(@?=f<ta:m#Wvp;~n!Yg."^sxMHNKDwybjr_,O%oq+TJGXAEe&'
alphabet03 = '(OIce$TnM=JvF?j<&X+S>i\\h"EY\'dK£,lq!Z@~QmbyD-wUWNsrV^H:fB.aPpkL_otC/);RzAGxg%*#u'

userChoice = ''

# Define what happens when the go button is clicked

def clickAlpha():
    print("Alphabet = ", algo.get()) # Calls algo and prints its value

def clickCrypt():
    print("Crypto = ", crypt.get()) # Calls crypt and prints its value

def moveCaesar(sld): # A variable must be in here for the function to work
    print("Shift = ", cesar.get()) # Calls cesar variable and prints its value
    
def clickGo():
    global newMessage
    #msgOutput.insert(0, newMessage)
    print("Clicked go button") # Log button click 
    print(msgInput.get())
    
    if algo == 1:
        useAlpha = alphabet01
        print(alphabet01)
    elif algo == 2:
        useAlpha = alphabet02
    else:
        useAlpha = alphabet03

    for character in str(msgInput):
        if character in useAlpha:
            position = useAlpha.find(character)
            # NB: len(alphabet) handles a list of any length
            newPosition = (position + cesar.get())%len(useAlpha) 
            newCharacter = useAlpha[newPosition]
            newMessage += newCharacter
            print(newMessage.get())
        else:
            newMessage += character
            #print(str(newMessage))

def clickClear():
    msgInput.delete(0, END)
    msgOutput.delete(0, END)
    print("Cleared all messages")

def clickCopy():
    return
    
def clickQuit(): # Created to have a pop-up to confirm quit.
    btnExit(command=root.quit) # This doesn't work. Need to figure out why

# List for radio buttons.
ALPHAS = [
    ("Alphabet 1", "Alpha1"),
    ("Alphabet 2", "Alpha3"),
    ("Alphabet 3", "Alpha3"),
]

# Set up for the Alphabet being used. Alphabet 1 is default
algo = StringVar()
algo.set("Alpha1") # Sets Alphabet 1 as default
print("Initial alphabet: ", algo.get()) # Calls algo.set and prints its value

# Set up for the encrypt being used. Encrypt is default
crypt = StringVar()
crypt.set("Crypt1") # Sets Encrypt as default
print("Crypto choice: ", crypt.get()) # Calls crypt and prints its value

# Set up for the Casar shift. 0 is the default
cesar = IntVar()
cesar.set(0)
print("Initial shift: ", cesar.get()) # Calls cesar variable and prints its value

newMessage = StringVar()
newMessage.set("")

# SET UP THE CANVAS
root.title("Caeser Cipher by JeffGames")


#   ---------------------------------------------------
#   SET UP THE BUTTONS, Message boxes, and input areas
#   ---------------------------------------------------

# Welcome message
welcFrame = LabelFrame(root, padx=10, pady=10, bg='blue')
lblWelcome = Label(welcFrame, text="Welcome to the Caesar Cipher program", bg='blue', fg='white') 

# Encrypt / Decrypt user choices
cryptFrame = LabelFrame(root, padx=10, pady=10, bg='pink')
lblCryptMsg = Label(cryptFrame, text="STEP 1 - Press a button to Encrypt or Decrypt a message", padx=5, pady=5)
btnCrypt1 = Radiobutton(cryptFrame, text="Encrypt", variable=crypt, value="Crypt1", command=clickCrypt)
btnCrypt2 = Radiobutton(cryptFrame, text="Decrypt", variable=crypt, value="Crypt2", command=clickCrypt) 


# Alphabet choices
alphaFrame = LabelFrame(root, padx=10, pady=10, bg='green')
lblAlphaChoice = Label(alphaFrame, text=" STEP 2 - Now choose your encryption algo")
btnAlpha1 = Radiobutton(alphaFrame, text="Alphabet 1", variable=algo, value="Alpha1", command=clickAlpha) 
btnAlpha2 = Radiobutton(alphaFrame, text="Alphabet 2", variable=algo, value="Alpha2",command=clickAlpha) 
btnAlpha3 = Radiobutton(alphaFrame, text="Alphabet 3", variable=algo, value="Alpha3",command=clickAlpha) 

# Caesar shift slider
caesarFrame = LabelFrame(root, padx=10, pady=10, bg='red')
lblCaesar = Label(caesarFrame, text=" STEP 3 - Now set your Caesar Shift")
sldrCaesar = Scale(caesarFrame, from_=0, to=80, variable=cesar, orient=HORIZONTAL, command=moveCaesar)

# Input message box with a heading instructing user to paste or type message
lblMsgIn = Label(root, text="STEP 4 - Type or paste your message here then press the GO! button below.")
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
welcFrame.grid(row=0, columnspan=3, sticky=W+E)
lblWelcome.grid(row=0, column=0, columnspan=3)

# ROW 1 & 2 - Encrypt Decrypt button and message placement
cryptFrame.grid(row=1, columnspan=3, sticky=W+E)
lblCryptMsg.grid(row=1, column=0, columnspan=3, sticky=W)
btnCrypt1.grid(row= 2, column=0)
btnCrypt2.grid(row= 2, column=1)

# ROW 3 & 4 - Choose Alphabet button and message placement
alphaFrame.grid(row=3, columnspan=3, sticky=W+E)
lblAlphaChoice.grid(row=3, column=0, columnspan=3, sticky=W)
btnAlpha1.grid(row=4, column=0)
btnAlpha2.grid(row=4, column=1)
btnAlpha3.grid(row=4, column=2)

# Caesar
caesarFrame.grid(row=5, columnspan=3, sticky=W+E)
lblCaesar.grid(row=5, column=0, columnspan=3, sticky=W)
sldrCaesar.grid(row=6, column=0, columnspan=3, sticky=W+E)

# ROW 5 & 6 - User's Message input heading and area
lblMsgIn.grid(row=7, column=0, columnspan=3)
msgInput.grid(row=8, column=0, columnspan=3, sticky=W+E)

# ROW 7 - Go button placement
btnGo.grid(row= 9, column=1)

# ROW 8 & 9 - User's Message input heading and area

msgOutput.grid(row=10, column=0, columnspan=3, sticky=W+E)

# ROW 10 - Clear Messages & Copy to clipboard, Exit program button placement
btnClear.grid(row=11, column=0)
btnCopy.grid(row=11, column=1)
btnExit.grid(row=11, column=2)

# tkinter mainloop
root.mainloop()
