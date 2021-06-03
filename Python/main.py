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
        self.BaseNote = "G"

    def Set_note(self, base):
        self.note = str(noteFinder.findNote(base,self.fretNumber-1))
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
        fr = 24
        neck = Grid(st+4, fr+1)

        for j in range(fr+1):
            neck.add_widget(empty())
        strings=['E','B','G','D', 'B', 'E']
        frets = []
        for i in range(st):
            for j in range(fr+1):
                frets.append(type("String"+str(i+1)+"Fret"+str(j+1),(Button, Fret),{})())
        for k in range(len(frets)):
            stringNum = int(frets[k].__class__.__name__[6])
            frets[k].BaseNote=strings[stringNum-1]
            frets[k].Set_note(frets[k].BaseNote)
            neck.add_widget(frets[k])

        for j in range(fr+1):
            neck.add_widget(Label(text=str(j)))
        neckScreen.add_widget(neck)gg
        return neckScreen


if __name__ == '__main__':
    GuitarApp().run()