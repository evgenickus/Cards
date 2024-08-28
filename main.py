from kivy.app import App
from kivy.properties import ColorProperty, StringProperty, ObjectProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import crud


class Menu(Screen):
  pass

class New(Screen):
  pass

class MainWidget(Screen):
  card_letter_list = ['Ч', 'Х', 'Ф', 'У', 'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л', 'К', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А']

  words_list = ['АНАНАС', 'АРБУЗ', 'АКВАРИУМ', 'АНГЕЛ', 'АНДРОИД', 'АПЕЛЬСИН', 'АДЖИКА', 'АБЗАЦ', 'АДИДАС', 'АРКА', 'АЛЛЕЯ', 'АЛМАЗ', 'АРНОЛЬД', 'АЛОЭ', 'АМПЛИТУДА', 'АБРИКОС', 'АИСТ', 'АПТЕКА', 'АКУЛА', 'АЛФАВИТ', 'АРХЫЗ', 'АНЧОУС', 'БИАТЛОН', 'БАБУШКА', 'БИВЕНЬ', 'БЕГЕМОТ', 'БАДМИНТОН', 'БРЕЛОК', 'БИЖУТЕРИЯ', 'БИЗОН', 'БРИТВА', 'БУКВАРЬ', 'БИЛЕТ', 'БУМЕРАНГ', 'БАНАН', 'БРОВИ', 'БИП', 'БОРОДА', 'БАССЕЙН', 'БАТОН', 'БОУЛИНГ', 'БИФШТЕКС', 'БАХИЛЫ', 'БОЧКА']

  letter_num_a = 21
  letter_num_b = 21
  letter_a = StringProperty(card_letter_list[letter_num_a])
  letter_b = StringProperty(card_letter_list[letter_num_b])
  underline_cards_counter = ObjectProperty(False)
  underline_new_cards_counter = ObjectProperty(False)
  underline_repeat_cards_counter = ObjectProperty(False)

  word = StringProperty("")
  word_db = str()
  word_len = 0
  cards_counter = StringProperty("11")
  new_cards_counter = StringProperty("0")
  repeat_cards_counter = StringProperty("0")

  picture_link = StringProperty("")


  def __init__(self, **kwargs):
    super(MainWidget, self).__init__(**kwargs)
    self.statistic()
    self.ids.main_widget.remove_widget(self.ids.box_level)
    self.ids.box_letter.remove_widget(self.ids.lab3)
    self.ids.box_letter.remove_widget(self.ids.picture)


  def rating_word(self, rating):
    crud.add_task(self.word_db, rating)
    self.reset()


  def find_word(self):
    tempory_word_list = []
    for word in self.words_list:
      if self.letter_a == word[0]:
        tempory_word_list.append(word)
    for word in tempory_word_list:
      if self.letter_b == word[2]:
        self.word_len = len(word)
        self.word_db = word
        self.word = f"[color=008eff][u]{word[0]}[/u][/color]{word[1].lower()}[color=008eff][u]{word[2]}[/u][/color]{word[3:].lower()}"
        self.picture_link = f"images/{str(self.words_list.index(word)+1)}.jpg"


  def reset(self):
    self.ids.box_letter.orientation = "horizontal"
    self.ids.box_letter.add_widget(self.ids.lab1)
    self.ids.box_letter.add_widget(self.ids.lab2)
    self.ids.box_letter.remove_widget(self.ids.lab3)
    self.ids.box_letter.remove_widget(self.ids.picture)
    self.ids.main_widget.add_widget(self.ids.but_open)
    self.ids.main_widget.remove_widget(self.ids.box_level)
    self.word = ""
    self.picture_link = ""

  def count_cards_counter(self):
    count = int(self.cards_counter) - 1
    self.cards_counter = str(count)
    self.underline_cards_counter = True

  def count_index_a_b(self):
    if self.letter_num_b > 0:
      self.letter_num_b -= 1
    else:
      self.letter_num_b = 21
      self.letter_num_a -= 1
    if self.letter_a == 0:
      self.letter_a = 21

  def statistic(self):
    old_words = crud.get_words()
    self.repeat_cards_counter = str(len(old_words))
    print(old_words)

  def open_card(self):
    self.ids.box_letter.orientation = "vertical"
    self.ids.box_letter.remove_widget(self.ids.lab1)
    self.ids.box_letter.remove_widget(self.ids.lab2)
    self.ids.box_letter.add_widget(self.ids.lab3)
    self.ids.box_letter.add_widget(self.ids.picture)
    self.ids.main_widget.remove_widget(self.ids.but_open)
    self.ids.main_widget.add_widget(self.ids.box_level)
    self.find_word()
    self.count_index_a_b()
    self.count_cards_counter()
    self.letter_a = self.card_letter_list[self.letter_num_a]
    self.letter_b = self.card_letter_list[self.letter_num_b]

  



class Cards(App):
  main_color = ColorProperty([255/255, 122/255, 0, 1])
  def build(self):
    sm = ScreenManager(transition=FadeTransition())
    sm.add_widget(Menu(name="menu"))
    sm.add_widget(MainWidget(name="main"))
    sm.add_widget(New(name="new"))


    return sm

Cards().run()