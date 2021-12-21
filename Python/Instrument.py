import NoteHelper as NH


class Instrument:
    type = 'GUITAR'
    numberOfStrings = 0
    numberOfFrets = 0
    tuningStyle = ''
    rootNote = ''
    tuning = []

    def calculate(self):
        for i in range(self.numberOfStrings):
            self.tuning.append('')
        self.tuning[0] = self.rootNote
        if self.tuningStyle is 'STANDARD':
            self.tuning[1] = NH.findNote(self.tuning[0], 5)
            self.tuning[2] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[1]), 5))
            self.tuning[3] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[2]), 5))
            self.tuning[4] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[3]), 4))
            self.tuning[5] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[4]), 5))
        if self.tuningStyle is 'DROP':
            self.tuning[1] = NH.findNote(self.tuning[0], 7)
            self.tuning[2] = NH.findNote(str(self.tuning[1]), 5)
            self.tuning[3] = NH.findNote(self.tuning[2], 5)
            self.tuning[4] = NH.findNote(self.tuning[3], 4)
            self.tuning[5] = NH.findNote(self.tuning[4], 5)
        if self.tuningStyle is 'OPEN':
            self.tuning[1] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[0]), 7))
            self.tuning[2] = self.tuning[0]
            self.tuning[3] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[0]), 16))
            self.tuning[4] = NH.numberToNote(NH.add(NH.noteToNumber(self.tuning[3]), 3))
            self.tuning[5] = self.tuning[0]
        return None