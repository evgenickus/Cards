from kivy.app import App
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class Menu(Screen):
  pass

class MainWidget(Screen):
  card_letter_list = ['Ц', 'Х', 'Ф', 'У', 'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л', 'К', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А']
  words_list = ["АНАНАС", "АРБУЗ", "АКВАЛАНГ", "АРГОН", "БРАГА", "БОБЁР", "БИВАК", "БЕГУН", "ВРАТА", "ВОБЛА", "ВОВА", "ВАГИНА", "ГРАВИЦАПА"]

  letter_a = StringProperty(card_letter_list[21])
  letter_b = StringProperty(card_letter_list[21])
  word = StringProperty('')
  picture_link = StringProperty("")


  def __init__(self, **kwargs):
    super(MainWidget, self).__init__(**kwargs)
    self.ids.main_widget.remove_widget(self.ids.picture)
    self.ids.main_widget.remove_widget(self.ids.level)

  def reset(self):
    self.ids.main_widget.remove_widget(self.ids.level)
    self.ids.main_widget.remove_widget(self.ids.picture)
    self.word = ""
    # self.ids.main_widget.add_widget(self.ids.lab1)
    # self.ids.main_widget.add_widget(self.ids.lab2)
    # self.ids.main_widget.add_widget(self.ids.but_open)



  def find_word(self):
    tempory_word_list = []
    for word in self.words_list:
      if self.letter_a == word[0]:
        tempory_word_list.append(word)
    for word in tempory_word_list:
      if self.letter_b == word[2]:
        self.word = word
        self.picture_link = f"../images/{str(self.words_list.index(word)+1)}.jpg"

  def open_card(self):
    self.ids.main_widget.remove_widget(self.ids.lab1)
    self.ids.main_widget.remove_widget(self.ids.lab2)
    self.ids.main_widget.remove_widget(self.ids.but_open)
    self.ids.main_widget.add_widget(self.ids.picture)
    self.ids.main_widget.add_widget(self.ids.level)

    # self.add_widget(self.ids.level)
    self.find_word()
    # else:
    #   self.menu_open = "ОТКРЫТЬ"
    #   self.word = ""
    #   self.picture_link = ""
    #   self.remove_widget(self.ids.picture)
    #   self.add_widget(self.ids.lab1)
    #   self.add_widget(self.ids.lab2)
    #   if self.traning_on:
    #     self.remove_widget(self.ids.level)


class Cards1(App):
  main_color = ColorProperty([255/255, 122/255, 0, 1])
  def build(self):
    sm = ScreenManager(transition=FadeTransition())
    sm.add_widget(Menu(name="menu"))
    sm.add_widget(MainWidget(name="main"))

    return sm

Cards1().run()