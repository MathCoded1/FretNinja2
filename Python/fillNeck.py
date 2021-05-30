
def change(self, note):
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





def changeBack(self, position):
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
    12: "F#",}
    return changer.get(position)


def fillarr(self, zeroth):
    a = []
    a[0] = changeBack(zeroth)
    a[1] = changeBack(add(zeroth,1))
    a[2] = changeBack(add(zeroth,2))
    a[3] = changeBack(add(zeroth,3))
    a[4] = changeBack(add(zeroth,4))
    a[5] = changeBack(add(zeroth,5))
    a[6] = changeBack(add(zeroth,6))
    a[7] = changeBack(add(zeroth,7))
    a[8] = changeBack(add(zeroth,8))
    a[9] = changeBack(add(zeroth,9))
    a[10] = changeBack(add(zeroth,10))
    a[11] = changeBack(add(zeroth,11))
    return a


def add(self, num1, num2):
    if num1 + num2 <=12:
        return num1 + num2
    else:
        return num1 + num2 - 11


