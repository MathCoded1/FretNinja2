from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from utilities import NoteHelper
from . Neck import Neck as Neck
from utilities.Instrument import Instrument as Instrument
from . MainScreen import SetTuningScreen as SetTuningScreen


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

    def callback_back_from_root_note(self,instance,tuning_screen,structure):
        tuning_screen.remove_widget(structure)
        self.tuning_select(tuning_screen)

    def root_note_select(self, tuning_screen):
        self.instrument.root_note = ''
        structure = BoxLayout(orientation='vertical')
        btn = Button(text='Back')
        btn.bind(on_press=lambda instance: self.callback_back_from_root_note(instance, tuning_screen, structure))
        structure.add_widget(btn)
        w = Label()
        w.text = 'What is your low note?'
        root_note_selector = BoxLayout()
        buttons = []
        for i in range(12):
            buttons.append(type('btn' + str(i), (Button,), {})())
            buttons[i].text = NoteHelper.number_to_note(i + 1)
            buttons[i].bind(on_press=lambda instance, bound_i=i: self.callback_root_note(instance,
                                                                                         NoteHelper.number_to_note(
                                                                                             bound_i + 1),
                                                                                         tuning_screen,
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
            buttons[i].text = NoteHelper.number_to_note(i + 1)
            buttons[i].bind(on_press=lambda instance, bound_i=i: self.callback_custom(instance,
                                                                                      NoteHelper.number_to_note(
                                                                                          bound_i + 1), string,
                                                                                      tuning_screen,
                                                                                      structure))
            cs_selector.add_widget(buttons[i])
        structure.add_widget(l)
        structure.add_widget(cs_selector)
        tuning_screen.add_widget(structure)
