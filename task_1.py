punctuation = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~0123456789'

def most_wanted_letter(text: str) -> str:
    for mark in text:
        if mark in punctuation:
            text = text.replace(mark, '')

    if text != '': 
        letters = [x for x in text.lower()]
        max_count, result = 0, 0
        for letter in set(letters):
            count = letters.count(letter)
            if count > max_count:
                max_count = count
                result = letter

        return f'The most popular letter is {result}'
    
    return 'There are no letters in string'
            

print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))
