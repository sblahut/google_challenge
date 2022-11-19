#### NOTES
####
####
#### Result = {'success' : 'great', 'colleague' : 'esteemed', 
####           'efforts' : 'incredible', 'achievement' : 'unlocked', 
####           'rabbits' : 'safe', 'foo' : 'win!'}
####
####

import base64

MESSAGE = '''
CEUfFAsWEUJCFlNYTEYPBxFQRRZfQksCBxkYVFBWBgdLQVJVU1RCRRYHAQQMUlgRFlQVBAMTHAZT EQsRVAsCAhoQEFhTXRZFQEFPFBdZWFQFBwEEBgFTEQsRVBcCDQcWH1RVFl9CSxMJFxZYRUJUQlZB TwYVV1QWX0JLBwcaUxELEVQVBQ9JUgk=
'''

KEY = 'PC_USERNAME'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))