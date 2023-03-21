import db

# Перевод одной буквы
def transl(ru):
    return db.translit[ru]

# Перевод всего слова
def translin_word(word_ru):
    word_trans = ''
    for i in word_ru:
        i = i.lower()
        if i == ' ':
            word_trans = word_trans + ' '
        if i in db.letter_list:
            word_trans = word_trans + transl(i)
        else:
            word_trans = word_trans + i
    return word_trans

# Перевод типа
def type(type):
    return db.type_list[type]

# Перевод всех слов в список
def trabslit_list(df):
    list_trans = {}
    for i in df.values.tolist():
        list_trans[translin_word(i[0])] = type(i[1])
    return list_trans
