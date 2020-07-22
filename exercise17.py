#palidrome word

def palidrome(word):
    if word[ : : -1]== word:
        return True
    else:
         return False

word = input('enter your word: ')
ans = palidrome(word)
print(f'palidrome : {ans}')
print(palidrome("naman"))
print(palidrome("rahul"))