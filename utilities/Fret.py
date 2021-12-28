from kivy.uix.button import Button

from utilities import NoteHelper


class Fret(Button):
    base_note = "G"
    other_notes = []
    highlighted = False
    unhighlighted = .13
    note = ''

    def set_note(self):
        self.note = str(NoteHelper.find_note(self.base_note, self.fret_number))
        self.text = self.note
        self.background_color = (0, 0, 0, self.unhighlighted)

    def set_color(self, opacity):
        return NoteHelper.color_note(self.note, opacity)

    def callback(self, instance):
        if self.highlighted is False:
            self.background_color = self.set_color(1)
            self.color = (0, 0, 0, 1)
            self.highlighted = True
            for fret in self.other_notes:
                if fret.note is self.note:
                    fret.background_color = self.set_color(1)
                    fret.color = (0, 0, 0, 1)
                    fret.highlighted = True
        else:
            self.background_color = self.set_color(self.unhighlighted)
            self.color = (1, 1, 1, 1)
            self.highlighted = False
            for fret in self.other_notes:
                if fret.note is self.note:
                    fret.background_color = (0,0,0,self.unhighlighted)
                    fret.color = (1, 1, 1, 1)
                    fret.highlighted = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        name_length = len(self.__class__.__name__)
        self.bind(on_press=self.callback)
        if self.__class__.__name__[name_length - 2].isdigit():
            self.fret_number = int(self.__class__.__name__[name_length - 2:name_length])
        else:
            self.fret_number = int(self.__class__.__name__[name_length - 1])
        self.string_number = int(self.__class__.__name__[6])
        self.background_normal = ''
