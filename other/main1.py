from kivy.app import App
from kivy.properties import ColorProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class Menu(Screen):
  pass

class MainWidget(Screen):
  pass

class Cards1(App):
  main_color = ColorProperty([255/255, 122/255, 0, 1])
  def build(self):
    sm = ScreenManager(transition=FadeTransition())
    sm.add_widget(Menu(name="menu"))
    sm.add_widget(MainWidget(name="main"))

    return sm

Cards1().run()