def note_to_number(note):
    changer = {
        'G ': 1,
        'G#': 2,
        'A ': 3,
        'A#': 4,
        'B ': 5,
        'C ': 6,
        'C#': 7,
        'D ': 8,
        'D#': 9,
        'E ': 10,
        'F ': 11,
        'F#': 12}
    return changer.get(note)


def number_to_note(position):
    changer = {
        1: "G ",
        2: "G#",
        3: 'A ',
        4: 'A#',
        5: 'B ',
        6: 'C ',
        7: 'C#',
        8: 'D ',
        9: 'D#',
        10: 'E ',
        11: 'F ',
        12: 'F#'}
    return changer.get(position)


def add(note1, fret):
    if note1 + fret is 36:
        return note1
    if fret == 0:
        return note1
    if note1 + fret <= 12:
        return note1 + fret
    elif (note1 + fret) % 12 is not 0:
        return (note1 + fret) % 12
    elif note1 + fret is 24:
        return fret-12+note1


def find_note(open_fret, fret):
    a = number_to_note(add(int(note_to_number(open_fret)), fret))
    return a


def color_note(note, opacity):
    colors = {
        "A ": (.25, .75, .75, opacity),
        "A#": (.64901, 1, .92157, opacity),
        "B ": (.39608, .12157, 1, opacity),
        "C ": (.75, 0, .341176, opacity),
        "C#": (.75, .25, .75, opacity),
        "D ": (1, .75, .25, opacity),
        "D#": (.7765, 1, 0, opacity),
        "E ": (.95686, .262745, .211764, opacity),
        "F ": (1, 0, 1, opacity),
        'F#': (1, 0, .75, opacity),
        "G ": (0, 1, 0, opacity),
        "G#": (0, .75, 0, opacity),
    }
    return colors.get(note)


def get_frequency(note, number):
    base = {'C ': 16.35,
            'C#': 17.32,
            'D ': 18.35,
            'D#': 19.45,
            'E ': 20.60,
            'F ': 21.83,
            'F#': 23.12,
            'G ': 24.50,
            'G#': 25.96,
            'A ': 27.50,
            'A#': 29.14,
            'B ': 30.87
            }
    return base.get(note)*(int(number)**2)


def get_frequency_from_distance(starting_note, distance):
    return starting_note*(2**(distance/12))
