def noteToNumber(note):
    changer ={
    "G": 1,
    "G#": 2,
    "A": 3,
    "A#": 4,
    "B": 5,
    "C": 6,
    "C#": 7,
    "D": 8,
    "D#": 9,
    "E": 10,
    "F": 11,
    "F#": 12}
    return changer.get(note)

def numberToNote(position):
    changer={
    1: "G ",
    2: "G#",
    3:"A ",
    4:"A#",
    5: "B ",
    6: "C ",
    7: "C#",
    8:"D ",
    9: "D#",
    10: "E ",
    11: "F ",
    12: "F#"}
    return changer.get(position)

def add(note1, fret):
        if note1+fret <=12:
            return note1 + fret
        elif (note1 + fret)%12 != 0:
            return (note1 + fret)%12
        elif note1 +fret == 24:
            return fret-12 + note1

def findNote(openFret, fret):
    a = numberToNote(add(int(noteToNumber(openFret)), fret))
    return a

