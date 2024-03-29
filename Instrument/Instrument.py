from Instrument import NoteHelper

class Instrument:
    instrument_type = 'GUITAR'
    number_of_strings = 0
    number_of_frets = 0
    tuning_style = ''
    root_note = ''
    tuning = []
    root_note_actual = None

    def noteChanger(self, a, b):
        pass

    def calculate(self):
        self.notes = [[''] * (self.number_of_frets+1)]*self.number_of_strings
        self.tuning = []
        for i in range(self.number_of_strings):
            self.tuning.append('')
        self.tuning[0] = self.root_note
        if self.instrument_type == 'GUITAR':

            if self.tuning_style == 'STANDARD':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 5)
                self.tuning[2] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[1]), 5))
                self.tuning[3] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[2]), 5))
                self.tuning[4] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[3]), 4))
                self.tuning[5] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[4]), 5))

            if self.tuning_style == 'DROP':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 7)
                self.tuning[2] = NoteHelper.find_note(str(self.tuning[1]), 5)
                self.tuning[3] = NoteHelper.find_note(self.tuning[2], 5)
                self.tuning[4] = NoteHelper.find_note(self.tuning[3], 4)
                self.tuning[5] = NoteHelper.find_note(self.tuning[4], 5)
            if self.tuning_style == 'OPEN':
                self.tuning[1] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 7))
                self.tuning[2] = self.tuning[0]
                self.tuning[3] = NoteHelper.number_to_note(
                    NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 16))
                self.tuning[4] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[3]), 3))
                self.tuning[5] = self.tuning[0]
        elif self.instrument_type == 'BASS':
            if self.tuning_style == 'STANDARD':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 5)
                self.tuning[2] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[1]), 5))
                self.tuning[3] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[2]), 5))
            if self.tuning_style == 'DROP':
                self.tuning[1] = NoteHelper.find_note(self.tuning[0], 7)
                self.tuning[2] = NoteHelper.find_note(str(self.tuning[1]), 5)
                self.tuning[3] = NoteHelper.find_note(self.tuning[2], 5)
            if self.tuning_style == 'OPEN':
                self.tuning[1] = NoteHelper.number_to_note(NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 7))
                self.tuning[2] = self.tuning[0]
                self.tuning[3] = NoteHelper.number_to_note(
                    NoteHelper.add(NoteHelper.note_to_number(self.tuning[0]), 16))
        self.calculate_frequency()

    def calculate_frequency(self):
        pass
