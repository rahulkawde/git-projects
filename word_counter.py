def word_counter(s):
    counts ={}
    for i in s:
        counts[i]= s.count(i)     # char : count
    return counts 


print(word_counter('rahul kawde'))    