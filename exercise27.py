# set comprehension    always in disorder:
s={k**2 for k in range(1,11)}
print(s)
# dict comprehension
# first char
name={'rahul','sachin'}
first={i[0] for i in name}
print(first)


#odd even
odd_even= { a :('even' if a%2==0 else 'odd') for a in range(1,11)}
print(odd_even)


# square
square={num : num**2 for num in range (1,11)}
print(square)