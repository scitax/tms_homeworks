phrase = input('Enter phrase ')

phrase_len = len(phrase)

if phrase_len < 1:
    pass
elif phrase_len < 9:
    print(phrase[:2])

elif  phrase_len >= 10:
    new_phrase = phrase + '!!!'
    print(new_phrase)
