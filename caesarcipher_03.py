#
#   CAESAR CIPHER - PART 3
#   Making the cipher more complex and harder to reverse engineer
#
#   In this Caesar Cipher the alphabet was scrambled using a small Python app
#   This will guard against someone trying to reverse engineer your message by
#   assuming you made the alphabet by using lower case a-z then upper case A-Z
#   followed by non-alphanumeric characters.
#   The message is encoded according to the key in relation to the alphabet
#   
#    CHALLENGES - 
#       1. How would you handle characters which are missing such as ' and \
#       2. Is there a way to handle spaces between words
#

alphabet = 'GjlZCMaQKU"/-Xf$£mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k@hnIuVWsp'
newMessage = ''

message = input('Please enter a messsage: ')
# The key is the number of steps along the alphabet the program will step 
# when encrypting the message. A key of 3 for example would turn the letter
# 'c' into 'f'
theKey = int(input('Please enter your key: '))

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        # len(alphabet) handles a list of any length
        newPosition = (position + theKey)%len(alphabet) 
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character # line to handle a character which isn't in the alphabet variable

print('Your new message is: ', newMessage)


