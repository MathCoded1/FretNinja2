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

    def __init__(self,**kwargs):
        super(SetTuningScreen,self).__init__(**kwargs)
        self.name = 'infoScr'


class Fret(Button):
    baseNote = "G"
    otherNotes = []
    highlighted = False
    unhighlighted = .13
    note = ''
    
    def set_note(self):
        self.note = str(NoteHelper.findNote(self.baseNote, self.fretNumber))
        self.text = self.note
        self.background_color = self.set_color(self.unhighlighted)

    def set_color(self, opacity):
        return NoteHelper.colorNote(self.note, opacity)

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
        nameLength = len(self.__class__.__name__)
        self.bind(on_press=self.callback)
        if self.__class__.__name__[nameLength-2].isdigit():
            self.fretNumber=int(self.__class__.__name__[nameLength-2:nameLength])
        else:
            self.fretNumber=int(self.__class__.__name__[nameLength-1])
        self.stringNumber = int(self.__class__.__name__[6])


class InstrumentInfo:
    instrument = Instrument()

    def callback(self, instance, a, b):
        self.instrument.type = 'GUITAR'
        a.remove_widget(b)
        self.stringSelect(a)

    def callback2(self, instance, a, b):
        self.instrument.type = 'BASS'
        a.remove_widget(b)
        self.stringSelect(a)

    def setup_info(self):
        tuningScreen = SetTuningScreen()
        InstrumentSelector = BoxLayout(orientation='vertical')
        btn = Button(text='Guitar')
        btn2 = Button(text='Bass')
        btn.bind(on_press=lambda instance: self.callback(instance, tuningScreen, InstrumentSelector))
        btn2.bind(on_press=lambda instance: self.callback2(instance, tuningScreen, InstrumentSelector))
        InstrumentSelector.add_widget(btn)
        InstrumentSelector.add_widget(btn2)
        tuningScreen.add_widget(InstrumentSelector)
        return tuningScreen

    def callback3(self, instance, tuningScreen, stringSelector):
        self.instrument.numberOfStrings = 6
        tuningScreen.remove_widget(stringSelector)
        self.fret_select(tuningScreen)

    def callback4(self,instance, tuningScreen, stringSelector):
        self.instrument.numberOfStrings = 7
        tuningScreen.remove_widget(stringSelector)
        self.fret_select(tuningScreen)

    def callback5(self, instance, tuningScreen, stringSelector):
        self.instrument.numberOfStrings = 4
        tuningScreen.remove_widget(stringSelector)
        self.fret_select(tuningScreen)

    def callback6(self, instance, tuningScreen, stringSelector):
        self.instrument.numberOfStrings = 5
        tuningScreen.remove_widget(stringSelector)
        self.fret_select(tuningScreen)

    def stringSelect(self, tuningScreen):
        stringSelector = BoxLayout(orientation='vertical')

        if Instrument.type is 'GUITAR':
            btn3 = Button(text = '6')
            btn3.bind(on_press= lambda instance: self.callback3(instance,tuningScreen,stringSelector))
            btn4 = Button(text = '7')
            btn4.bind(on_press=lambda instance: self.callback4(instance,tuningScreen,stringSelector))
            stringSelector.add_widget(btn3)
            stringSelector.add_widget(btn4)
        else:
            btn5 = Button(text = '4')
            btn5.bind(on_press=lambda instance:self.callback5(instance,tuningScreen,stringSelector))
            btn6 = Button(text = '5')
            btn6.bind(on_press=lambda instance:self.callback6(instance,tuningScreen,stringSelector))
            stringSelector.add_widget(btn5)
            stringSelector.add_widget(btn6)
        stringSelector.text='how many strings is your '+Instrument.type+'?'

        tuningScreen.add_widget(stringSelector)

    def callback7(self,instance,tuningScreen,numberOfFretsSelector):
        self.instrument.numberOfFrets = 22
        tuningScreen.remove_widget(numberOfFretsSelector)
        self.tuning_select(tuningScreen)

    def callback8(self,instance,tuningScreen,numberOfFretsSelector):
        self.instrument.numberOfFrets = 24
        tuningScreen.remove_widget(numberOfFretsSelector)
        self.tuning_select(tuningScreen)

    def fret_select(self, tuningScreen):
        numberOfFretsSelector=BoxLayout(orientation='vertical')
        btn5=Button(text='22')
        btn5.bind(on_press=lambda instance:self.callback7(instance, tuningScreen, numberOfFretsSelector))
        btn6=Button(text='24')
        btn6.bind(on_press=lambda instance:self.callback8(instance, tuningScreen, numberOfFretsSelector))
        numberOfFretsSelector.add_widget(btn5)
        numberOfFretsSelector.add_widget(btn6)
        tuningScreen.add_widget(numberOfFretsSelector)

    def callback9(self, instance, tuningScreen, tuningSelector):
        self.instrument.tuningStyle = 'STANDARD'
        tuningScreen.remove_widget(tuningSelector)
        self.root_note_select(tuningScreen)

    def callback10(self, instance, tuningScreen, tuningSelector):
        self.instrument.tuningStyle = 'DROP'
        tuningScreen.remove_widget(tuningSelector)
        self.root_note_select(tuningScreen)

    def callback11(self, instance, tuningScreen, tuningSelector):
        self.instrument.tuningStyle = 'OPEN'
        tuningScreen.remove_widget(tuningSelector)
        self.root_note_select(tuningScreen)

    def callback12(self, instance, tuningScreen, tuningSelector):
        self.instrument.tuningStyle = 'CUSTOM'
        tuningScreen.remove_widget(tuningSelector)
        self.root_note_select(tuningSelector)

    def tuning_select(self, tuningScreen):
        tuningSelector=BoxLayout()

        tuningSelector.text = 'What tuning is your ' + str(self.instrument.numberOfStrings) + ' ' + Instrument.type + ' in?'
        if self.instrument.type is 'GUITAR':
            btn7 = Button(text='Standard')
            btn8=Button(text='Drop')
            btn9=Button(text='Open')
            btn10=Button(text='Custom')
            btn7.bind(on_press=lambda instance:self.callback9(instance, tuningScreen, tuningSelector))
            btn8.bind(on_press=lambda instance:self.callback10(instance, tuningScreen, tuningSelector))
            btn9.bind(on_press=lambda instance:self.callback11(instance, tuningScreen, tuningSelector))
            btn10.bind(on_press=lambda instance: self.callback12(instance, tuningScreen, tuningSelector))
            tuningSelector.add_widget(btn7)
            tuningSelector.add_widget(btn8)
            tuningSelector.add_widget(btn9)
            tuningSelector.add_widget(btn10)
        tuningScreen.add_widget(tuningSelector)

    def callback_root_note(self, note, tuningScreen, rootNoteSelector):
        self.instrument.rootNote = note
        tuningScreen.remove_widget(rootNoteSelector)
        self.instrument.calculate()
        neck = Neck(self.instrument)
        neck.build_neck(tuningScreen)

    def callback13(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('E ', tuningScreen, rootNoteSelector)

    def callback14(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('D#', tuningScreen, rootNoteSelector)

    def callback15(self,instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('D ', tuningScreen, rootNoteSelector)

    def callback16(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('C#', tuningScreen, rootNoteSelector)

    def callback17(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('C ', tuningScreen, rootNoteSelector)

    def callback18(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('B ', tuningScreen, rootNoteSelector)

    def callback19(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('A#', tuningScreen, rootNoteSelector)

    def callback20(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('A ', tuningScreen, rootNoteSelector)

    def callback21(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('G#', tuningScreen, rootNoteSelector)

    def callback22(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('G ', tuningScreen, rootNoteSelector)

    def callback23(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('F#', tuningScreen, rootNoteSelector)

    def callback24(self, instance, tuningScreen, rootNoteSelector):
        self.callback_root_note('F ', tuningScreen, rootNoteSelector)

    def root_note_select(self, tuningScreen):
        rootNoteSelector=BoxLayout()
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
        btn11.bind(on_press=lambda instance: self.callback13(instance, tuningScreen, rootNoteSelector))
        btn12.bind(on_press=lambda instance: self.callback14(instance, tuningScreen, rootNoteSelector))
        btn13.bind(on_press=lambda instance: self.callback15(instance, tuningScreen, rootNoteSelector))
        btn14.bind(on_press=lambda instance: self.callback16(instance, tuningScreen, rootNoteSelector))
        btn15.bind(on_press=lambda instance: self.callback17(instance, tuningScreen, rootNoteSelector))
        btn16.bind(on_press=lambda instance: self.callback18(instance, tuningScreen, rootNoteSelector))
        btn17.bind(on_press=lambda instance: self.callback19(instance, tuningScreen, rootNoteSelector))
        btn18.bind(on_press=lambda instance: self.callback20(instance, tuningScreen, rootNoteSelector))
        btn19.bind(on_press=lambda instance: self.callback21(instance, tuningScreen, rootNoteSelector))
        btn20.bind(on_press=lambda instance: self.callback22(instance, tuningScreen, rootNoteSelector))
        btn21.bind(on_press=lambda instance: self.callback23(instance, tuningScreen, rootNoteSelector))
        btn22.bind(on_press=lambda instance: self.callback24(instance, tuningScreen, rootNoteSelector))
        rootNoteSelector.add_widget(btn11)
        rootNoteSelector.add_widget(btn12)
        rootNoteSelector.add_widget(btn13)
        rootNoteSelector.add_widget(btn14)
        rootNoteSelector.add_widget(btn15)
        rootNoteSelector.add_widget(btn16)
        rootNoteSelector.add_widget(btn17)
        rootNoteSelector.add_widget(btn18)
        rootNoteSelector.add_widget(btn19)
        rootNoteSelector.add_widget(btn20)
        rootNoteSelector.add_widget(btn21)
        rootNoteSelector.add_widget(btn22)
        tuningScreen.add_widget(rootNoteSelector)


class Empty(Widget):
    pass


class Grid(GridLayout):
    def __init__(self, rows, columns,**kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = columns


        dic = {0:1, 1:.2,2:.1}
        self.cols_minimum = dic


class Neck:
    def __init__(self,instrument):
        self.instrument=instrument

    def build_neck(self, screen):
        neckScreen = screen
        st = self.instrument.numberOfStrings
        frets = self.instrument.numberOfFrets
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
        for k in range(frets+1):
            neck.add_widget(Label(text=str(k)))
        neck.add_widget(Empty())
        for k in range(len(notes)):
            notes[k].baseNote = strings[notes[k].stringNumber - 1]
            notes[k].set_note()
            notes[k].otherNotes=notes
            if notes[k].fretNumber == 0:
                neck.add_widget(Label(text=str(notes[k].stringNumber)))
            neck.add_widget(notes[k])
            if notes[k].fretNumber == frets:
                neck.add_widget(Empty())
        # Add Lables for frets
        neck.add_widget(Label(text='#'))
        for j in range(frets + 1):
            neck.add_widget(Label(text=str(j)))
        neckScreen.add_widget(neck)
        return neckScreen


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