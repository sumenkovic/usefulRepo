#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()

print(text)
lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
print(lines)
text = '\n'.join(lines)

pyperclip.copy(text)
