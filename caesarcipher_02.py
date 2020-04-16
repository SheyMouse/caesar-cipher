#
#    CAESAR CIPHER - PART 2
#    Handling capitals and non-alphanumeric
#
#    This cipher varies from Part I in the alphabet variable now contains
#    capital letters and non-alphanumeric characters
#
#    There are still two major issues with this version of the cipher, can
#    you think what they are? 
#
#

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"£$%^&*();:@#~?/>.<,-_=+'
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


