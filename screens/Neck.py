from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from utilities.Fret import Fret as Fret


class Neck:
    first_fret_number = None
    second_fret_number = None

    def __init__(self, instrument, info):
        self.fretboard = BoxLayout()
        self.instrument = instrument
        self.instrument_info = info
        self.fret_selected = False
        self.frets = []
        self.notes = []
        self.built = False

    def callback_back(self, instance, screen, structure):
        screen.remove_widget(structure)
        if self.instrument.tuning_style is not 'CUSTOM':
            self.instrument_info.root_note_select(screen)

    def callback_fret_wire(self, instance, fret_number, tuning_screen, structure):
        if self.fret_selected is True:
            self.second_fret_number = fret_number
            self.fret_selected = False
            self.zoom_neck(tuning_screen, structure)
        elif self.fret_selected is False:
            self.first_fret_number = fret_number
            self.fret_selected = True

    def zoom_neck(self, tuning_screen, structure):
        if self.first_fret_number > self.second_fret_number:
            self.first_fret_number, self.second_fret_number = self.second_fret_number, self.first_fret_number
        tuning_screen.remove_widget(structure)
        for f in range(self.instrument.number_of_frets+1):
            self.frets[f].clear_widgets()
        self.build_zoomed_neck(tuning_screen, self.first_fret_number, self.second_fret_number)

    def callback_back_from_zoomed(self, instance, screen, structure):
        self.first_fret_number = self.second_fret_number = None
        screen.remove_widget(structure)
        self.fretboard.clear_widgets()
        for f in self.frets:
            f.clear_widgets()
        self.build_neck(screen)

    def build_zoomed_neck(self, screen, fret_1,fret_2):
        structure = BoxLayout(orientation='vertical')

        menu = AnchorLayout()
        menu.size_hint = (1, .17)
        back_button = Button(text='back')
        back_button.bind(on_press=lambda instance: self.callback_back_from_zoomed(instance, screen, structure))
        menu.add_widget(back_button)
        structure.add_widget(menu)
        self.frets = []
        fret_wires = []
        self.fretboard = BoxLayout()

        self.frets.append(BoxLayout(orientation='vertical'))
        self.fretboard.add_widget(self.frets[0])
        fret_wires.append(Label(text='0' + "\n\n\n\n\n\n\n\n\n\n\n\n" + '0'))
        self.fretboard.add_widget(fret_wires[0])
        self.fretboard.add_widget(Widget())
        for f in range(1, fret_2-fret_1+2):
            self.frets.append(BoxLayout(orientation='vertical'))
            self.fretboard.add_widget(self.frets[f])
            fret_wires.append(Button(text=str(fret_1+f-1)+"\n\n\n\n\n\n\n\n\n\n\n\n"+str(fret_1+f-1)))
            self.fretboard.add_widget(fret_wires[f])
        for s in range(self.instrument.number_of_strings):
            self.frets[0].add_widget(self.notes[s])
        number = (fret_2+1) * self.instrument.number_of_strings
        start = fret_1*self.instrument.number_of_strings
        count = 0
        counter = 1
        for i in range(start, number-1):
            if count is 5:
                self.frets[counter+1].add_widget(self.notes[i])
                count = 0
                counter += 1
            else:
                self.frets[counter].add_widget(self.notes[i])
                count += 1
        structure.add_widget(self.fretboard)
        screen.add_widget(structure)

    def build_frets(self, fret_number, st):
        for i in range(fret_number + 1):
            for j in range(st):
                self.notes.append(type("String" + str(6-j) + "Fret" + str(i), (Fret,), {})())

    def build_neck(self, screen):
        structure = BoxLayout(orientation='vertical')
        neck = BoxLayout()
        self.fretboard = BoxLayout()
        menu = AnchorLayout()
        menu.size_hint = (1, .17)
        back_button = Button(text='back')
        back_button.bind(on_press=lambda instance: self.callback_back(instance, screen, structure))
        menu.add_widget(back_button)
        structure.add_widget(menu)
        strings = self.instrument.tuning
        # Create Frets dynamically named String'number'Fret'number
        if self.built is False:
            self.build_frets(self.instrument.number_of_frets, self.instrument.number_of_strings)
            self.built = True
        for note in self.notes:
            note.base_note = strings[note.string_number - 1]
            note.set_note()
            note.other_notes = self.notes
        self.frets = []
        fret_wires = []
        for f in range(self.instrument.number_of_frets+1):
            self.frets.append(BoxLayout(orientation='vertical'))
            self.fretboard.add_widget(self.frets[f])
            fret_wires.append(Button(text=str(f)+"\n\n\n\n\n\n\n\n\n\n\n\n"+str(f)))
            self.fretboard.add_widget(fret_wires[f])
        for i in range(len(fret_wires)):
            fret_wires[i].bind(on_press=lambda instance, bound_i=i: self.callback_fret_wire( instance, bound_i,screen, structure))
        for note in self.notes:
            self.frets[note.fret_number].add_widget(note)
        neck.add_widget(self.fretboard)
        structure.add_widget(neck)
        details = Label()
        structure.add_widget(details)
        details.text = 'your '+str(self.instrument.instrument_type).lower()+" is in "+\
                       str(self.instrument.tuning_style).lower()+" "+str(self.instrument.root_note)
        screen.add_widget(structure)
        return screen
