from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from Instrument import Instrument as Instrument
import NoteHelper



class GuitarTheory(Widget):
    pass
class WindowManager(ScreenManager):
    pass

class NeckScreen(Screen):
    name = 'neckScr'
    def create(self):
        neck = Neck()
        return neck.buildNeck()
class SetTuningScreen(Screen):
    name = 'infoScr'
    def create(self):
        info = InstrumentInfo()
        return info.setupInfo()

class MenuScreen(Screen):
 pass

class Fret0:
    pass
class Fret(Button):
    baseNote = "G"
    otherNotes = []
    highlighted = False
    unhighlighted = .13
    def set_note(self):
        self.note = str(NoteHelper.findNote(self.baseNote, self.fretNumber))
        self.text = self.note
        self.background_color = self.setColor(self.unhighlighted)

    def setColor(self, opacity):
        return NoteHelper.colorNote(self.note, opacity)

    def callback(self,instance):
        if self.highlighted is False:
            self.background_color=self.setColor(1)
            self.highlighted = True
            for fret in self.otherNotes:
                if fret.note is self.note:
                    fret.background_color=self.setColor(1)
                    fret.highlighted=True
        else:
            self.background_color=self.setColor(self.unhighlighted)
            self.highlighted = False
            for fret in self.otherNotes:
                if fret.note is self.note:
                    fret.background_color = self.setColor(self.unhighlighted)
                    fret.highlighted=False

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

    def __init__(self):
        self.btn = Button(text='Guitar')
        self.btn2 = Button(text='Bass')

    def callback(self,instance,a,b):
        Instrument.type = 'GUITAR'
        a.remove_widget(b)
        self.stringSelect(a)

    def callback2(self, instance,a,b):
        Instrument.type = 'BASS'
        a.remove_widget(b)
        self.stringSelect(a)

    def setupInfo(self):
        tuningScreen = SetTuningScreen()
        InstrumentSelector = BoxLayout(orientation='vertical')
        self.btn.bind(on_press=lambda instance : self.callback(instance,tuningScreen,InstrumentSelector))
        self.btn2.bind(on_press=lambda instance: self.callback2(instance,tuningScreen,InstrumentSelector))
        InstrumentSelector.add_widget(self.btn)
        InstrumentSelector.add_widget(self.btn2)
        tuningScreen.add_widget(InstrumentSelector)
        return tuningScreen

    def callback3(self, instance,tuningScreen,stringSelector):
        Instrument.numberOfStrings = 6
        tuningScreen.remove_widget(stringSelector)
        self.fretSelect(tuningScreen)

    def callback4(self,instance, tuningScreen,stringSelector):
        Instrument.numberOfStrings = 7
        tuningScreen.remove_widget(stringSelector)
        self.fretSelect(tuningScreen)
    def callback5(self, instance,tuningScreen,stringSelector):
        Instrument.numberOfStrings = 4
        tuningScreen.remove_widget(stringSelector)
        self.fretSelect(tuningScreen)
    def callback6(self, instance,tuningScreen,stringSelector):
        Instrument.numberOfStrings = 5
        tuningScreen.remove_widget(stringSelector)
        self.fretSelect(tuningScreen)
    def stringSelect(self,tuningScreen):
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
        Instrument.numberOfFrets = 22
        tuningScreen.remove_widget(numberOfFretsSelector)
        self.tuningSelect(tuningScreen)

    def callback8(self,instance,tuningScreen,numberOfFretsSelector):
        Instrument.numberOfFrets = 24
        tuningScreen.remove_widget(numberOfFretsSelector)
        self.tuningSelect(tuningScreen)

    def fretSelect(self, tuningScreen):
        numberOfFretsSelector=BoxLayout(orientation='vertical')
        btn5=Button(text ='22')
        btn5.bind(on_press=lambda instance:self.callback7(instance,tuningScreen,numberOfFretsSelector))
        btn6=Button(text='24')
        btn6.bind(on_press=lambda instance:self.callback8(instance,tuningScreen,numberOfFretsSelector))
        numberOfFretsSelector.add_widget(btn5)
        numberOfFretsSelector.add_widget(btn6)
        tuningScreen.add_widget(numberOfFretsSelector)

    def callback9(self,instance,tuningScreen,tuningSelector):
        Instrument.tuning = ['E', 'A' , 'D' ,'G' , 'B', 'E']
        tuningScreen.remove_widget(tuningSelector)
        tuningScreen.manager.current = 'NeckScreen'

    def tuningSelect(self,tuningScreen):
        tuningSelector=BoxLayout()

        tuningSelector.text = 'What tuning is your ' + str(Instrument.numberOfStrings) + ' ' + Instrument.type + ' in?'
        if Instrument.type is 'GUITAR' and Instrument.numberOfStrings is 6:
            btn7 = Button(text = 'Standard')
            btn7.bind(on_press=lambda instance:self.callback9(instance,tuningScreen,tuningSelector))
            tuningSelector.add_widget(btn7)
        tuningScreen.add_widget(tuningSelector)

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
    def buildNeck(self):
        neckScreen = NeckScreen()
        st = Instrument.numberOfStrings
        frets = Instrument.numberOfFrets
        neck = Grid(st + 4, frets + 3)

        for j in range(frets + 3):
            neck.add_widget(Empty())
        strings = Instrument.tuning
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
    screen_one=SetTuningScreen()
    screen_two=NeckScreen()
class FretNinjaApp(App):
    def build(self):
        sm = Manager()
        sm.current = 'infoScr'
        sm.current.create()

        return sm

if __name__ == '__main__':
    FretNinjaApp().run()