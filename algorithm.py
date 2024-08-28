all_words = 22* 22 #484
steps = 11
rounds = int(all_words / steps) #44

card_letter_list = ['Ч', 'Х', 'Ф', 'У', 'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л', 'К', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А']
words_list = ['АНАНАС', 'АРБУЗ', 'АКВАРИУМ', 'АНГЕЛ', 'АНДРОИД', 'АПЕЛЬСИН', 'АДЖИКА', 'АБЗАЦ', 'АДИДАС', 'АРКА', 'АЛЛЕЯ', 'АЛМАЗ', 'АРНОЛЬД', 'АЛОЭ', 'АМПЛИТУДА', 'АБРИКОС', 'АИСТ', 'АПТЕКА', 'АКУЛА', 'АЛФАВИТ', 'АРХЫЗ', 'АНЧОУС', 'БИАТЛОН', 'БАБУШКА', 'БИВЕНЬ', 'БЕГЕМОТ', 'БАДМИНТОН', 'БРЕЛОК', 'БИЖУТЕРИЯ', 'БИЗОН', 'БРИТВА', 'БУКВАРЬ', 'БИЛЕТ', 'БУМЕРАНГ', 'БАНАН', 'БРОВИ', 'БИП', 'БОРОДА', 'БАССЕЙН', 'БАТОН', 'БОУЛИНГ', 'БИФШТЕКС', 'БАХИЛЫ', 'БОЧКА']

def find_word(letter_num_a = 21, letter_num_b = 21):
  letter_a = card_letter_list[letter_num_a]
  letter_b = card_letter_list[letter_num_b]
  tempory_word_list = []
  for word in words_list:
    if letter_a == word[0]:
      tempory_word_list.append(word)
  for word in tempory_word_list:
    if letter_b == word[2]:
      return word

for round in range(rounds):
  print(round)
  # for step in range(steps):
  #   print(find_word(21, 21-steps))
  # for step in range(steps):
  #   print(find_word(21, 21-steps*2))