#
#   CAESAR CIPHER - PART 4
#   Making the cipher even more complex and harder to reverse engineer
#
#   In this Caesar Cipher we use multiple scrambled alphabets. The user chooses
#   an alphabet, then types the message, and finally picks the key.
#   Adding extra complexity makes it even more difficult to reverse your
#   message, but could be easily found out if both the key and the alphabet
#   number are known.
#    The single apostrophe is handled using the escape character \. So is
#   the backslash. This needs to manually be entered after the alphabets 
#   scrambled. 
#   
#   CHALLENGES - 
#   1. What if the user doesn't choose 1-3
#   2. What if the user doesn't choose a numeric key
#   3. What if the user wanted to decode a message from a friend?

alphabet01 = 'GjlZCMaQKU"/-Xf$£\\mrw:>H(%Fo&tD<!gJLzbiSxBcT,dqPYy=*OA~_?^.)E;evN+R#k\'@hnIuVWsp'
alphabet02 = 'hkS*F>ucL/l-)VPB£iR\\ZUdI\'CQ$z(@?=f<ta:m#Wvp;~n!Yg."^sxMHNKDwybjr_,O%oq+TJGXAEe&'
alphabet03 = '(OIce$TnM=JvF?j<&X+S>i\\h"EY\'dK£,lq!Z@~QmbyD-wUWNsrV^H:fB.aPpkL_otC/);RzAGxg%*#u'
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
        newMessage += character # line to handle a character which isn't in the alphabet variable

print('Your new message is: ', newMessage)


