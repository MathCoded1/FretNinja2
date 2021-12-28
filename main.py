from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import NoteHelper
from InstrumentInfo import InstrumentInfo as InstrumentInfo

def create():
    info = InstrumentInfo()
    return info.setup_info()

class Empty(Widget):
    pass




class Menu(AnchorLayout):
    def __init__(self, instrument, screen, **kwargs):
        super().__init__(**kwargs)
        self.instrument = instrument
        self.screen = screen

    anchor_x = 'left'
    anchor_y = 'top'
    btn_retune = Button(text='retune')
    # btn_retune.bind(on_press=lambda instance:



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
