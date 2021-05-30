import kivy.graphics
from kivy.app import App
from kivy.graphics import Color, Rectangle, Canvas, Callback
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import fillNeck

class GuitarTheory(Widget):
    pass

class ColoredLabel(Label):
    background_color = ListProperty((1, 1, 1, 1))

class Fret:
    pass

class Fret0String1(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret0String1, self).__init__(**kwargs)
        self.text = 'E'

class Fret0String2(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret0String2, self).__init__(**kwargs)
        self.text = 'A'

class Fret0String3(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret0String3, self).__init__(**kwargs)
        self.text = 'D'

class Fret0String4(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret0String4, self).__init__(**kwargs)
        self.text = 'G'

class Fret0String5(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret0String5, self).__init__(**kwargs)
        self.text = 'B'

class Fret0String6(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret0String6, self).__init__(**kwargs)
        self.text = 'E'

class Fret1String1(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret1String1, self).__init__(**kwargs)
        self.text = 'F'

class Fret1String2(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret1String2, self).__init__(**kwargs)
        self.text = 'A#'

class Fret1String3(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret1String3, self).__init__(**kwargs)
        self.text = 'D#'

class Fret1String4(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret1String4, self).__init__(**kwargs)
        self.text = 'G#'

class Fret1String5(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret1String5, self).__init__(**kwargs)
        self.text = 'C'

class Fret1String6(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret1String6, self).__init__(**kwargs)
        self.text = 'F'

class Fret2String1(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret2String1, self).__init__(**kwargs)
        self.text = 'F#'

class Fret2String2(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret2String2, self).__init__(**kwargs)
        self.text = 'B'

class Fret2String3(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret2String3, self).__init__(**kwargs)
        self.text = 'E'

class Fret2String4(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret2String4, self).__init__(**kwargs)
        self.text = 'A'

class Fret2String5(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret2String5, self).__init__(**kwargs)
        self.text = 'C#'

class Fret2String6(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret2String6, self).__init__(**kwargs)
        self.text = 'F#'

class Fret3String1(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret3String1, self).__init__(**kwargs)
        self.text = 'G'

class Fret3String2(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret3String2, self).__init__(**kwargs)
        self.text = 'C'

class Fret3String3(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret3String3, self).__init__(**kwargs)
        self.text = 'F'

class Fret3String4(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret3String4, self).__init__(**kwargs)
        self.text = 'A#'

class Fret3String5(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret3String5, self).__init__(**kwargs)
        self.text = 'D'

class Fret3String6(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret3String6, self).__init__(**kwargs)
        self.text = 'G'

class Fret4String1(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret4String1, self).__init__(**kwargs)
        self.text = 'G#'

class Fret4String2(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret4String2, self).__init__(**kwargs)
        self.text = 'C#'

class Fret4String3(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret4String3, self).__init__(**kwargs)
        self.text = 'F#'

class Fret4String4(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret4String4, self).__init__(**kwargs)
        self.text = 'B'

class Fret4String5(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret4String5, self).__init__(**kwargs)
        self.text = 'D#'

class Fret4String6(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret4String6, self).__init__(**kwargs)
        self.text = 'G#'

class Fret5String1(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret5String1, self).__init__(**kwargs)
        self.text = 'A'

class Fret5String2(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret5String2, self).__init__(**kwargs)
        self.text = 'D'

class Fret5String3(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret5String3, self).__init__(**kwargs)
        self.text = 'G'
class Fret5String4(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret5String4, self).__init__(**kwargs)
        self.text = 'C'

class Fret5String5(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret5String5, self).__init__(**kwargs)
        self.text = 'E'

class Fret5String6(Button, Fret):
    def __init__(self, **kwargs):
        super(Fret5String6, self).__init__(**kwargs)
        self.text = 'A'

class Fret6String1(Button, Fret):
    pass

class Fret6String2(Button, Fret):
    pass

class Fret6String3(Button, Fret):
    pass

class Fret6String4(Button, Fret):
    pass

class Fret6String5(Button, Fret):
    pass

class Fret6String6(Button, Fret):
    pass

class Fret7String1(Button, Fret):
    pass

class Fret7String2(Button, Fret):
    pass

class Fret7String3(Button, Fret):
    pass

class Fret7String4(Button, Fret):
    pass

class Fret7String5(Button, Fret):
    pass

class Fret7String6(Button, Fret):
    pass

class Fret8String1(Button, Fret):
    pass

class Fret8String2(Button, Fret):
    pass

class Fret8String3(Button, Fret):
    pass

class Fret8String4(Button, Fret):
    pass

class Fret8String5(Button, Fret):
    pass

class Fret8String6(Button, Fret):
    pass

class Fret9String1(Button, Fret):
    pass

class Fret9String2(Button, Fret):
    pass

class Fret9String3(Button, Fret):
    pass

class Fret9String4(Button, Fret):
    pass

class Fret9String5(Button, Fret):
    pass

class Fret9String6(Button, Fret):
    pass

class Fret10String1(Button, Fret):
    pass

class Fret10String2(Button, Fret):
    pass

class Fret10String3(Button, Fret):
    pass

class Fret10String4(Button, Fret):
    pass

class Fret10String5(Button, Fret):
    pass

class Fret10String6(Button, Fret):
    pass

class Fret11String1(Button, Fret):
    pass

class Fret11String2(Button, Fret):
    pass

class Fret11String3(Button, Fret):
    pass

class Fret11String4(Button, Fret):
    pass

class Fret11String5(Button, Fret):
    pass

class Fret11String6(Button, Fret):
    pass

class Fret12String1(Button, Fret):
    pass

class Fret12String2(Button, Fret):
    pass

class Fret12String3(Button, Fret):
    pass

class Fret12String4(Button, Fret):
    pass

class Fret12String5(Button, Fret):
    pass

class Fret12String6(Button, Fret):
    pass

class Fret13String1(Button, Fret):
    pass

class Fret13String2(Button, Fret):
    pass

class Fret13String3(Button, Fret):
    pass

class Fret13String4(Button, Fret):
    pass

class Fret13String5(Button, Fret):
    pass

class Fret13String6(Button, Fret):
    pass

class Fret14String1(Button, Fret):
    pass

class Fret14String2(Button, Fret):
    pass

class Fret14String3(Button, Fret):
    pass

class Fret14String4(Button, Fret):
    pass

class Fret14String5(Button, Fret):
    pass

class Fret14String6(Button, Fret):
    pass

class Fret15String1(Button, Fret):
    pass

class Fret15String2(Button, Fret):
    pass

class Fret15String3(Button, Fret):
    pass

class Fret15String4(Button, Fret):
    pass

class Fret15String5(Button, Fret):
    pass

class Fret15String6(Button, Fret):
    pass

class Fret16String1(Button, Fret):
    pass

class Fret16String2(Button, Fret):
    pass

class Fret16String3(Button, Fret):
    pass

class Fret16String4(Button, Fret):
    pass

class Fret16String5(Button, Fret):
    pass

class Fret16String6(Button, Fret):
    pass

class Fret17String1(Button, Fret):
    pass

class Fret17String2(Button, Fret):
    pass

class Fret17String3(Button, Fret):
    pass

class Fret17String4(Button, Fret):
    pass

class Fret17String5(Button, Fret):
    pass

class Fret17String6(Button, Fret):
    pass

class Fret18String1(Button, Fret):
    pass

class Fret18String2(Button, Fret):
    pass

class Fret18String3(Button, Fret):
    pass

class Fret18String4(Button, Fret):
    pass

class Fret18String5(Button, Fret):
    pass

class Fret18String6(Button, Fret):
    pass

class Fret19String1(Button, Fret):
    pass

class Fret19String2(Button, Fret):
    pass

class Fret19String3(Button, Fret):
    pass

class Fret19String4(Button, Fret):
    pass

class Fret19String5(Button, Fret):
    pass

class Fret19String6(Button, Fret):
    pass

class Fret20String1(Button, Fret):
    pass

class Fret20String2(Button, Fret):
    pass

class Fret20String3(Button, Fret):
    pass

class Fret20String4(Button, Fret):
    pass

class Fret20String5(Button, Fret):
    pass

class Fret20String6(Button, Fret):
    pass

class Fret21String1(Button, Fret):
    pass

class Fret21String2(Button, Fret):
    pass

class Fret21String3(Button, Fret):
    pass

class Fret21String4(Button, Fret):
    pass

class Fret21String5(Button, Fret):
    pass

class Fret21String6(Button, Fret):
    pass

class Fret22String1(Button, Fret):
    pass

class Fret22String2(Button, Fret):
    pass

class Fret22String3(Button, Fret):
    pass

class Fret22String4(Button, Fret):
    pass

class Fret22String5(Button, Fret):
    pass

class Fret22String6(Button, Fret):
    pass

class Fret23String1(Button, Fret):
    pass

class Fret23String2(Button, Fret):
    pass

class Fret23String3(Button, Fret):
    pass

class Fret23String4(Button, Fret):
    pass

class Fret23String5(Button, Fret):
    pass

class Fret23String6(Button, Fret):
    pass

class Fret24String1(Button, Fret):
    pass

class Fret24String2(Button, Fret):
    pass

class Fret24String3(Button, Fret):
    pass

class Fret24String4(Button, Fret):
    pass

class Fret24String5(Button, Fret):
    pass

class Fret24String6(Button, Fret):
    pass

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



class Grid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 7
        self.cols = 25


class GuitarApp(App):
    def build(self):
        root = Grid()
        root.add_widget(Fret0String6())

        root.add_widget(Fret1String6(width=20))
        root.add_widget(Fret2String6(width=20))
        root.add_widget(Fret3String6(width=20))
        root.add_widget(Fret4String6(width=20))
        root.add_widget(Fret5String6())
        root.add_widget(Fret6String6())
        root.add_widget(Fret7String6())
        root.add_widget(Fret8String6())
        root.add_widget(Fret9String6())
        root.add_widget(Fret10String6())
        root.add_widget(Fret11String6())
        root.add_widget(Fret12String6())
        root.add_widget(Fret13String6())
        root.add_widget(Fret14String6())
        root.add_widget(Fret15String6())
        root.add_widget(Fret16String6())
        root.add_widget(Fret17String6())
        root.add_widget(Fret18String6())
        root.add_widget(Fret19String6())
        root.add_widget(Fret20String6())
        root.add_widget(Fret21String6())
        root.add_widget(Fret22String6())
        root.add_widget(Fret23String6())
        root.add_widget(Fret24String6())

        root.add_widget(Fret0String5())
        root.add_widget(Fret1String5())
        root.add_widget(Fret2String5())
        root.add_widget(Fret3String5())
        root.add_widget(Fret4String5())
        root.add_widget(Fret5String5())
        root.add_widget(Fret6String5())
        root.add_widget(Fret7String5())
        root.add_widget(Fret8String5())
        root.add_widget(Fret9String5())
        root.add_widget(Fret10String5())
        root.add_widget(Fret11String5())
        root.add_widget(Fret12String5())
        root.add_widget(Fret13String5())
        root.add_widget(Fret14String5())
        root.add_widget(Fret15String5())
        root.add_widget(Fret16String5())
        root.add_widget(Fret17String5())
        root.add_widget(Fret18String5())
        root.add_widget(Fret19String5())
        root.add_widget(Fret20String5())
        root.add_widget(Fret21String5())
        root.add_widget(Fret22String5())
        root.add_widget(Fret23String5())
        root.add_widget(Fret24String5())

        root.add_widget(Fret0String4())
        root.add_widget(Fret1String4())
        root.add_widget(Fret2String4())
        root.add_widget(Fret3String4())
        root.add_widget(Fret4String4())
        root.add_widget(Fret5String4())
        root.add_widget(Fret6String4())
        root.add_widget(Fret7String4())
        root.add_widget(Fret8String4())
        root.add_widget(Fret9String4())
        root.add_widget(Fret10String4())
        root.add_widget(Fret11String4())
        root.add_widget(Fret12String4())
        root.add_widget(Fret13String4())
        root.add_widget(Fret14String4())
        root.add_widget(Fret15String4())
        root.add_widget(Fret16String4())
        root.add_widget(Fret17String4())
        root.add_widget(Fret18String4())
        root.add_widget(Fret19String4())
        root.add_widget(Fret20String4())
        root.add_widget(Fret21String4())
        root.add_widget(Fret22String4())
        root.add_widget(Fret23String4())
        root.add_widget(Fret24String4())

        root.add_widget(Fret0String3())
        root.add_widget(Fret1String3())
        root.add_widget(Fret2String3())
        root.add_widget(Fret3String3())
        root.add_widget(Fret4String3())
        root.add_widget(Fret5String3())
        root.add_widget(Fret6String3())
        root.add_widget(Fret7String3())
        root.add_widget(Fret8String3())
        root.add_widget(Fret9String3())
        root.add_widget(Fret10String3())
        root.add_widget(Fret11String3())
        root.add_widget(Fret12String3())
        root.add_widget(Fret13String3())
        root.add_widget(Fret14String3())
        root.add_widget(Fret15String3())
        root.add_widget(Fret16String3())
        root.add_widget(Fret17String3())
        root.add_widget(Fret18String3())
        root.add_widget(Fret19String3())
        root.add_widget(Fret20String3())
        root.add_widget(Fret21String3())
        root.add_widget(Fret22String3())
        root.add_widget(Fret23String3())
        root.add_widget(Fret24String3())

        root.add_widget(Fret0String2())
        root.add_widget(Fret1String2())
        root.add_widget(Fret2String2())
        root.add_widget(Fret3String2())
        root.add_widget(Fret4String2())
        root.add_widget(Fret5String2())
        root.add_widget(Fret6String2())
        root.add_widget(Fret7String2())
        root.add_widget(Fret8String2())
        root.add_widget(Fret9String2())
        root.add_widget(Fret10String2())
        root.add_widget(Fret11String2())
        root.add_widget(Fret12String2())
        root.add_widget(Fret13String2())
        root.add_widget(Fret14String2())
        root.add_widget(Fret15String2())
        root.add_widget(Fret16String2())
        root.add_widget(Fret17String2())
        root.add_widget(Fret18String2())
        root.add_widget(Fret19String2())
        root.add_widget(Fret20String2())
        root.add_widget(Fret21String2())
        root.add_widget(Fret22String2())
        root.add_widget(Fret23String2())
        root.add_widget(Fret24String2())

        root.add_widget(Fret0String1())
        root.add_widget(Fret1String1())
        root.add_widget(Fret2String1())
        root.add_widget(Fret3String1())
        root.add_widget(Fret4String1())
        root.add_widget(Fret5String1())
        root.add_widget(Fret6String1())
        root.add_widget(Fret7String1())
        root.add_widget(Fret8String1())
        root.add_widget(Fret9String1())
        root.add_widget(Fret10String1())
        root.add_widget(Fret11String1())
        root.add_widget(Fret12String1())
        root.add_widget(Fret13String1())
        root.add_widget(Fret14String1())
        root.add_widget(Fret15String1())
        root.add_widget(Fret16String1())
        root.add_widget(Fret17String1())
        root.add_widget(Fret18String1())
        root.add_widget(Fret19String1())
        root.add_widget(Fret20String1())
        root.add_widget(Fret21String1())
        root.add_widget(Fret22String1())
        root.add_widget(Fret23String1())
        root.add_widget(Fret24String1())

        root.add_widget(Label(text="0"))
        root.add_widget(Label(text="1"))
        root.add_widget(Label(text="2"))
        root.add_widget(Label(text="3"))
        root.add_widget(Label(text="4"))
        root.add_widget(Label(text="5"))
        root.add_widget(Label(text="6"))
        root.add_widget(Label(text="7"))
        root.add_widget(Label(text="8"))
        root.add_widget(Label(text="9"))
        root.add_widget(Label(text="10"))
        root.add_widget(Label(text="11"))
        root.add_widget(Label(text="12"))
        root.add_widget(Label(text="13"))
        root.add_widget(Label(text="14"))
        root.add_widget(Label(text="15"))
        root.add_widget(Label(text="16"))
        root.add_widget(Label(text="17"))
        root.add_widget(Label(text="18"))
        root.add_widget(Label(text="19"))
        root.add_widget(Label(text="20"))
        root.add_widget(Label(text="21"))
        root.add_widget(Label(text="22"))
        root.add_widget(Label(text="23"))
        root.add_widget(Label(text="24"))
        return root


if __name__ == '__main__':
    GuitarApp().run()