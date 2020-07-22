def word_counter(s):
    counts ={}
    for i in s:
        counts[i]= s.count(i)     # char : count
    return counts 

word= input('enter your word:')
# print(word_counter('rahul kawde'))  
print(f'word counter : {word_counter(word)} ')  