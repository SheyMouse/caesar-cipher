#
#   CAESAR CIPHER - PART 1
#
#   Standard Caesar Cipher where the user adds a message and cipher key
#   The message is encoded according to the key in relation to the alphabet
#
#   There are some obvious issues with this cipher. What are they?
#
#

alphabet = 'abcdefghijklmnopqrstuvwxyz' # The alphabet which the cypher will use for encoding
newMessage = '' # Initialise the message variable

message = input('Please enter a messsage: ')
theKey = int(input('Please enter your key: '))

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + theKey)%26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is: ', newMessage)
