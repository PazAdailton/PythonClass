"""
Four most important components

"." == anything like letters, numbers, symbols... but not newlines... OBS: Only characters

"+" == one or more of

"*" == zero or more of... OBS get all word

"?" == zero or one of

 "\" literal of symbol

"""

import re


name = 'charlie'
email = 'jose@tecladocode.com'

regexer = '[a-z]'

match = re.findall(regexer, name)
print(match)