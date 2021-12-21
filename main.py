from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from Instrument import Instrument as Instrument
import NoteHelper


def create():
    info = InstrumentInfo()
    return info.setup_info()


class SetTuningScreen(Screen):

    def __init__(self, **kwargs):
        super(SetTuningScreen, self).__init__(**kwargs)
        self.name = 'infoScr'


class Fret(Button):
    base_note = "G"
    other_notes = []
    highlighted = False
    unhighlighted = .13
    note = ''

    def set_note(self):
        self.note = str(NoteHelper.find_note(self.baseNote, self.fret_number))
        self.text = self.note
        self.background_color = self.set_color(self.unhighlighted)

    def set_color(self, opacity):
        return NoteHelper.color_note(self.note, opacity)

    def callback(self, instance):
        if self.highlighted is False:
            self.background_color = self.set_color(1)
            self.highlighted = True
            for fret in self.otherNotes:
                if fret.note is self.note:
                    fret.background_color = self.set_color(1)
                    fret.highlighted = True
        else:
            self.background_color = self.set_color(self.unhighlighted)
            self.highlighted = False
            for fret in self.otherNotes:
                if fret.note is self.note:
                    fret.background_color = self.set_color(self.unhighlighted)
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


class InstrumentInfo:
    instrument = Instrument()

    def callback(self, instance, a, b):
        self.instrument.type = 'GUITAR'
        a.remove_widget(b)
        self.string_select(a)

    def callback2(self, instance, a, b):
        self.instrument.type = 'BASS'
        a.remove_widget(b)
        self.string_select(a)

    def setup_info(self):
        tuning_screen = SetTuningScreen()
        instrument_selector = BoxLayout(orientation='vertical')
        btn = Button(text='Guitar')
        btn2 = Button(text='Bass')
        btn.bind(on_press=lambda instance: self.callback(instance, tuning_screen, instrument_selector))
        btn2.bind(on_press=lambda instance: self.callback2(instance, tuning_screen, instrument_selector))
        instrument_selector.add_widget(btn)
        instrument_selector.add_widget(btn2)
        tuning_screen.add_widget(instrument_selector)
        return tuning_screen

    def callback3(self, instance, tuning_screen, string_selector):
        self.instrument.number_of_strings = 6
        tuning_screen.remove_widget(string_selector)
        self.fret_select(tuning_screen)

    def callback4(self, instance, tuning_screen, string_selector):
        self.instrument.number_of_strings = 7
        tuning_screen.remove_widget(string_selector)
        self.fret_select(tuning_screen)

    def callback5(self, instance, tuning_screen, string_selector):
        self.instrument.number_of_strings = 4
        tuning_screen.remove_widget(string_selector)
        self.fret_select(tuning_screen)

    def callback6(self, instance, tuning_screen, string_selector):
        self.instrument.number_of_strings = 5
        tuning_screen.remove_widget(string_selector)
        self.fret_select(tuning_screen)

    def string_select(self, tuning_screen):
        string_selector = BoxLayout(orientation='vertical')

        if Instrument.type is 'GUITAR':
            btn3 = Button(text='6')
            btn3.bind(on_press=lambda instance: self.callback3(instance, tuning_screen, string_selector))
            btn4 = Button(text='7')
            btn4.bind(on_press=lambda instance: self.callback4(instance, tuning_screen, string_selector))
            string_selector.add_widget(btn3)
            string_selector.add_widget(btn4)
        else:
            btn5 = Button(text='4')
            btn5.bind(on_press=lambda instance: self.callback5(instance, tuning_screen, string_selector))
            btn6 = Button(text='5')
            btn6.bind(on_press=lambda instance: self.callback6(instance, tuning_screen, string_selector))
            string_selector.add_widget(btn5)
            string_selector.add_widget(btn6)
        string_selector.text = 'how many strings is your ' + Instrument.type + '?'

        tuning_screen.add_widget(string_selector)

    def callback7(self, instance, tuning_screen, number_of_frets_selector):
        self.instrument.number_of_frets = 22
        tuning_screen.remove_widget(number_of_frets_selector)
        self.tuning_select(tuning_screen)

    def callback8(self, instance, tuning_screen, number_of_frets_selector):
        self.instrument.number_of_frets = 24
        tuning_screen.remove_widget(number_of_frets_selector)
        self.tuning_select(tuning_screen)

    def fret_select(self, tuning_screen):
        number_of_frets_selector = BoxLayout(orientation='vertical')
        btn5 = Button(text='22')
        btn5.bind(on_press=lambda instance: self.callback7(instance, tuning_screen, number_of_frets_selector))
        btn6 = Button(text='24')
        btn6.bind(on_press=lambda instance: self.callback8(instance, tuning_screen, number_of_frets_selector))
        number_of_frets_selector.add_widget(btn5)
        number_of_frets_selector.add_widget(btn6)
        tuning_screen.add_widget(number_of_frets_selector)

    def callback9(self, instance, tuning_screen, tuning_selector):
        self.instrument.tuning_style = 'STANDARD'
        tuning_screen.remove_widget(tuning_selector)
        self.root_note_select(tuning_screen)

    def callback10(self, instance, tuning_screen, tuning_selector):
        self.instrument.tuning_style = 'DROP'
        tuning_screen.remove_widget(tuning_selector)
        self.root_note_select(tuning_screen)

    def callback11(self, instance, tuning_screen, tuning_selector):
        self.instrument.tuning_style = 'OPEN'
        tuning_screen.remove_widget(tuning_selector)
        self.root_note_select(tuning_screen)

    def callback12(self, instance, tuning_screen, tuning_selector):
        self.instrument.tuning_style = 'CUSTOM'
        tuning_screen.remove_widget(tuning_selector)
        self.root_note_select(tuning_selector)

    def tuning_select(self, tuning_screen):
        tuning_selector = BoxLayout()

        tuning_selector.text = 'What tuning is your ' + str(
            self.instrument.number_of_strings) + ' ' + Instrument.type + ' in?'
        if self.instrument.type is 'GUITAR':
            btn7 = Button(text='Standard')
            btn8 = Button(text='Drop')
            btn9 = Button(text='Open')
            btn10 = Button(text='Custom')
            btn7.bind(on_press=lambda instance: self.callback9(instance, tuning_screen, tuning_selector))
            btn8.bind(on_press=lambda instance: self.callback10(instance, tuning_screen, tuning_selector))
            btn9.bind(on_press=lambda instance: self.callback11(instance, tuning_screen, tuning_selector))
            btn10.bind(on_press=lambda instance: self.callback12(instance, tuning_screen, tuning_selector))
            tuning_selector.add_widget(btn7)
            tuning_selector.add_widget(btn8)
            tuning_selector.add_widget(btn9)
            tuning_selector.add_widget(btn10)
        tuning_screen.add_widget(tuning_selector)

    def callback_root_note(self, note, tuning_screen, root_note_selector):
        self.instrument.root_note = note
        tuning_screen.remove_widget(root_note_selector)
        self.instrument.calculate()
        neck = Neck(self.instrument)
        neck.build_neck(tuning_screen)

    def callback13(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('E ', tuning_screen, root_note_selector)

    def callback14(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('D#', tuning_screen, root_note_selector)

    def callback15(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('D ', tuning_screen, root_note_selector)

    def callback16(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('C#', tuning_screen, root_note_selector)

    def callback17(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('C ', tuning_screen, root_note_selector)

    def callback18(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('B ', tuning_screen, root_note_selector)

    def callback19(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('A#', tuning_screen, root_note_selector)

    def callback20(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('A ', tuning_screen, root_note_selector)

    def callback21(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('G#', tuning_screen, root_note_selector)

    def callback22(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('G ', tuning_screen, root_note_selector)

    def callback23(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('F#', tuning_screen, root_note_selector)

    def callback24(self, instance, tuning_screen, root_note_selector):
        self.callback_root_note('F ', tuning_screen, root_note_selector)

    def root_note_select(self, tuning_screen):
        root_note_selector = BoxLayout()
        btn11 = Button(text='E')
        btn12 = Button(text='Eb')
        btn13 = Button(text='D')
        btn14 = Button(text='C#')
        btn15 = Button(text='C')
        btn16 = Button(text='B')
        btn17 = Button(text='Bb')
        btn18 = Button(text='A')
        btn19 = Button(text='G#')
        btn20 = Button(text='G')
        btn21 = Button(text='F#')
        btn22 = Button(text='F')
        btn11.bind(on_press=lambda instance: self.callback13(instance, tuning_screen, root_note_selector))
        btn12.bind(on_press=lambda instance: self.callback14(instance, tuning_screen, root_note_selector))
        btn13.bind(on_press=lambda instance: self.callback15(instance, tuning_screen, root_note_selector))
        btn14.bind(on_press=lambda instance: self.callback16(instance, tuning_screen, root_note_selector))
        btn15.bind(on_press=lambda instance: self.callback17(instance, tuning_screen, root_note_selector))
        btn16.bind(on_press=lambda instance: self.callback18(instance, tuning_screen, root_note_selector))
        btn17.bind(on_press=lambda instance: self.callback19(instance, tuning_screen, root_note_selector))
        btn18.bind(on_press=lambda instance: self.callback20(instance, tuning_screen, root_note_selector))
        btn19.bind(on_press=lambda instance: self.callback21(instance, tuning_screen, root_note_selector))
        btn20.bind(on_press=lambda instance: self.callback22(instance, tuning_screen, root_note_selector))
        btn21.bind(on_press=lambda instance: self.callback23(instance, tuning_screen, root_note_selector))
        btn22.bind(on_press=lambda instance: self.callback24(instance, tuning_screen, root_note_selector))
        root_note_selector.add_widget(btn11)
        root_note_selector.add_widget(btn12)
        root_note_selector.add_widget(btn13)
        root_note_selector.add_widget(btn14)
        root_note_selector.add_widget(btn15)
        root_note_selector.add_widget(btn16)
        root_note_selector.add_widget(btn17)
        root_note_selector.add_widget(btn18)
        root_note_selector.add_widget(btn19)
        root_note_selector.add_widget(btn20)
        root_note_selector.add_widget(btn21)
        root_note_selector.add_widget(btn22)
        tuning_screen.add_widget(root_note_selector)


class Empty(Widget):
    pass


class Grid(GridLayout):
    def __init__(self, rows, columns, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = columns

        dic = {0: 1, 1: .2, 2: .1}
        self.cols_minimum = dic


class Neck:
    def __init__(self, instrument):
        self.instrument = instrument

    def build_neck(self, screen):
        neck_screen = screen
        st = self.instrument.number_of_strings
        frets = self.instrument.number_of_frets
        neck = Grid(st + 4, frets + 3)

        for j in range(frets + 3):
            neck.add_widget(Empty())
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
        neck.add_widget(Empty())
        for k in range(len(notes)):
            notes[k].base_note = strings[notes[k].string_number - 1]
            notes[k].set_note()
            notes[k].other_notes = notes
            if notes[k].fret_number == 0:
                neck.add_widget(Label(text=str(notes[k].string_number)))
            neck.add_widget(notes[k])
            if notes[k].fret_number == frets:
                neck.add_widget(Empty())
        # Add Lables for frets
        neck.add_widget(Label(text='#'))
        for j in range(frets + 1):
            neck.add_widget(Label(text=str(j)))
        neck_screen.add_widget(neck)
        return neck_screen


class Manager(ScreenManager):
    pass


class FretNinjaApp(App):
    def build(self):
        sm = ScreenManager()
        tune = SetTuningScreen()
        sm.add_widget(create())
        sm.remove_widget(tune)
        return sm


if __name__ == '__main__':
    FretNinjaApp().run()