import pyperclip, itertools

#1. copy  specific format of country and capitals to clipboard
#2. create string of c&c and replace all blanks with one blank
capitalsAndCities = ' '.join(pyperclip.paste().split())
#3. replace newlines with one blank
finalString = capitalsAndCities.replace('\n',' ')
#4. split all words in string to substring and create list
listOfCapitalsAndCities = finalString.split()
#5. convert list to a dictionary
dictionaryOfCapitalsAndCities = dict(itertools.zip_longest(*[iter(listOfCapitalsAndCities)] * 2, fillvalue=""))
stringForClipboard= str(dictionaryOfCapitalsAndCities)
pyperclip.copy(stringForClipboard)
