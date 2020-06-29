import matplotlib         # import module
from matplotlib import pyplot as plt
#Regular Type
x =[2,3,5,7,9]       # x - axis no.
y=[8,9,2,4,7]        # y - axis no.
plt.plot(x,y)           # plot  line graph
plt.show()              # show graph

# Bar Type
x =[2,3,5,7,9]
y=[8,9,2,4,7]
plt.bar(x,y)            # show graph in bar type
plt.show()

#Histogram type

y=[53,69,18,75,90] # y axis value
plt.hist(y)        # shoe in histogram form
plt.show()

# plotting type

plt.plot([1,2,3,4],[1,4,9,16], 'ro')    # x aand y axis points and ro for red circle
plt.axis([0,6,0,20])                   # built x and y axis with co-ordinates
plt.show()
