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
name2 = 'Jo.se'
email = 'jose@tecladocode.me'
any_string = """
  charlie hello - I am Jose
              hi - there

"""


regexer1 = '[a-z]+' #name
regexer2 = '[a-z].*' #name
regexer3 = '[A-z]+' #with capital letters
regexer4 = r'[A-z\.]+' #name2
regexer5 = r'[A-z\.]+' #usar raw string return == ['jose', 'tecladocode.com']
regexer6 = r'[A-z\.]+@[A-z\.]+' #return ['jose@tecladocode.com']
regexer7 = r'[A-z\.]+@[A-z]+\.' #['jose@tecladocode.']
regexer8 = r'[A-z\.]+@[A-z]+\.com'
regexer9 = r'[A-z\.]+@[A-z]+\.(com|me)'
match = re.findall(regexer9, email)
print(match)