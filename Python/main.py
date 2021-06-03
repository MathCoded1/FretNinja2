from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import fillNeck

class GuitarTheory(Widget):
    pass

class WindowManager(ScreenManager):
    pass

class NeckScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

class String:
    pass


class Fret:
    def __init__(self):
        nameLength = len(self.__class__.__name__)
        if self.__class__.__name__[nameLength-2].isdigit():
            self.fretNumber=self.__class__.__name__[nameLength-2:nameLength]
        else:
            self.fretNumber=self.__class__.__name__[nameLength-1]
        self.note = self.Set_note()
    def Set_note(self):
        pass

class Tuning(DropDown):
    pass

class empty(Widget):
    pass

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 10
        self.cols = 25


class GuitarApp(App):
    def build(self):
        neckScreen = NeckScreen()
        neck = Grid()
        st = 6
        fr = 24
        for j in range(fr+1):
            neck.add_widget(empty())

        for i in range(st):
            for j in range(fr+1):
                neck.add_widget(type("String"+str(i)+"Fret"+str(j),(Button, Fret),{})())
        for j in range(fr+1):
            neck.add_widget(Label(text=str(j)))
        neckScreen.add_widget(neck)
        return neckScreen


if __name__ == '__main__':
    GuitarApp().run()