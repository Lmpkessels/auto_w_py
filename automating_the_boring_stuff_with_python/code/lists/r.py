import random
spam = ['Hello', 'Cat', 'New']

print(spam)
spam.insert(3, 'Flat')
print(spam)
spam.remove('Hello')
print(spam)
print(spam.index('New'))
print(spam)
spam.sort()
print(spam)

abc = ['b', 'c', 'a']
abc.sort()
print(abc)
print(abc.index('c'))

spam_plus_spam = []
spam_plus_spam += spam
print(spam_plus_spam)

spam_plus_spam.remove('Cat')
print(spam_plus_spam)
cat_in_spam = spam.index('Cat')
spam_plus_spam.insert(0, spam[cat_in_spam])
print(spam_plus_spam.index('Cat'))

print(random.choice(spam))