word=str(input('Enter the word: '))
rev=word
i=len(word)-1
a=0

Ans=set()
model="Wrong"

for x in word:
    ans=((word[a]==rev[i]))
    if ans==True:
        Ans.add('Correct')
    else:
        Ans.add('Wrong')
    a+=1
    i=i-1

if model in Ans:
    print ('not palindrome')
else:
    print('palindrome')   