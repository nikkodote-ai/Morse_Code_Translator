"""Convert user input to Morse Code and vice versa"""


import requests

#get morse code from web
morse_code_link = 'https://math.hws.edu/eck/cs225/s03/code.txt'
response = requests.get(morse_code_link).text.split('\n')
morse_code = {letter.split(' ')[0]: letter.strip().split(' ')[-1] for letter in response}
morse_code[' '] = '/'
morse_code["'"] = '.----.'

#ask for input from user then convert to morse code
raw_input = input('What would you like to translate to or from Morse Code: ')
output = ''

#automatically convert morse or not to it's counter code.
# if the input is likely to be morse, encrypt as morse, else, decrypt.
morse_texts = ['-', '.', '/', ' ']
likely_normal = (sum([raw_input.count(i) for i in morse_texts])/len(raw_input))

#encrypt to morse because the input is likely to be normal text
if  likely_normal < 0.9:
    for i in raw_input:
        try:
            output+= morse_code[i.upper()] + ' '
        except KeyError:
            print(f'{i} Not Found')
            break

#else, decrypt because this is likely to be Morse code
else:
    for i in raw_input.split(' '):
        for key,value in morse_code.items():
            if value == i:
                output+= key
    output = output.title()

print(output)