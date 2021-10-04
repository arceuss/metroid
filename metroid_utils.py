import sys
import time
import ascii_magic

def pick(options):
    type("\nSelect an option.\n",80)
    for idx, element in enumerate(options):
        ("{}) {}".format(idx+1,element),160)
    i = input()
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        pass
    return None

def render(imagepath,color):
    if not color:
        color = ascii_magic.Modes.ASCII
    else:
        color = ascii_magic.Modes.TERMINAL
    ascii_magic.to_terminal(ascii_magic.from_image_file(
        imagepath,
        columns = 100,
        mode = color
    ))

def type(text,speed):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5*10.0/speed)