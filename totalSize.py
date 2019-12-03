import os

totalSize = 0
for filename in os.listdir('c:\\users\\piotr\\desktop'):
    totalSize += os.path.getsize(os.path.join('c:\\users\\piotr\\desktop',filename))
print(totalSize)
