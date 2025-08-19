def substring(word,str):
    if str in word:
        print(f'{str} is present in {word}')
    else:
        print(f'{str} is not present in {word}')
word=input('enter the word:')
str=input('enter the string:')

substring(word,str)

