from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from utilities.Fret import Fret as Fret


class Neck:
    def __init__(self, instrument, info):
        self.instrument = instrument
        self.instrument_info = info

    def callback_back(self, instance, screen, structure):
        screen.remove_widget(structure)
        if self.instrument.tuning_style is not 'CUSTOM':
            self.instrument_info.root_note_select(screen)

    def build_neck(self, screen):
        structure = BoxLayout(orientation='vertical')
        neck_screen = screen
        st = self.instrument.number_of_strings
        fret_number = self.instrument.number_of_frets
        neck = BoxLayout()

        menu = AnchorLayout()
        menu.size_hint = (1, .17)
        back_button = Button(text='back')
        back_button.bind(on_press=lambda instance: self.callback_back(instance, screen, structure))
        menu.add_widget(back_button)
        structure.add_widget(menu)
        strings = self.instrument.tuning
        notes = []
        # Create Frets dynamically named String'number'Fret'number

        for i in range(fret_number + 1):
            for j in range(st):
                notes.append(type("String" + str(6-j) + "Fret" + str(i), (Fret,), {})())
        fretboard = BoxLayout()
        for note in notes:
            note.base_note = strings[note.string_number - 1]
            note.set_note()
            note.other_notes = notes
        frets = []
        fret_wires = []
        for f in range(fret_number+1):
            frets.append(BoxLayout(orientation='vertical'))
            fretboard.add_widget(frets[f])
            fret_wires.append(Button(text=str(f)+"\n\n\n\n\n\n\n\n\n\n\n\n"+str(f)))
            fretboard.add_widget(fret_wires[f])
        for note in notes:
            frets[note.fret_number].add_widget(note)
        neck.add_widget(fretboard)
        structure.add_widget(neck)
        details = Label()
        structure.add_widget(details)
        details.text = 'your '+str(self.instrument.instrument_type).lower()+" is in "+\
                       str(self.instrument.tuning_style).lower()+" "+str(self.instrument.root_note)
        neck_screen.add_widget(structure)
        return neck_screen


class Grid(GridLayout):
    def __init__(self, rows, columns, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = columns

        dic = {0: 1, 1: .2, 2: .1}
        self.cols_minimum = dic
