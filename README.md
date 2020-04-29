# Caesar Cipher
 Variations on a simple Caesar Cipher from St. Neots CoderDojo

At the CoderDojo the pythonista ninjas went through an exercise where they built a programme
to encrypt a message using a [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).
Link to the exercise [here](https://projects.raspberrypi.org/en/projects/secret-messages).

Some of the stretch goals set for the ninjas was to write a decryption script, handle captials
and non-alphanumeric characters. One of the attendees wanted to 

Based on interactions with a couple of attendees my mind got working about how to go even
further with the cipher programme and learn some Python at the same time!

I've tried to split all the files up to show progression of the application as it gets more
complex.

## caesarcipher_01.py

This is the basic programme. It takes the user's input, runs through the alphabet, and outputs
an encrypted message.
Some of the obvious issues with this programme are:
* Won't encrypt anything thats outside of the alphabet such as capitals and non-alpha characters
* The length of the string used to calculate when to wrap round to character 0 is hard coded to 26.
    * See line 24 "newPosition = (position + theKey)%26"

## caesarcipher_02.py

This version is very similar to the last iteration. We now have a larger alphabet for the programme
to parse and apply the Caesar shift to. "%26" from version 01 will now automatically adjust for any
length of alphabet. This is set by "%len(alphabet)" on line 26.
There are still some issues here:
* The single apostrophe " ' " isn't included in the alphabet
* The alphabet is sequential and so would be fairly easy for someone to reverse engineer your message
with a script [Maybe this should be a ToDo]

## caesarcipher_03.py

TBD

## caesarcipher_04.py

TBD

## caesarcipher_05.py

TBD

## caesarcipher_06.py

TBD

## Further learnings

TBD

## Resources

TBD

