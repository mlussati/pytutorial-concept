# Compact the code with conditional expression
WORDS = 'Mary had a little Lamb'.split()
[(print(word.upper()) if word and word[0].isupper() \
    else print(word)) for word in WORDS ]

[print(word.upper()) for word in WORDS \
    if word and word[0].isupper()]

# Conversion of functions into dictionary
choice = int(input("Enter your choice in integer"))
actions= {0: 'you chose zero',1: 'you chose one', 99: 'you chose ninety-nine'}
print(actions.get(choice))