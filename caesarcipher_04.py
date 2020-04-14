#
#   CAESAR CIPHER - PART 4
#   Making the cipher even more complex and harder to reverse engineer
#
#   In this Caesar Cipher we use multiple scrambled alphabets. The user choses
#   an alphabet, then types the message, and picks the key.
#   Adding extra complexity makes it even more difficult to reverse your
#   message, but could be easily found out if both the key and the alphabet
#   number are known.
#
#   Known issues:
#   - Won't encode the single apostrophe, ', as that is what is being used
#   to define the aplphabet
#   - Also, the 'alphabet' is a limiting factor as only characters which are in
#   there will be encoded. EG. there aren't curly brackets {} so they won't get
#   get encoded
#

alphabet01 = 'GjlZCMaQKU"/-Xf$£mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k@hnIuVWsp'
alphabet02 = 'hkS*F>ucL/l-)VPB£iRZUdICQ$z(@?=f<ta:m#Wvp;~n!Yg."^sxMHNKDwybjr_,O%oq+TJGXAEe&'
alphabet03 = '(OIce$TnM=JvF?j<&X+S>ih"EYdK£,lq!Z@~QmbyD-wUWNsrV^H:fB.aPpkL_otC/);RzAGxg%*#u'
newMessage = ''

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


