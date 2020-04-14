#
#   CAESAR CIPHER - PART 3
#   Making the cipher more complex and harder to reverse engineer
#
#   In this Caesar Cipher the alphabet was scrambled using a small Python app
#   This will guard against someone trying to reverse engineer your message by
#   assuming you made the alphabet by using lower case a-z then upper case A-z
#   followed by non-alphanumeric characters.
#   The message is encoded according to the key in relation to the alphabet
#   
#
#   Known issues:
#   - Won't encode the single apostrophe, ', as that is what is being used
#   to define the aplphabet
#   - Also, the 'alphabet' is a limiting factor as only characters which are in
#   there will be encoded. EG. there aren't curly brackets {} so they won't get
#   get encoded
#

alphabet = 'GjlZCMaQKU"/-Xf$£mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k@hnIuVWsp'
newMessage = ''

message = input('Please enter a messsage: ')
theKey = int(input('Please enter your key: '))

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        # len(alphabet) handles a list of any length
        newPosition = (position + theKey)%len(alphabet) 
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is: ', newMessage)


