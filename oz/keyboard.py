keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'

a = input()
s = input()

a = 1 if a == 'L' else -1 if a == 'R' else 0

s_ = []

for el in s:
    ind = keyboard.index(el)
    if (ind % 10 == 0 and a == -1) or (ind % 10 == 9 and a == 1):
        s_.append(el)
    else:
        s_.append(keyboard[ind + a])

print(''.join(s_))

