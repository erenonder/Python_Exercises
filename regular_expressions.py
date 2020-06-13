# regular_expressions.py
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


# pattern = re.compile(r'(http|https)://(www\.)?[a-z]+\.(gov|com)')

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.IGNORECASE)

# with open('data.txt', 'r') as f:
#     contents = f.read()

matches = pattern.search(sentence)
print(matches)
# for match in matches:
#     print(match)
