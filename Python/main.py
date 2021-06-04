from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import noteFinder

class GuitarTheory(Widget):
    pass
class WindowManager(ScreenManager):
    pass
class NeckScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class Fret0:
    pass
class Fret:
    def __init__(self):
        nameLength = len(self.__class__.__name__)
        if self.__class__.__name__[nameLength-2].isdigit():
            self.fretNumber=int(self.__class__.__name__[nameLength-2:nameLength])
        else:
            self.fretNumber=int(self.__class__.__name__[nameLength-1])
        self.stringNumber = int(self.__class__.__name__[6])
        self.baseNote = "G"

    def Set_note(self, base):
        if self.fretNumber == 0:
            self.note = self.baseNote
            self.text = self.note
        else:
            self.note = str(noteFinder.findNote(base,self.fretNumber))
            self.text = self.note

class Tuning(DropDown):
    pass
class empty(Widget):
    pass
class Grid(GridLayout):
    def __init__(self, rows, columns,**kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = columns

class GuitarApp(App):
    def build(self):
        neckScreen = NeckScreen()
        st = 6
        frets = 24
        neck = Grid(st+4, frets+2)

        for j in range(frets+2):
            neck.add_widget(empty())
        strings=['E','A','D','G', 'B', 'E']
        notes = []
        #Create Frets dynamically named String'number'Fret'number
        for i in range(st):
            for j in range(frets+1):
                notes.append(type("String"+str(6-i)+"Fret"+str(j),(Button, Fret),{})())
        #Assign notes and add to neck
        for k in range(len(notes)):
            notes[k].__init__()
            notes[k].baseNote=strings[notes[k].stringNumber-1]
            notes[k].Set_note(notes[k].baseNote)
            print(notes[k].stringNumber)
            if notes[k].fretNumber == 0:
                neck.add_widget(Label(text=str(notes[k].stringNumber)))
            neck.add_widget(notes[k])
        #Add Lables for frets
        neck.add_widget(Label(text='#'))
        for j in range(frets+1):
            neck.add_widget(Label(text=str(j)))
        neckScreen.add_widget(neck)
        return neckScreen


if __name__ == '__main__':
    GuitarApp().run()