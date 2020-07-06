# Currency converter:

with open('practice/currency.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split('\t')               # get key and value
    currencyDict[parsed[0]] = parsed[1]      # get dict format

# print(currencyDict)
amount = int(input('Enter the amount :\n'))    #amount

print('choose currency for convert your amount\n And the options are:\n')   # input
[print(items) for items in currencyDict.keys()]       # for list type

currency = input('please choose the currency:\n')

print (f'your amount {amount} INR is equal to {amount*float(currencyDict[currency])} {currency}')

print(currencyDict.keys())