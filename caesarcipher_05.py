#
#   CAESAR CIPHER - PART 5
#   Encrypt and decrypt your message
#
#   In this Caesar Cipher we take the Part 4 cypher code and add the ability to
#   decrypt a message sent to you.
#   The user chooses to encrypt or decrypt a message. Then the app asks for the
#   message, key, and alphabet, and then performs the desired action.
#

alphabet01 = 'GjlZCMaQKU"/-Xf$£mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k@hnIuVWsp'
alphabet02 = 'hkS*F>ucL/l-)VPB£iRZUdICQ$z(@?=f<ta:m#Wvp;~n!Yg."^sxMHNKDwybjr_,O%oq+TJGXAEe&'
alphabet03 = '(OIce$TnM=JvF?j<&X+S>ih"EYdK£,lq!Z@~QmbyD-wUWNsrV^H:fB.aPpkL_otC/);RzAGxg%*#u'
newMessage = ''

print('Would you like to encode or decode a message?')
userChoice = int(input('Choose 1 to encode or 2 to decode: '))


##message = input('Please enter a messsage: ')
##theAlpha = int(input('Please choose alphabet 1, 2, or 3: '))
##theKey = int(input('Please enter your key: '))

if userChoice == 1:
    message = input('Please enter a messsage: ')
    theAlpha = int(input('Please choose alphabet 1, 2, or 3: '))
    theKey = int(input('Please enter your key: '))

    if theAlpha == 1:
        useAlpha = alphabet01
    elif theAlpha == 2:
        useAlpha = alphabet02
    else:
        useAlpha = alphabet03

    for character in message:
        if character in useAlpha:
            position = useAlpha.find(character)
            # NB: len(alphabet) handles a list of any length
            newPosition = (position + theKey)%len(useAlpha) 
            newCharacter = useAlpha[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character

    print('Your new message is: ', newMessage)
else:
    message = input('Please enter a messsage: ')
    theAlpha = int(input('Please choose alphabet 1, 2, or 3: '))
    theKey = int(input('Please enter your key: '))

    if theAlpha == 1:
        useAlpha = alphabet01
    elif theAlpha == 2:
        useAlpha = alphabet02
    else:
        useAlpha = alphabet03

    for character in message:
        if character in useAlpha:
            position = useAlpha.find(character)
            # NB: len(alphabet) handles a list of any length
            newPosition = (position - theKey)%len(useAlpha) 
            newCharacter = useAlpha[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character

    print('Your new message is: ', newMessage)
