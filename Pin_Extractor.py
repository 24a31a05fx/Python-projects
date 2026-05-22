# Build a Pin Extractor
# Description
'''
Write a function pin_extractor(poems) that takes a list of poems (strings). Each poem contains multiple lines separated by \n.

For each poem, you must generate a secret code (PIN) by analyzing each line:

Split the poem into lines.
For each line, split it into words.
Use the number of words in each line to build a string.
If a line has no words at a given position, add "0" instead.

Finally, return a list of secret codes for all poems.
'''
# source code:

def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes
       

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'
poems=[poem, poem2, poem3] 

print(pin_extractor([poem,poem2,poem3]))
