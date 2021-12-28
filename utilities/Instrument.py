from utilities import NoteHelper


class Instrument:
    instrument_type = 'GUITAR'
    number_of_strings = 0
    number_of_frets = 0
    tuning_style = ''
    root_note = ''
    tuning = []

    def calculate(self):
        self.tuning =[]
        for i in range(self.number_of_strings):
            self.tuning.append('')
        self.tuning[0] = self.root_note
        if self.instrument_type is 'GUITAR':
            if self.tuning_style is 'STANDARD':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 5)
                self.tuning[2] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[1]), 5))
                self.tuning[3] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[2]), 5))
                self.tuning[4] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[3]), 4))
                self.tuning[5] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[4]), 5))

            if self.tuning_style is 'DROP':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 7)
                self.tuning[2] = NoteHelper.find_note(str(self.tuning[1]), 5)
                self.tuning[3] = NoteHelper.find_note(self.tuning[2], 5)
                self.tuning[4] = NoteHelper.find_note(self.tuning[3], 4)
                self.tuning[5] = NoteHelper.find_note(self.tuning[4], 5)
            if self.tuning_style is 'OPEN':
                self.tuning[1] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 7))
                self.tuning[2] = self.tuning[0]
                self.tuning[3] = NoteHelper.number_to_note(
                    NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 16))
                self.tuning[4] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[3]), 3))
                self.tuning[5] = self.tuning[0]
        elif self.instrument_type is 'BASS':
            if self.tuning_style is 'STANDARD':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 5)
                self.tuning[2] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[1]), 5))
                self.tuning[3] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[2]), 5))
            if self.tuning_style is 'DROP':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 7)
                self.tuning[2] = NoteHelper.find_note(str(self.tuning[1]), 5)
                self.tuning[3] = NoteHelper.find_note(self.tuning[2], 5)
            if self.tuning_style is 'OPEN':
                self.tuning[1] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 7))
                self.tuning[2] = self.tuning[0]
                self.tuning[3] = NoteHelper.number_to_note(
                    NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 16))
