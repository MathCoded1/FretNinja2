from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from Fret import Fret as Fret


class Neck:
    def __init__(self, instrument, info):
        self.instrument = instrument
        self.instrument_info = info

    def callback_back(self, instance, screen, structure):
        screen.remove_widget(structure)
        # self.instrument_info = InstrumentInfo()
        self.instrument_info.setup_info_w_screen(screen)

    def build_neck(self, screen):
        structure = BoxLayout(orientation='vertical')
        neck_screen = screen
        st = self.instrument.number_of_strings
        frets = self.instrument.number_of_frets
        neck = Grid(st + 4, frets + 3)
        menu = AnchorLayout()
        menu.size_hint = (1, .17)
        back_button = Button(text='back')
        back_button.bind(on_press=lambda instance: self.callback_back(instance, screen, structure))
        menu.add_widget(back_button)
        structure.add_widget(menu)

        for j in range(frets + 3):
            neck.add_widget(Widget())
        strings = self.instrument.tuning
        notes = []
        # Create Frets dynamically named String'number'Fret'number
        for i in range(st):
            for j in range(frets + 1):
                notes.append(type("String" + str(6 - i) + "Fret" + str(j), (Fret,), {})())
        # Assign notes and add to neck
        neck.add_widget(Label(text='#'))
        for k in range(frets + 1):
            neck.add_widget(Label(text=str(k)))
        neck.add_widget(Widget())
        for note in notes:
            note.base_note = strings[note.string_number - 1]
            note.set_note()
            note.other_notes = notes
            if note.fret_number is 0:
                neck.add_widget(Label(text=str(note.string_number)))
            neck.add_widget(note)
            if note.fret_number is frets:
                neck.add_widget(Widget())
        # Add Lables for frets
        neck.add_widget(Label(text='#'))
        for j in range(frets + 1):
            neck.add_widget(Label(text=str(j)))
        structure.add_widget(neck)
        neck_screen.add_widget(structure)
        return neck_screen


class Grid(GridLayout):
    def __init__(self, rows, columns, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = columns

        dic = {0: 1, 1: .2, 2: .1}
        self.cols_minimum = dic
