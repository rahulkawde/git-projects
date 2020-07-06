# Currency Converter GUI ****************** √√√√√√√√
import tkinter as tk
from tkinter import ttk
win = tk.Tk ()
win.title('Currency Converter')
win.geometry('300x200')


with open ('practice/currency.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split('\t')               # get key and value
    currencyDict[parsed[0]] = parsed[1]



f1 = tk.Frame(win)
f1.grid(row=0,column=0)


def converter():
    amount = inr.get()
    # currency = (currencyDict[currency_var])
    # convertedAmt = amount * float(currency)
    # print(amount)  
    print(currencyDict[currency_var.get()])     # to get currency value

    ttk.Label(f1,text=f'your amount {amount} INR is equal to {amount * float(currencyDict[currency_var.get()])} {currency_var.get()}').grid(row=3,columnspan=2)
    

label1 = tk.Label(f1, text ='Enter your amount:')
label2 = tk.Label(f1, text ='Select currency :') 
label1.grid(row=0,column=0 ,padx=5,pady=5)
label2.grid(row=1,column=0, padx=5,pady=5)  

inr = tk.IntVar()
entry1 = tk.Entry (f1,width = 10, textvariable = inr)
entry1.grid(row=0,column=1,padx=5,pady=5)

currency_var= tk.StringVar()  
# currency_var= (currency_var)       # value store
currency_box = ttk.Combobox(f1,width=14,textvariable= currency_var,state='readonly')
currency_box['values'] = tuple(currencyDict.keys())     # list of currency
currency_box.grid(row=1,column=1,padx=5,pady=5)

converters = ttk.Button(f1,text= 'Converter',command = converter)
converters.grid(row=2,column=0,padx=5,pady=5)

win.mainloop()

# currency = currency_var.get()

# print(currencyDict.keys())
# # # print ( type(currencyDict()))
# # value1= inr*(currencyDict[currency_var])
# print(currencyDict.values())