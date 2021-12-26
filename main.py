from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
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
        self.note = str(NoteHelper.find_note(self.base_note, self.fret_number))
        self.text = self.note
        self.background_color = (0,0,0,self.unhighlighted)

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
                    fret.background_color = self.set_color(self.unhighlighted)
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


class InstrumentInfo:
    instrument = Instrument()

    def callback_type(self, instance, instrument_type, screen, selector):
        self.instrument.instrument_type = instrument_type
        screen.remove_widget(selector)
        self.string_select(screen)

    def setup_info(self):
        tuning_screen = SetTuningScreen()
        instrument_selector = BoxLayout(orientation='vertical')
        w = Label()
        w.text = 'What instrument are you playing?'
        w.background_color = (1, 1, 1, 1)
        btn_guitar = Button(text='Guitar')
        btn_bass = Button(text='Bass')
        btn_guitar.bind(
            on_press=lambda instance: self.callback_type(instance, 'GUITAR', tuning_screen, instrument_selector))
        btn_bass.bind(
            on_press=lambda instance: self.callback_type(instance, 'BASS', tuning_screen, instrument_selector))
        instrument_selector.add_widget(w)
        instrument_selector.add_widget(btn_guitar)
        instrument_selector.add_widget(btn_bass)
        tuning_screen.add_widget(instrument_selector)
        return tuning_screen

    def setup_info_w_screen(self, screen):
        tuning_screen = screen
        instrument_selector = BoxLayout(orientation='vertical')
        w = Label()
        w.text = 'What instrument are you playing?'
        w.background_color = (1, 1, 1, 1)
        btn_guitar = Button(text='Guitar')
        btn_bass = Button(text='Bass')
        btn_guitar.bind(
            on_press=lambda instance: self.callback_type(instance, 'GUITAR', tuning_screen, instrument_selector))
        btn_bass.bind(
            on_press=lambda instance: self.callback_type(instance, 'BASS', tuning_screen, instrument_selector))
        instrument_selector.add_widget(w)
        instrument_selector.add_widget(btn_guitar)
        instrument_selector.add_widget(btn_bass)
        tuning_screen.add_widget(instrument_selector)
        return tuning_screen

    def callback_strings(self, instance, number, tuning_screen, string_selector):
        self.instrument.number_of_strings = number
        tuning_screen.remove_widget(string_selector)
        self.fret_select(tuning_screen)

    def string_select(self, tuning_screen):
        string_selector = BoxLayout(orientation='vertical')

        if self.instrument.instrument_type is 'GUITAR':
            w = Label(text='How many strings are on your guitar?')
            btn_six = Button(text='6')
            btn_six.bind(on_press=lambda instance: self.callback_strings(instance, 6, tuning_screen, string_selector))
            btn_seven = Button(text='7')
            btn_seven.bind(on_press=lambda instance: self.callback_strings(instance, 7, tuning_screen, string_selector))
            string_selector.add_widget(w)
            string_selector.add_widget(btn_six)
            string_selector.add_widget(btn_seven)
        elif self.instrument.instrument_type is 'BASS':
            w = Label(text='How many strings are on your bass?')
            btn_four = Button(text='4')
            btn_four.bind(on_press=lambda instance: self.callback_strings(instance, 4, tuning_screen, string_selector))
            btn_five = Button(text='5')
            btn_five.bind(on_press=lambda instance: self.callback_strings(instance, 5, tuning_screen, string_selector))
            string_selector.add_widget(w)
            string_selector.add_widget(btn_four)
            string_selector.add_widget(btn_five)
        string_selector.text = 'how many strings is your ' + Instrument.instrument_type + '?'

        tuning_screen.add_widget(string_selector)

    def callback_fret_number(self, instance, number, tuning_screen, number_of_frets_selector):
        self.instrument.number_of_frets = number
        tuning_screen.remove_widget(number_of_frets_selector)
        self.tuning_select(tuning_screen)

    def fret_select(self, tuning_screen):
        number_of_frets_selector = BoxLayout(orientation='vertical')
        w = Label(text='How many frets are on your instrument?')
        btn_twenty_two = Button(text='22')
        btn_twenty_two.bind(
            on_press=lambda instance: self.callback_fret_number(instance, 22, tuning_screen, number_of_frets_selector))
        btn_twenty_four = Button(text='24')
        btn_twenty_four.bind(
            on_press=lambda instance: self.callback_fret_number(instance, 24, tuning_screen, number_of_frets_selector))
        number_of_frets_selector.add_widget(w)
        number_of_frets_selector.add_widget(btn_twenty_two)
        number_of_frets_selector.add_widget(btn_twenty_four)
        tuning_screen.add_widget(number_of_frets_selector)

    def callback_tuning_style(self, instance, style, structure, tuning_screen):
        self.instrument.tuning_style = style
        tuning_screen.remove_widget(structure)
        self.root_note_select(tuning_screen)

    def callback_start_custom(self, instance, structure, tuning_screen):
        self.instrument.tuning_style = 'CUSTOM'
        tuning_screen.remove_widget(structure)
        self.instrument.tuning = [0] * self.instrument.number_of_strings
        self.custom_select(tuning_screen, 1)

    def tuning_select(self, tuning_screen):
        structure = BoxLayout(orientation='vertical')

        w = Label()
        w.text = 'What tuning is your ' + str(
            self.instrument.number_of_strings) + ' ' + self.instrument.instrument_type.lower() + ' in?'
        tuning_selector = BoxLayout()
        if self.instrument.instrument_type is 'GUITAR':
            btn_standard = Button(text='Standard')
            btn_drop = Button(text='Drop')
            btn_open = Button(text='Open')
            btn_custom = Button(text='Custom')
            btn_standard.bind(
                on_press=lambda instance: self.callback_tuning_style(instance, 'STANDARD', structure, tuning_screen))
            btn_drop.bind(
                on_press=lambda instance: self.callback_tuning_style(instance, 'DROP', structure, tuning_screen))
            btn_open.bind(
                on_press=lambda instance: self.callback_tuning_style(instance, 'OPEN', structure, tuning_screen))
            btn_custom.bind(on_press=lambda instance: self.callback_start_custom(instance, structure, tuning_screen))
            tuning_selector.add_widget(btn_standard)
            tuning_selector.add_widget(btn_drop)
            tuning_selector.add_widget(btn_open)
            tuning_selector.add_widget(btn_custom)
        structure.add_widget(w)
        structure.add_widget(tuning_selector)
        tuning_screen.add_widget(structure)

    def callback_root_note(self, instance, note, tuning_screen, s):
        self.instrument.root_note = note
        tuning_screen.remove_widget(s)
        self.instrument.calculate()
        neck = Neck(self.instrument, self)
        neck.build_neck(tuning_screen)

    def callback_custom(self, instance, note, string, tuning_screen, structure):
        self.instrument.tuning[string - 1] = note
        tuning_screen.remove_widget(structure)
        if string < self.instrument.number_of_strings:
            self.custom_select(tuning_screen, string + 1)
        else:
            neck = Neck(self.instrument, self)
            neck.build_neck(tuning_screen)

    def root_note_select(self, tuning_screen):
        structure = BoxLayout(orientation='vertical')
        w = Label()
        w.text = 'What is your low note?'
        root_note_selector = BoxLayout()
        buttons = []
        for i in range(12):
            buttons.append(type('btn' + str(i), (Button,), {})())
            buttons[i].text=NoteHelper.number_to_note(i+1)
            buttons[i].bind(on_press=lambda instance: self.callback_root_note(instance,
                                                                                            NoteHelper.number_to_note(
                                                                                                i+1), tuning_screen,
                                                                                            structure))
            root_note_selector.add_widget(buttons[i])
        structure.add_widget(w)
        structure.add_widget(root_note_selector)
        tuning_screen.add_widget(structure)

    def custom_select(self, tuning_screen, string):
        structure = BoxLayout(orientation='vertical')
        l = Label()
        l.text = 'what is your ' + str(string) + ' string tuned to?'
        cs_selector = BoxLayout()
        buttons = []
        for i in range(12):
            buttons.append(type('btn' + str(i), (Button,), {})())
            buttons[i].text=NoteHelper.number_to_note(i+1)
            buttons[i].bind(on_press=lambda instance: self.callback_custom(instance,
                                                                        NoteHelper.number_to_note(
                                                                            i + 1), tuning_screen,
                                                                        structure))
            cs_selector.add_widget(buttons[i])
        structure.add_widget(l)
        structure.add_widget(cs_selector)
        tuning_screen.add_widget(structure)


class Empty(Widget):
    pass


class Grid(GridLayout):
    def __init__(self, rows, columns, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = columns

        dic = {0: 1, 1: .2, 2: .1}
        self.cols_minimum = dic


class Menu(AnchorLayout):
    def __init__(self, instrument, screen, **kwargs):
        super().__init__(**kwargs)
        self.instrument = instrument
        self.screen = screen

    anchor_x = 'left'
    anchor_y = 'top'
    btn_retune = Button(text='retune')
    # btn_retune.bind(on_press=lambda instance:


class Neck():
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
        self.neck = Grid(st + 4, frets + 3)
        menu = AnchorLayout()
        menu.size_hint = (1, .17)
        back_button = Button(text='back')
        back_button.bind(on_press=lambda instance: self.callback_back(instance, screen, structure))
        menu.add_widget(back_button)
        structure.add_widget(menu)

        for j in range(frets + 3):
            self.neck.add_widget(Empty())
        strings = self.instrument.tuning
        notes = []
        # Create Frets dynamically named String'number'Fret'number
        for i in range(st):
            for j in range(frets + 1):
                notes.append(type("String" + str(6 - i) + "Fret" + str(j), (Fret,), {})())
        # Assign notes and add to neck
        self.neck.add_widget(Label(text='#'))
        for k in range(frets + 1):
            self.neck.add_widget(Label(text=str(k)))
        self.neck.add_widget(Empty())
        for note in notes:
            note.base_note = strings[note.string_number - 1]
            note.set_note()
            note.other_notes = notes
            if note.fret_number is 0:
                self.neck.add_widget(Label(text=str(note.string_number)))
            self.neck.add_widget(note)
            if note.fret_number is frets:
                self.neck.add_widget(Empty())
        # Add Lables for frets
        self.neck.add_widget(Label(text='#'))
        for j in range(frets + 1):
            self.neck.add_widget(Label(text=str(j)))
        structure.add_widget(self.neck)
        neck_screen.add_widget(structure)
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
