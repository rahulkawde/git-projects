#palidrome word

def palidrome(word):
    if word[ : : -1]== word:
        return True
    else:
         return False

print(palidrome("naman"))
print(palidrome("rahul"))