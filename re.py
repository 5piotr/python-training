import re

text = 'ksdv vefer 2 asdv 23 vsdfv43vf 66 vf77'

aRegex = re.compile(r'\d\d')
mo = aRegex.search(text)
mo2 = aRegex.findall(text)

print(mo.group())
print(mo)
print(mo2)
