from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import NoteHelper


class GuitarTheory(Widget):
    pass
class WindowManager(ScreenManager):
    pass

class NeckScreen(Screen):
    def create(self):
        neck = Neck()
        return neck.buildNeck()

class MenuScreen(Screen):
 pass

class Fret0:
    pass
class Fret(Button):
    baseNote = "G"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        nameLength = len(self.__class__.__name__)
        if self.__class__.__name__[nameLength-2].isdigit():
            self.fretNumber=int(self.__class__.__name__[nameLength-2:nameLength])
        else:
            self.fretNumber=int(self.__class__.__name__[nameLength-1])
        self.stringNumber = int(self.__class__.__name__[6])

    def set_note(self):
        self.note = str(NoteHelper.findNote(self.baseNote, self.fretNumber))
        self.text = self.note
        self.background_color = self.setColor(1)

    def setColor(self, opacity):
        return NoteHelper.colorNote(self.note, opacity)

class Tuning(DropDown):
    pass
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
        st = 6
        frets = 24
        neck = Grid(st + 4, frets + 3)

        for j in range(frets + 3):
            neck.add_widget(Empty())
        strings = ['C', 'G', 'C', 'F', 'A', 'D']
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


class GuitarApp(App):
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(MenuScreen())
        sm.add_widget(NeckScreen().create())
        return sm

if __name__ == '__main__':
    GuitarApp().run()