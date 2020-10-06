import translator
import time

def pause(units):
    time.sleep(unit * units)

unit = 1

dit = 1
dah = 3
sep_ditdah = 1
sep_letter = 3
sep_word = 7

def create_morse(string):
    string = translator.encode(string.upper())
    print(string)
    for character in string:
        if character == '':
            pause(sep_word - (sep_ditdah + sep_letter))
        else:
            for char in character:
                yield 'on'
                if char == '-':
                    pause(dah)
                else:
                    pause(dit)
                yield 'off'
                pause(sep_ditdah)
            pause(sep_letter - sep_ditdah)
