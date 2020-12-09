screenNames = open("100screen_names.txt", "r")

names = []

for screenName in screenNames:
    justScreenName = screenName.replace('\n', '')
    names.append(justScreenName)
screenNames.close()
print(names)
