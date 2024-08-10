#Learning
print('My first code')


#if-else
age = 25
if age <= 18:
    print('Cant Drink')
else:
    print('Can Drink')

name = 'Nasif'
if name is 'Nasif':
    print('Hi Nasif')
elif name is 'Zeehan':
    print('Hello Zeehan')
else:
    print('Change your Name')


#for
fruit = ['mango', 'banana', 'apple', 'jackfruit', 'licchi']
for f in fruit[:3]:
    print(f)
    print(len(f))

for x in range(10):
    print(x)

for x in range(15, 20):
    print(x)

for x in range(10, 50, 10):
    print(x)


#while
number = 10
while number > 5:
    print(number)
    number -= 1

number = 10
while number > 5:
    print("number")
    number -= 1

magic = 4
for n in range(10):
    if n is magic:
        print(n, 'is a magic number')
    else:
        print(n)

magic = 4
for n in range(10):
    if n is magic:
        print(n, 'is a magic number')
        break
    else:
        print(n)

for m in range(12):
    if (m % 4 == 0):
        print(m)

player = [2, 5, 7, 9]
for n in range(20):
    if n in player:
        continue
    print(n)


