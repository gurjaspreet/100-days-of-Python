text = 'Programming in python.'

vowels = {'a', 'e', 'i', 'o', 'u'}

textset = set(text.lower())
textset.discard(' ')
textset.discard('.')
textset -= vowels

print(f'Number of items: {len(textset)}')