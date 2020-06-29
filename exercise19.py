# [abc , xyz] -----> [cba,zyx]

def reverse_word(k):
    word =[]
    for a in k:
        word.append(k[: :-1])       #for reverse
    return word

n= ["a s k","b y e"]
print(reverse_word(n))        


