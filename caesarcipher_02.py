#
#   CAESAR CIPHER - PART 2
#   Handling capitals and non-alphanumeric
#
#   Standard Caesar Cipher where the user adds a message and cipher key
#   The message is encoded according to the key in relation to the alphabet
#   Part 2 gets round the capitalised and non-alphanumeric characters
#
#   Known issues:
#   - Won't encode the single apostrophe, ', as that is what is being used
#   to define the aplphabet
#   - Also, the 'alphabet' is a limiting factor as only characters which are in
#   there will be encoded. EG. there aren't curly brackets {} so they won't get
#   get encoded
#

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"£$%^&*();:@#~?/>.<,-_=+'
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


