class name1():

    def first_name(self):
        print('Nasif')

class name2():

    def last_name(self):
        print('Zeehan')

class name(name1, name2):
    pass

nm = name()
nm.first_name()
nm.last_name()



list = ['30-01-2019', 'Nasif Zeehan', 'Banashree']
print(list[2])



date, name, plsce = ['30-01-2019', 'Nasif Zeehan', 'Banashree']
print(date)



def list(number):
    first, *middle, last = number
    avg = sum(middle)/len(middle)
    print(avg)

list([2, 20, 38, 43, 56, 78, 54,27,85, 93])



f1 = ['nasif', 'mush', 'ryan', 'noro']
f2 = ['zeehan', 'rahaman', 'rabby', 'hussain']
names = zip(f1, f2)

for a, b in names:
    print(a, b)



ans = lambda x: x * 7
print(ans(5))



stocks = {
    'FB' : 520,
    'Google' : 680,
    'Amazon' : 442,
    'Yahoo' : 85,
    'Apple' : 99
}
print(min(zip(stocks.keys(),stocks.values())))

stocks = {
    'FB' : 520,
    'Google' : 680,
    'Amazon' : 442,
    'Yahoo' : 85,
    'Apple' : 99
}
print(max(zip(stocks.keys(),stocks.values())))

stocks = {
    'FB' : 520,
    'Google' : 680,
    'Amazon' : 442,
    'Yahoo' : 85,
    'Apple' : 99
}
print(sorted(zip(stocks.keys(),stocks.values())))

stocks = {
    'FB' : 520,
    'Google' : 680,
    'Amazon' : 442,
    'Yahoo' : 85,
    'Apple' : 99
}
print(sorted(zip(stocks.values(), stocks.keys())))