import wikipedia as wiki
name=input('enter a name\n')
info=wiki.summary(name)
print(info)