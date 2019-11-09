import math, os, sys

ones = ['zero','one', 'two', 'three', 'four','five','six', 'seven', 'eight', 'nine']
teens = ['ten','eleven', 'twelve', 'thirteen', 'fourteen','fifteen','sixteen', 'seventeen', 'eightteen', 'nineteen']
tens = ['twenty','thirty', 'forty', 'fifty', 'sixty','seventy','eighty', 'ninty']
hundreds = ['one-hundred','two-hundred','three-hundred','four-hundred','five-hundred','six-hundred','seven-hundred','eight-hundred','nine-hundred']

print("1 through 9")
for i in ones:
    print(i,',', end=' ')

print('\n\n')
print("10 through 19")
for i in teens:
    print(i,',', end=' ')

print('\n\n')
print("20 through 99")
for i in tens:
    for j in ones:
        if j == 'zero':
            pass
        else:
            print(i,j,',', end=' ')


print('\n\n')
print("100 through 999")
for i in hundreds:
    for j in ones:
        if j == 'zero':
            pass
        else:
            print(i,'and',j,',', end=' ')
    for k in teens:
        print(i,'and',k,',', end=' ')

    for l in tens:
        for o in ones:
            print(i,'and',l,o,',', end=' ')
