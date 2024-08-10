# Function
def new():
    print("My first function")
new()

def usd_to_taka(currency):
    amount = currency * 80
    print(amount)
usd_to_taka(1000)


def age_limit(ur_age):
    gf_age = ur_age - 5
    return gf_age

my_limit = age_limit(22)
print('you can date girls aged', my_limit,'and above')


def get_gender(sex = 'Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    else:
        sex = 'Unclear'
    print(sex)

get_gender('f')
get_gender('m')
get_gender('r')
get_gender()


def new_One(name='Nasif', action='is', item='Awesome'):
    print(name, action, item)

new_One()
new_One('Zeehan', 'is not a', 'good boy')
new_One(name='NZ', item='fucked up')
new_One()


shop = ('milk', 'breed', 'coconut', 'chicken', 'beef', 'juice')
print(shop)

if "beef" in shop:
    print('You have that')
else:
    print('take one')


classmates = {'Lima' : ' Cute girl', 'FM' : ' Moody', 'Shan' : ' frndly', 'Afid' : ' Styly'}
print(classmates)
print(classmates['Lima'])
print(classmates['FM'])
print("  ")
for n, v in classmates.items():
    print(n + v)


