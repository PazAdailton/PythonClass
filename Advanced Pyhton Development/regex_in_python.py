import re

email = 'jose@tecladocode.com'
expression = r'[a-z\.]+'

match = re.findall(expression, email)
print(match)

name = match[0]
domain = match[1]

print(name)
print(domain)
                            # (---------------------------------------------------------)


price = 'Price: $18,649.50'
expression = r'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)

print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets

prince_without_comma = matches.group(1).replace(',', '')
price_number = float(prince_without_comma)
print(f'float price number {price_number}')
