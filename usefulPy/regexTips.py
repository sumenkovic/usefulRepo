#find the number
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
if(mo != None):
    print('Phone number found: ' + mo.group())
    areaCode, mainNumber = mo.groups()
else:
    print('Theres no phone number pattern found!')

#regex matching multiple groups
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
#or findall()
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
#regex pattern Bat(man|mobile|women) for any of ocurrences

#The ? matches zero or one of the preceding group.
#The * matches zero or more of the preceding group.
#The + matches one or more of the preceding group.
#The {n} matches exactly n of the preceding group.
#The {n,} matches n or more of the preceding group.
#The {,m} matches 0 to m of the preceding group.
#The {n,m} matches at least n and at most m of the preceding group.
#{n,m}? or *? or +? performs a nongreedy match of the preceding group.
#^spam means the string must begin with spam.
#spam$ means the string must end with spam.
#The . matches any character, except newline characters.
#\d , \w , and \s match a digit, word, or space character, respectively.
#\D , \W , and \S match anything except a digit, word, or space character,
#respectively.
#[abc] matches any character between the brackets (such as a, b, or c).
#[^abc] matches any character that isn’t between the brackets.
#To make your regex case-insen-sitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile() .

#>>> namesRegex = re.compile(r'Agent \w+')
#>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#'CENSORED gave the secret documents to CENSORED.'
