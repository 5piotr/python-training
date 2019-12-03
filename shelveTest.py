import shelve

shelfFile = shelve.open('mydata')
cats = ['mruczek','kropka','tajger']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
