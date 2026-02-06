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
regexer9 = r'[A-z\.]+@[A-z]+\.(com|me)' #return me
match = re.findall(regexer9, email)
print(match)



"""

Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = '^[a-zA-Z0-9][a-zA-Z0-9\-_()]*\.(jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None

"""