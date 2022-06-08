from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from screens.Info import Info as Info
from screens.MainScreen import SetTuningScreen as SetTuningScreen


def create():
    info = Info()
    return info.setup_info()


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
        #self.icon =
        sm = ScreenManager()
        tune = SetTuningScreen()
        sm.add_widget(create())
        sm.remove_widget(tune)
        return sm


if __name__ == '__main__':
    FretNinjaApp().run()
