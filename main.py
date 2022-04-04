#-*- coding: utf-8 -*-
#!/usr/bin/env python
language = input("Choose language/ Выберите язык  Ru or En:  ")
LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
LETTERS_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
key = 0
message = input("Сообщение для дешифровки: ")
n = 32
n_p = 9
punctuation_marks = '.,?!;/+*-'
if language == 'Ru':
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num -= key
                translated += LETTERS[num%n]
            elif symbol in LETTERS_lower:
                num = LETTERS_lower.find(symbol)
                num -= key
                translated += LETTERS_lower[num%n]
            elif symbol in punctuation_marks:
                num = punctuation_marks.find(symbol)
                translated += punctuation_marks[num]
            else:
                translated += ' '

        print(f"""Hacking key #{key}, translated:{translated} """)



