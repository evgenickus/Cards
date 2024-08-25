from kivy.app import App
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class Menu(Screen):
  pass

class MainWidget(Screen):
  card_letter_list = ['Ц', 'Х', 'Ф', 'У', 'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л', 'К', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А']
  words_list = ["АНАНАС", "АРБУЗ", "АКВАЛАНГ", "АРГОН", "БРАГА", "БОБЁР", "БИВАК", "БЕГУН", "ВРАТА", "ВОБЛА", "ВОВА", "ВАГИНА", "ГРАВИЦАПА"]

  letter_num_a = 21
  letter_num_b = 21
  letter_a = StringProperty(card_letter_list[letter_num_a])
  letter_b = StringProperty(card_letter_list[letter_num_b])
  word = StringProperty('')
  picture_link = StringProperty("")


  def __init__(self, **kwargs):
    super(MainWidget, self).__init__(**kwargs)
    self.ids.main_widget.remove_widget(self.ids.box_level)

  def rating_word(self, rating):
    self.reset()
    print(rating)

  def find_word(self):
    tempory_word_list = []
    for word in self.words_list:
      if self.letter_a == word[0]:
        tempory_word_list.append(word)
    for word in tempory_word_list:
      if self.letter_b == word[2]:
        self.word = f"[color=0000ff][u]{word[0]}[/u][/color]{word[1].lower()}[color=00ff00][u]{word[2]}[/u][/color]{word[3:].lower()}"
        self.picture_link = f"../images/{str(self.words_list.index(word)+1)}.jpg"
    

  def reset(self):
    self.ids.main_widget.add_widget(self.ids.lab1)
    self.ids.main_widget.add_widget(self.ids.lab2)
    self.ids.main_widget.add_widget(self.ids.but_open)
    self.ids.main_widget.remove_widget(self.ids.box_level)
    self.word = ""
    self.picture_link = ""

  def count_index_a_b(self):
    if self.letter_num_b > 0:
      self.letter_num_b -= 1
    else:
      self.letter_num_b = 21
      self.letter_num_a -= 1
    if self.letter_a == 0:
      self.letter_a = 21

  def open_card(self):
    self.ids.main_widget.remove_widget(self.ids.lab1)
    self.ids.main_widget.remove_widget(self.ids.lab2)
    self.ids.main_widget.remove_widget(self.ids.but_open)
    self.ids.main_widget.add_widget(self.ids.box_level)
    self.find_word()
    self.count_index_a_b()
    self.letter_a = self.card_letter_list[self.letter_num_a]
    self.letter_b = self.card_letter_list[self.letter_num_b]

  



class Cards1(App):
  main_color = ColorProperty([255/255, 122/255, 0, 1])
  def build(self):
    sm = ScreenManager(transition=FadeTransition())
    sm.add_widget(Menu(name="menu"))
    sm.add_widget(MainWidget(name="main"))

    return sm

Cards1().run()