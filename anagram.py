###
#  This program inputs two words and sees 
#  if they are anagrams.
###

print("Welcome to the Anagram tester!")
a = input("Enter your first word: ")
b = input("now your second word: ")

aa = sorted(a)
bb = sorted(b)

if aa == bb:
    print(f'Your words', a, 'and', b, 'are anagrams')
else:
    print(f'Sorry the words', a, 'and', b, 'are not anagrams')