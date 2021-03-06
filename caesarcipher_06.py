#
#   CAESAR CIPHER - PART 6 
#   Add a GUI
#   - by JeffGames
#   
#
#
# ToDo: 
# 1. Add JeffGames icon
# 2. Handle spaces in the string


# Import tkinter, our GUI framework
from tkinter import * # Import tkinter, our GUI framework

root = Tk()

# Variables used by the main program.
alphabet01 = 'GjlZCMaQKU"/-Xf$£\\mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k\'@hnIuVWsp'
alphabet02 = 'hkS*F>ucL/l-)VPB£iR\\ZUdI\'CQ$z(@?=f<ta:m#Wvp;~n!Yg."^sxMHNKDwybjr_,O%oq+TJGXAEe&'
alphabet03 = '(OIce$TnM=JvF?j<&X+S>i\\h"EY\'dK£,lq!Z@~QmbyD-wUWNsrV^H:fB.aPpkL_otC/);RzAGxg%*#u'

# Define what happens when the go button is clicked
fooAlpha = alphabet01
def clickAlpha():
    global fooAlpha
    print("Alphabet from clickAlpha = ", algo.get()) # Calls algo and prints its value
    myAlpha = algo.get()
    print("myAlpha = ", myAlpha) # debug printing
    if myAlpha == "Alpha1":
        print(alphabet01) # debug printing
        fooAlpha = alphabet01
    elif myAlpha == "Alpha2":
        print(alphabet02) # debug printing
        fooAlpha = alphabet02
    else:
        print(alphabet03) # debug printing
        fooAlpha = alphabet03


def clickEncrypt():
    msgEncrypt = msgInput.get()
    msgEncrypt = str(msgEncrypt)
    #print(msgEncrypt) # Used for debugging
    caesarShift = cesar.get()
    caesarShift = int(caesarShift)
    useAlpha = fooAlpha
    useAlpha = str(useAlpha)
    print(useAlpha) # Used for debugging
    newMessage = ""

    for character in msgEncrypt:
        if character in useAlpha:
            position = useAlpha.find(character) 
            # NB: len(alphabet) handles a list of any length
            newPosition = (position + caesarShift)%len(useAlpha) 
            newCharacter = useAlpha[newPosition]
            newMessage += newCharacter
            #Put the new message into the message output field        

        else:
            newMessage += character # line to handle a character which isn't in the alphabet variable
        msgOutput.delete(0, END) # Clear the output field after GO is clicked
        # Ans = str(newMessage) # Read message for putting into the output field
        msgOutput.insert(0, newMessage) #(0, Ans) # Put the message from input field into

def clickDecrypt():
    print("Decrypt pressed")
    msgEncrypt = msgInput.get()
    msgEncrypt = str(msgEncrypt)
    #print(msgEncrypt) # Used for debugging
    caesarShift = cesar.get()
    caesarShift = int(caesarShift)
    useAlpha = fooAlpha # Hard coding the algo
    useAlpha = str(useAlpha)
    print(useAlpha) # Used for debugging
    newMessage = ""

    for character in msgEncrypt:
        if character in useAlpha:
            position = useAlpha.find(character) 
            # NB: len(alphabet) handles a list of any length
            newPosition = (position - caesarShift)%len(useAlpha) 
            newCharacter = useAlpha[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character # line to handle a character which isn't in the alphabet variable
        msgOutput.delete(0, END) # Clear the output field after GO is clicked
        # Ans = str(newMessage) # Read message for putting into the output field
        msgOutput.insert(0, newMessage) #(0, Ans) # Put the message from input field into

def moveCaesar(sld): # A variable must be in here for the function to work
    print("Shift = ", cesar.get()) # Calls cesar variable and prints its value

def clickClear():
    msgInput.delete(0, END)
    msgOutput.delete(0, END)
    print("Cleared all messages")

def clickCopy():
    # return # Will eventually copy the decrypted or encrypted text to clipboard
    root.clipboard_clear() #clear the computer's clopboard
    # root.clipboard_append(msgOutput) #populate the clipboard
    print('clipboard module accessed')
    
    
def clickQuit(): # Created to have a pop-up to confirm quit.
    btnExit(command=root.quit)

# Set up for the Alphabet being used. Alphabet 1 is default
algo = StringVar()
algo.set("Alpha1") # Sets Alphabet 1 as default
print("Initial alphabet: ", algo.get()) # Calls algo.set and prints its value

# Set up for the Casar shift. 0 is the default
cesar = IntVar()
cesar.set(1)
print("Initial shift: ", cesar.get()) # Calls cesar variable and prints its value



# SET UP THE CANVAS
root.title("Caesar Cipher by JeffGames")


#   ---------------------------------------------------
#   SET UP THE BUTTONS, Message boxes, and input areas
#   ---------------------------------------------------

# Welcome message
welcFrame = LabelFrame(root, padx=10, pady=10, bg='blue')
lblWelcome = Label(welcFrame, text="Welcome to the Caesar Cipher program", bg='blue', fg='white') 

# Input message box with a heading instructing user to paste or type message
lblMsgIn = Label(root, text="Type or paste your message in the box below.")
msgInput = Entry(root)

# Parent frame for Alphabet and Caesar shift
choicesFrame = LabelFrame(root, padx= 5, pady=5)

# Alphabet choices
alphaFrame = LabelFrame(choicesFrame, padx=2, pady=2)
lblAlphaChoice = Label(alphaFrame, text="Choose your encryption algo")
btnAlpha1 = Radiobutton(alphaFrame, text="Alphabet 1", variable=algo, value="Alpha1", command=clickAlpha) 
btnAlpha2 = Radiobutton(alphaFrame, text="Alphabet 2", variable=algo, value="Alpha2",command=clickAlpha) 
btnAlpha3 = Radiobutton(alphaFrame, text="Alphabet 3", variable=algo, value="Alpha3",command=clickAlpha) 

# Caesar shift slider
caesarFrame = LabelFrame(choicesFrame, padx=2, pady=2)
lblCaesar = Label(caesarFrame, text="Set your Caesar Shift")
sldrCaesar = Scale(caesarFrame, from_=0, to=80, variable=cesar, orient=VERTICAL, command=moveCaesar)

# Encrypt / Decrypt user choices
cryptFrame = LabelFrame(root, padx=10, pady=10)
lblCryptMsg = Label(cryptFrame, text="Press a button to Encrypt or Decrypt a message", padx=5, pady=5)
btnCrypt1 = Button(cryptFrame, text="Encrypt", command=clickEncrypt)
btnCrypt2 = Button(cryptFrame, text="Decrypt", command=clickDecrypt) 

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

# ROW 1 & 2 - User's Message input heading and area
lblMsgIn.grid(row=1, column=0, columnspan=3)
msgInput.grid(row=2, column=0, columnspan=3, sticky=W+E)

choicesFrame.grid(row=3, columnspan=3, sticky=W+E)
# ROW 3 & 4 - Choose Alphabet button and message placement
alphaFrame.grid(row=0, column=0, sticky=W+E) #span=3
lblAlphaChoice.grid(row=0, column=0, columnspan=3, sticky=W)
btnAlpha1.grid(row=1, column=0)
btnAlpha2.grid(row=2, column=0)
btnAlpha3.grid(row=3, column=0)

# ROW 5 & 6 Caesar shift slider
#caesarFrame.grid(row=5, columnspan=3, sticky=W+E)
caesarFrame.grid(row=0, column=1, sticky=W+E)
lblCaesar.grid(row=5, column=0, columnspan=3, sticky=W)
sldrCaesar.grid(row=6, column=0, columnspan=3, sticky=W+E)

# ROW 7 & 8 - Encrypt Decrypt button and message placement
cryptFrame.grid(row=7, columnspan=3, sticky=W+E)
lblCryptMsg.grid(row=7, column=0, columnspan=3, sticky=W)
btnCrypt1.grid(row= 8, column=0)
btnCrypt2.grid(row= 8, column=1)

# ROW 0 - User's Message ouput heading and area
msgOutput.grid(row=9, column=0, columnspan=3, sticky=W+E)

# ROW 10 - Clear Messages & Copy to clipboard, Exit program button placement
btnClear.grid(row=10, column=0)
btnCopy.grid(row=10, column=1)
btnExit.grid(row=10, column=2)

# tkinter mainloop
root.mainloop()
