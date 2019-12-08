def timeConversion(s):
    if s[:2] == '12' and s[-2:] == 'AM':
        return '00' + s[2:8]
    if s[:2] == '12' and s[-2:] == 'PM':
        return '12' + s[2:8]

    if s[-2:] == 'PM':
        if s[0] == '0':
            p = int(s[1]) + 12
            return str(p) + s[2:8]
        if s[0] == '1':
            p = int(s[:2]) + 12
            return str(p) + s[2:8]

    if s[-2:] == 'AM':
        return s[:8]

s = '12:40:22AM'

print(timeConversion(s))
