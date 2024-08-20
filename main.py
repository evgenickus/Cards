from kivy.config import Config
Config.set('graphics', 'width', 450)
Config.set('graphics', 'height', 750)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, ObjectProperty
from random import randint
import crud


class MainWidget(Widget):
  # rev_ls = card_letter_list[::-1]
  card_letter_list = ['Ц', 'Х', 'Ф', 'У', 'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л', 'К', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А']
  words_list = ["АНАНАС", "АРБУЗ", "АКВАЛАНГ", "АРГОН", "БРАГА", "БОБЁР", "БИВАК", "БЕГУН", "ВРАТА", "ВОБЛА", "ВОВА", "ВАГИНА", "ГРАВИЦАПА"]

  letter_a = StringProperty(card_letter_list[21])
  letter_b = StringProperty(card_letter_list[21])
  word = StringProperty('')
  clear_card = False
  num_a = ObjectProperty(21)
  num_b = ObjectProperty(21)
  bar_value = ObjectProperty(0)
  menu_open = StringProperty("ОТКРЫТЬ")
  menu_traning = StringProperty("ТРЕНИРОВКА")
  picture_link = StringProperty("")
  traning_on = False
  count = 0
  letter_num_a = 21
  letter_num_b = 21


  def __init__(self, **kwargs):
    super(MainWidget, self).__init__(**kwargs)
    self.remove_widget(self.ids.level)
    self.remove_widget(self.ids.picture)

  def slide_A(self, value):
    self.letter_a = self.card_letter_list[int(value)]

  def slide_B(self, value):
    self.letter_b = self.card_letter_list[int(value)]


  def find_word(self):
    tempory_word_list = []
    for word in self.words_list:
      if self.letter_a == word[0]:
        tempory_word_list.append(word)
    for word in tempory_word_list:
      if self.letter_b == word[2]:
        self.word = word
        self.picture_link = f"images/{str(self.words_list.index(word)+1)}.jpg"
        
  def open_card(self):
    if self.menu_open == "ОТКРЫТЬ":
      self.menu_open = "ЗАКРЫТЬ"
      self.remove_widget(self.ids.lab1)
      self.remove_widget(self.ids.lab2)
      if self.traning_on:
        self.add_widget(self.ids.level)
      self.find_word()
      self.add_widget(self.ids.picture)
    else:
      self.menu_open = "ОТКРЫТЬ"
      self.word = ""
      self.picture_link = ""
      self.remove_widget(self.ids.picture)
      self.add_widget(self.ids.lab1)
      self.add_widget(self.ids.lab2)
      if self.traning_on:
        self.remove_widget(self.ids.level)
      

  # def start_traning(self):
  #   self.traning_on = True
  #   random_num_a = randint(0, 21)
  #   random_num_b = randint(0, 21)
  #   self.letter_a = self.card_letter_list[random_num_a]
  #   self.letter_b = self.card_letter_list[random_num_b]
  #   self.num_a = random_num_a
  #   self.num_b = random_num_b
  #   self.remove_widget(self.ids.sld_1)
  #   self.remove_widget(self.ids.sld_2)
  #   if self.count < 10:
  #     self.count += 1
  #     self.bar_value += 1
  #   else:
  #     self.count = 0
  #     self.bar_value = 0
  #   self.menu_traning = f" {self.count} / 10"
  #   if self.menu_open == "ЗАКРЫТЬ":
  #     self.word = ""
  #     self.picture_link = ""
  #     self.add_widget(self.ids.lab1)
  #     self.add_widget(self.ids.lab2)
  #     self.remove_widget(self.ids.level)
  #     self.remove_widget(self.ids.picture)
  #     self.menu_open = "ОТКРЫТЬ"


  def count_index_a_b(self):
    if self.letter_num_b > 0:
      self.letter_num_b -= 1
    else:
      self.letter_num_b = 21
      self.letter_num_a -= 1
    if self.letter_a == 0:
      self.letter_a = 21
  
  def counter(self):
    if self.count < 21:
      self.count += 1
      self.bar_value += 1
    else:
      self.count = 0
      self.bar_value = 0
    self.menu_traning = f" {self.count} / 22"


  def start_traning(self):
    self.traning_on = True
    self.letter_a = self.card_letter_list[self.letter_num_a]
    self.letter_b = self.card_letter_list[self.letter_num_b]
    self.count_index_a_b()
    self.counter()
    self.remove_widget(self.ids.sld_1)
    self.remove_widget(self.ids.sld_2)
    if self.menu_open == "ЗАКРЫТЬ":
      self.word = ""
      self.picture_link = ""
      self.add_widget(self.ids.lab1)
      self.add_widget(self.ids.lab2)
      self.remove_widget(self.ids.level)
      self.remove_widget(self.ids.picture)
      self.menu_open = "ОТКРЫТЬ"
    res = crud.get_words()
    print(res)
    
  
  def rating_word(self, lelel):
    crud.add_task(self.word, lelel)
    self.remove_widget(self.ids.level)

  

  # def reset(self):
  #   if self.traning_on and self.menu_open == "ЗАКРЫТЬ":
  #     self.menu_open = "ОТКРЫТЬ"
  #     self.word = ""
  #     self.picture_link = ""
  #     self.add_widget(self.ids.lab1)
  #     self.add_widget(self.ids.lab2)
  #   if self.traning_on:
  #     self.add_widget(self.ids.sld_1)
  #     self.add_widget(self.ids.sld_2)

  #   self.bar_value = 0
  #   self.traning_on = False
  #   self.menu_traning = "ТРЕНИРОВКА"
  #   self.count = 0
  #   self.remove_widget(self.ids.level)
  #   self.remove_widget(self.ids.picture)
  def reset(self):
    self.letter_num_a = 21
    self.letter_num_b = 21
    self.letter_a = self.card_letter_list[self.letter_num_a]
    self.letter_b = self.card_letter_list[self.letter_num_b]

    if self.traning_on and self.menu_open == "ЗАКРЫТЬ":
      self.menu_open = "ОТКРЫТЬ"
      self.word = ""
      self.picture_link = ""
      self.add_widget(self.ids.lab1)
      self.add_widget(self.ids.lab2)
    if self.traning_on:
      self.add_widget(self.ids.sld_1)
      self.add_widget(self.ids.sld_2)

    self.bar_value = 0
    self.traning_on = False
    self.menu_traning = "ТРЕНИРОВКА"
    self.count = 0
    self.remove_widget(self.ids.level)
    self.remove_widget(self.ids.picture)



class CardsApp(App):
  def build(self):
    return MainWidget()


if __name__ == "__main__":
  CardsApp().run()
