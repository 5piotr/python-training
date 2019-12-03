#! python3

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    print('0 '+groups[0])
    print('1 '+groups[1])
    print('2 '+groups[2])
    print('3 '+groups[3])
    print('4 '+groups[4])
    print('5 '+groups[5])
    print('6 '+groups[6])
    print('7 '+groups[7])
    print('8 '+groups[8])
    print('9 '+groups[9])

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka:')
    print('\n'.join(matches))
else:
    print('Nie znaleziono żadnego adresu email ani numeru telefonu')


