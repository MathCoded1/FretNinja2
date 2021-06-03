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

class String1Fret0(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret0, self).__init__(**kwargs)
        self.text = 'E'

class String2Fret0(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret0, self).__init__(**kwargs)
        self.text = 'A'
        self.fret = 0

class String3Fret0(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret0, self).__init__(**kwargs)
        self.text = 'D'

class String4Fret0(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret0, self).__init__(**kwargs)
        self.text = 'G'

class String5Fret0(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret0, self).__init__(**kwargs)
        self.text = 'B'

class String6Fret0(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret0, self).__init__(**kwargs)
        self.text = 'E'

class String1Fret1(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret1, self).__init__(**kwargs)
        self.text = 'F'

class String2Fret1(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret1, self).__init__(**kwargs)
        self.text = 'A#'

class String3Fret1(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret1, self).__init__(**kwargs)
        self.text = 'D#'

class String4Fret1(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret1, self).__init__(**kwargs)
        self.text = 'G#'

class String5Fret1(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret1, self).__init__(**kwargs)
        self.text = 'C'

class String6Fret1(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret1, self).__init__(**kwargs)
        self.text = 'F'

class String1Fret2(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret2, self).__init__(**kwargs)
        self.text = 'F#'

class String2Fret2(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret2, self).__init__(**kwargs)
        self.text = 'B'

class String3Fret2(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret2, self).__init__(**kwargs)
        self.text = 'E'

class String4Fret2(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret2, self).__init__(**kwargs)
        self.text = 'A'

class String5Fret2(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret2, self).__init__(**kwargs)
        self.text = 'C#'

class String6Fret2(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret2, self).__init__(**kwargs)
        self.text = 'F#'

class String1Fret3(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret3, self).__init__(**kwargs)
        self.text = 'G'

class String2Fret3(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret3, self).__init__(**kwargs)
        self.text = 'C'

class String3Fret3(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret3, self).__init__(**kwargs)
        self.text = 'F'

class String4Fret3(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret3, self).__init__(**kwargs)
        self.text = 'A#'

class String5Fret3(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret3, self).__init__(**kwargs)
        self.text = 'D'

class String6Fret3(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret3, self).__init__(**kwargs)
        self.text = 'G'

class String1Fret4(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret4, self).__init__(**kwargs)
        self.text = 'G#'

class String2Fret4(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret4, self).__init__(**kwargs)
        self.text = 'C#'

class String3Fret4(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret4, self).__init__(**kwargs)
        self.text = 'F#'

class String4Fret4(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret4, self).__init__(**kwargs)
        self.text = 'B'

class String5Fret4(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret4, self).__init__(**kwargs)
        self.text = 'D#'

class String6Fret4(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret4, self).__init__(**kwargs)
        self.text = 'G#'

class String1Fret5(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret5, self).__init__(**kwargs)
        self.text = 'A'

class String2Fret5(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret5, self).__init__(**kwargs)
        self.text = 'D'

class String3Fret5(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret5, self).__init__(**kwargs)
        self.text = 'G'
class String4Fret5(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret5, self).__init__(**kwargs)
        self.text = 'C'

class String5Fret5(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret5, self).__init__(**kwargs)
        self.text = 'E'

class String6Fret5(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret5, self).__init__(**kwargs)
        self.text = 'A'

class String1Fret6(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret6, self).__init__(**kwargs)
        self.text = 'A#'

class String2Fret6(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret6, self).__init__(**kwargs)
        self.text = 'D#'

class String3Fret6(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret6, self).__init__(**kwargs)
        self.text = 'G#'

class String4Fret6(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret6, self).__init__(**kwargs)
        self.text = 'C#'

class String5Fret6(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret6, self).__init__(**kwargs)
        self.text = 'F'

class String6Fret6(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret6, self).__init__(**kwargs)
        self.text = 'A#'

class String1Fret7(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret7, self).__init__(**kwargs)
        self.text = 'B'

class String2Fret7(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret7, self).__init__(**kwargs)
        self.text = 'E'

class String3Fret7(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret7, self).__init__(**kwargs)
        self.text = 'A'

class String4Fret7(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret7, self).__init__(**kwargs)
        self.text = 'D'

class String5Fret7(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret7, self).__init__(**kwargs)
        self.text = 'F#'

class String6Fret7(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret7, self).__init__(**kwargs)
        self.text = 'B'

class String1Fret8(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret8, self).__init__(**kwargs)
        self.text = 'C'

class String2Fret8(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret8, self).__init__(**kwargs)
        self.text = 'F'

class String3Fret8(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret8, self).__init__(**kwargs)
        self.text = 'A#'

class String4Fret8(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret8, self).__init__(**kwargs)
        self.text = 'D#'

class String5Fret8(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret8, self).__init__(**kwargs)
        self.text = 'G'

class String6Fret8(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret8, self).__init__(**kwargs)
        self.text = 'C'

class String1Fret9(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret9, self).__init__(**kwargs)
        self.text = 'C#'

class String2Fret9(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret9, self).__init__(**kwargs)
        self.text = 'F#'

class String3Fret9(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret9, self).__init__(**kwargs)
        self.text = 'B'

class String4Fret9(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret9, self).__init__(**kwargs)
        self.text = 'E'

class String5Fret9(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret9, self).__init__(**kwargs)
        self.text = 'G#'

class String6Fret9(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret9, self).__init__(**kwargs)
        self.text = 'C#'

class String1Fret10(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret10, self).__init__(**kwargs)
        self.text = 'D'

class String2Fret10(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret10, self).__init__(**kwargs)
        self.text = 'G'

class String3Fret10(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret10, self).__init__(**kwargs)
        self.text = 'C'

class String4Fret10(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret10, self).__init__(**kwargs)
        self.text = 'F'

class String5Fret10(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret10, self).__init__(**kwargs)
        self.text = 'A'

class String6Fret10(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret10, self).__init__(**kwargs)
        self.text = 'D'

class String1Fret11(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret11, self).__init__(**kwargs)
        self.text = 'D#'

class String2Fret11(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret11, self).__init__(**kwargs)
        self.text = 'G#'

class String3Fret11(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret11, self).__init__(**kwargs)
        self.text = 'C#'

class String4Fret11(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret11, self).__init__(**kwargs)
        self.text = 'F#'

class String5Fret11(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret11, self).__init__(**kwargs)
        self.text = 'A#'

class String6Fret11(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret11, self).__init__(**kwargs)
        self.text = 'D#'

class String1Fret12(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret12, self).__init__(**kwargs)
        self.text = 'E'

class String2Fret12(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret12, self).__init__(**kwargs)
        self.text = 'A'

class String3Fret12(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret12, self).__init__(**kwargs)
        self.text = 'D'

class String4Fret12(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret12, self).__init__(**kwargs)
        self.text = 'G'

class String5Fret12(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret12, self).__init__(**kwargs)
        self.text = 'B'

class String6Fret12(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret12, self).__init__(**kwargs)
        self.text = 'E'

class String1Fret13(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret13, self).__init__(**kwargs)
        self.text = 'F'

class String2Fret13(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret13, self).__init__(**kwargs)
        self.text = 'A#'

class String3Fret13(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret13, self).__init__(**kwargs)
        self.text = 'D#'

class String4Fret13(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret13, self).__init__(**kwargs)
        self.text = 'G#'

class String5Fret13(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret13, self).__init__(**kwargs)
        self.text = 'C'

class String6Fret13(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret13, self).__init__(**kwargs)
        self.text = 'F'

class String1Fret14(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret14, self).__init__(**kwargs)
        self.text = 'F#'

class String2Fret14(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret14, self).__init__(**kwargs)
        self.text = 'B'

class String3Fret14(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret14, self).__init__(**kwargs)
        self.text = 'E'

class String4Fret14(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret14, self).__init__(**kwargs)
        self.text = 'A'

class String5Fret14(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret14, self).__init__(**kwargs)
        self.text = 'C#'

class String6Fret14(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret14, self).__init__(**kwargs)
        self.text = 'F#'

class String1Fret15(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret15, self).__init__(**kwargs)
        self.text = 'G'

class String2Fret15(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret15, self).__init__(**kwargs)
        self.text = 'C'

class String3Fret15(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret15, self).__init__(**kwargs)
        self.text = 'F'

class String4Fret15(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret15, self).__init__(**kwargs)
        self.text = 'A#'

class String5Fret15(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret15, self).__init__(**kwargs)
        self.text = 'D'

class String6Fret15(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret15, self).__init__(**kwargs)
        self.text = 'G'

class String1Fret16(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret16, self).__init__(**kwargs)
        self.text = 'G#'

class String2Fret16(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret16, self).__init__(**kwargs)
        self.text = 'C#'

class String3Fret16(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret16, self).__init__(**kwargs)
        self.text = 'F#'

class String4Fret16(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret16, self).__init__(**kwargs)
        self.text = 'B'

class String5Fret16(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret16, self).__init__(**kwargs)
        self.text = 'D#'

class String6Fret16(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret16, self).__init__(**kwargs)
        self.text = 'G#'

class String1Fret17(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret17, self).__init__(**kwargs)
        self.text = 'A'

class String2Fret17(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret17, self).__init__(**kwargs)
        self.text = 'D'

class String3Fret17(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret17, self).__init__(**kwargs)
        self.text = 'G'

class String4Fret17(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret17, self).__init__(**kwargs)
        self.text = 'C'

class String5Fret17(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret17, self).__init__(**kwargs)
        self.text = 'E'


class String6Fret17(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret17, self).__init__(**kwargs)
        self.text = 'A'

class String1Fret18(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret18, self).__init__(**kwargs)
        self.text = 'A#'

class String2Fret18(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret18, self).__init__(**kwargs)
        self.text = 'D#'

class String3Fret18(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret18, self).__init__(**kwargs)
        self.text = 'G#'

class String4Fret18(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret18, self).__init__(**kwargs)
        self.text = 'C#'

class String5Fret18(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret18, self).__init__(**kwargs)
        self.text = 'F'

class String6Fret18(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret18, self).__init__(**kwargs)
        self.text = 'A#'

class String1Fret19(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret19, self).__init__(**kwargs)
        self.text = 'B'

class String2Fret19(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret19, self).__init__(**kwargs)
        self.text = 'E'

class String3Fret19(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret19, self).__init__(**kwargs)
        self.text = 'A'

class String4Fret19(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret19, self).__init__(**kwargs)
        self.text = 'D'

class String5Fret19(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret19, self).__init__(**kwargs)
        self.text = 'F#'

class String6Fret19(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret19, self).__init__(**kwargs)
        self.text = 'B'

class String1Fret20(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret20, self).__init__(**kwargs)
        self.text = 'C'

class String2Fret20(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret20, self).__init__(**kwargs)
        self.text = 'F'

class String3Fret20(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret20, self).__init__(**kwargs)
        self.text = 'A#'

class String4Fret20(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret20, self).__init__(**kwargs)
        self.text = 'D#'

class String5Fret20(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret20, self).__init__(**kwargs)
        self.text = 'G'


class String6Fret20(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret20, self).__init__(**kwargs)
        self.text = 'C'

class String1Fret21(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret21, self).__init__(**kwargs)
        self.text = 'C#'

class String2Fret21(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret21, self).__init__(**kwargs)
        self.text = 'F#'

class String3Fret21(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret21, self).__init__(**kwargs)
        self.text = 'B'

class String4Fret21(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret21, self).__init__(**kwargs)
        self.text = 'E'

class String5Fret21(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret21, self).__init__(**kwargs)
        self.text = 'G#'

class String6Fret21(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret21, self).__init__(**kwargs)
        self.text = 'C#'

class String1Fret22(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret22, self).__init__(**kwargs)
        self.text = 'D'

class String2Fret22(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret22, self).__init__(**kwargs)
        self.text = 'G'

class String3Fret22(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret22, self).__init__(**kwargs)
        self.text = 'C'

class String4Fret22(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret22, self).__init__(**kwargs)
        self.text = 'F'

class String5Fret22(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret22, self).__init__(**kwargs)
        self.text = 'A'

class String6Fret22(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret22, self).__init__(**kwargs)
        self.text = 'D'

class String1Fret23(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret23, self).__init__(**kwargs)
        self.text = 'D#'

class String2Fret23(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret23, self).__init__(**kwargs)
        self.text = 'G#'

class String3Fret23(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret23, self).__init__(**kwargs)
        self.text = 'C#'

class String4Fret23(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret23, self).__init__(**kwargs)
        self.text = 'F#'

class String5Fret23(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret23, self).__init__(**kwargs)
        self.text = 'A#'

class String6Fret23(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret23, self).__init__(**kwargs)
        self.text = 'D#'

class String1Fret24(Button, Fret):
    def __init__(self, **kwargs):
        super(String1Fret24, self).__init__(**kwargs)
        self.text = 'E'

class String2Fret24(Button, Fret):
    def __init__(self, **kwargs):
        super(String2Fret24, self).__init__(**kwargs)
        self.text = 'A'

class String3Fret24(Button, Fret):
    def __init__(self, **kwargs):
        super(String3Fret24, self).__init__(**kwargs)
        self.text = 'D'

class String4Fret24(Button, Fret):
    def __init__(self, **kwargs):
        super(String4Fret24, self).__init__(**kwargs)
        self.text = 'G'

class String5Fret24(Button, Fret):
    def __init__(self, **kwargs):
        super(String5Fret24, self).__init__(**kwargs)
        self.text = 'B'

class String6Fret24(Button, Fret):
    def __init__(self, **kwargs):
        super(String6Fret24, self).__init__(**kwargs)
        self.text = 'E'

class Fret0Label(Button, Fret):
    pass

class Fret1Label(Widget):
    pass

class Fret2Label(Widget):
    pass

class Fret3Label(Widget):
    pass

class Fret4Label(Widget):
    pass

class Fret5Label(Widget):
    pass

class Fret6Label(Widget):
    pass

class Fret7Label(Widget):
    pass

class Fret8Label(Widget):
    pass

class Fret9Label(Widget):
    pass

class Fret10Label(Widget):
    pass

class Fret11Label(Widget):
    pass

class Fret12Label(Widget):
    pass

class Fret13Label(Widget):
    pass

class Fret14Label(Widget):
    pass

class Fret15Label(Widget):
    pass

class Fret16Label(Widget):
    pass

class Fret17Label(Widget):
    pass

class Fret18Label(Widget):
    pass

class Fret19Label(Widget):
    pass

class Fret20Label(Widget):
    pass

class Fret21Label(Widget):
    pass

class Fret22Label(Widget):
    pass

class Fret23Label(Widget):
    pass

class Fret24Label(Widget):
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
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())
        neck.add_widget(empty())

        neck.add_widget(String6Fret0())
        neck.add_widget(String6Fret1())
        neck.add_widget(String6Fret2())
        neck.add_widget(String6Fret3())
        neck.add_widget(String6Fret4())
        neck.add_widget(String6Fret5())
        neck.add_widget(String6Fret6())
        neck.add_widget(String6Fret7())
        neck.add_widget(String6Fret8())
        neck.add_widget(String6Fret9())
        neck.add_widget(String6Fret10())
        neck.add_widget(String6Fret11())
        neck.add_widget(String6Fret12())
        neck.add_widget(String6Fret13())
        neck.add_widget(String6Fret14())
        neck.add_widget(String6Fret15())
        neck.add_widget(String6Fret16())
        neck.add_widget(String6Fret17())
        neck.add_widget(String6Fret18())
        neck.add_widget(String6Fret19())
        neck.add_widget(String6Fret20())
        neck.add_widget(String6Fret21())
        neck.add_widget(String6Fret22())
        neck.add_widget(String6Fret23())
        neck.add_widget(String6Fret24())

        neck.add_widget(String5Fret0())
        neck.add_widget(String5Fret1())
        neck.add_widget(String5Fret2())
        neck.add_widget(String5Fret3())
        neck.add_widget(String5Fret4())
        neck.add_widget(String5Fret5())
        neck.add_widget(String5Fret6())
        neck.add_widget(String5Fret7())
        neck.add_widget(String5Fret8())
        neck.add_widget(String5Fret9())
        neck.add_widget(String5Fret10())
        neck.add_widget(String5Fret11())
        neck.add_widget(String5Fret12())
        neck.add_widget(String5Fret13())
        neck.add_widget(String5Fret14())
        neck.add_widget(String5Fret15())
        neck.add_widget(String5Fret6())
        neck.add_widget(String5Fret17())
        neck.add_widget(String5Fret18())
        neck.add_widget(String5Fret19())
        neck.add_widget(String5Fret20())
        neck.add_widget(String5Fret21())
        neck.add_widget(String5Fret22())
        neck.add_widget(String5Fret23())
        neck.add_widget(String5Fret24())

        neck.add_widget(String4Fret0())
        neck.add_widget(String4Fret1())
        neck.add_widget(String4Fret2())
        neck.add_widget(String4Fret3())
        neck.add_widget(String4Fret4())
        neck.add_widget(String4Fret5())
        neck.add_widget(String4Fret6())
        neck.add_widget(String4Fret7())
        neck.add_widget(String4Fret8())
        neck.add_widget(String4Fret9())
        neck.add_widget(String4Fret10())
        neck.add_widget(String4Fret11())
        neck.add_widget(String4Fret12())
        neck.add_widget(String4Fret13())
        neck.add_widget(String4Fret14())
        neck.add_widget(String4Fret15())
        neck.add_widget(String4Fret16())
        neck.add_widget(String4Fret17())
        neck.add_widget(String4Fret18())
        neck.add_widget(String4Fret19())
        neck.add_widget(String4Fret20())
        neck.add_widget(String4Fret21())
        neck.add_widget(String4Fret22())
        neck.add_widget(String4Fret23())
        neck.add_widget(String4Fret24())

        neck.add_widget(String3Fret0())
        neck.add_widget(String3Fret1())
        neck.add_widget(String3Fret2())
        neck.add_widget(String3Fret3())
        neck.add_widget(String3Fret4())
        neck.add_widget(String3Fret5())
        neck.add_widget(String3Fret6())
        neck.add_widget(String3Fret7())
        neck.add_widget(String3Fret8())
        neck.add_widget(String3Fret9())
        neck.add_widget(String3Fret10())
        neck.add_widget(String3Fret11())
        neck.add_widget(String3Fret12())
        neck.add_widget(String3Fret13())
        neck.add_widget(String3Fret14())
        neck.add_widget(String3Fret15())
        neck.add_widget(String3Fret16())
        neck.add_widget(String3Fret17())
        neck.add_widget(String3Fret18())
        neck.add_widget(String3Fret19())
        neck.add_widget(String3Fret20())
        neck.add_widget(String3Fret21())
        neck.add_widget(String3Fret22())
        neck.add_widget(String3Fret23())
        neck.add_widget(String3Fret24())

        neck.add_widget(String2Fret0())
        neck.add_widget(String2Fret1())
        neck.add_widget(String2Fret2())
        neck.add_widget(String2Fret3())
        neck.add_widget(String2Fret4())
        neck.add_widget(String2Fret5())
        neck.add_widget(String2Fret6())
        neck.add_widget(String2Fret7())
        neck.add_widget(String2Fret8())
        neck.add_widget(String2Fret9())
        neck.add_widget(String2Fret10())
        neck.add_widget(String2Fret11())
        neck.add_widget(String2Fret12())
        neck.add_widget(String2Fret13())
        neck.add_widget(String2Fret14())
        neck.add_widget(String2Fret15())
        neck.add_widget(String2Fret16())
        neck.add_widget(String2Fret17())
        neck.add_widget(String2Fret18())
        neck.add_widget(String2Fret19())
        neck.add_widget(String2Fret20())
        neck.add_widget(String2Fret21())
        neck.add_widget(String2Fret22())
        neck.add_widget(String2Fret23())
        neck.add_widget(String2Fret24())

        neck.add_widget(String1Fret0())
        neck.add_widget(String1Fret1())
        neck.add_widget(String1Fret2())
        neck.add_widget(String1Fret3())
        neck.add_widget(String1Fret4())
        neck.add_widget(String1Fret5())
        neck.add_widget(String1Fret6())
        neck.add_widget(String1Fret7())
        neck.add_widget(String1Fret8())
        neck.add_widget(String1Fret9())
        neck.add_widget(String1Fret10())
        neck.add_widget(String1Fret11())
        neck.add_widget(String1Fret12())
        neck.add_widget(String1Fret13())
        neck.add_widget(String1Fret14())
        neck.add_widget(String1Fret15())
        neck.add_widget(String1Fret16())
        neck.add_widget(String1Fret17())
        neck.add_widget(String1Fret18())
        neck.add_widget(String1Fret19())
        neck.add_widget(String1Fret20())
        neck.add_widget(String1Fret21())
        neck.add_widget(String1Fret22())
        neck.add_widget(String1Fret23())
        neck.add_widget(String1Fret24())

        neck.add_widget(Label(text="0"))
        neck.add_widget(Label(text="1"))
        neck.add_widget(Label(text="2"))
        neck.add_widget(Label(text="3"))
        neck.add_widget(Label(text="4"))
        neck.add_widget(Label(text="5"))
        neck.add_widget(Label(text="6"))
        neck.add_widget(Label(text="7"))
        neck.add_widget(Label(text="8"))
        neck.add_widget(Label(text="9"))
        neck.add_widget(Label(text="10"))
        neck.add_widget(Label(text="11"))
        neck.add_widget(Label(text="12"))
        neck.add_widget(Label(text="13"))
        neck.add_widget(Label(text="14"))
        neck.add_widget(Label(text="15"))
        neck.add_widget(Label(text="16"))
        neck.add_widget(Label(text="17"))
        neck.add_widget(Label(text="18"))
        neck.add_widget(Label(text="19"))
        neck.add_widget(Label(text="20"))
        neck.add_widget(Label(text="21"))
        neck.add_widget(Label(text="22"))
        neck.add_widget(Label(text="23"))
        neck.add_widget(Label(text="24"))
        neckScreen.add_widget(neck)
        return neckScreen


if __name__ == '__main__':
    GuitarApp().run()