"""
Given a string, are all characters unique?
should give a True or False return

Uses python built in structures
"""

def unique(s):
    s = s.replace(' ', '')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

print(unique('i am rejw'))