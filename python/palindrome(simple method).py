word=str(input('Enter the word: '))

wordrev=word[::-1]

if word==wordrev:
    print('palindrome')
else:
    print('not palindrome')