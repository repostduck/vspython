print("hello world!")
x = 1
print(x)
y = "steve"
print(y)
not_bool = True
print(not_bool)

x, y, not_bool = (2, 3, False)
print(type(not_bool))
#casting
z = str(x)
r = float(y)

#concatenate
line = "hello world!"
x = 19
print(line + " I am " + str(x)) #all variables must be type string

#Positional arguments - note we don't need to recast x
print('{saying} I am {num}'.format(saying=line,num=x))
#string methods
    #str.capitalize(), len(str), str.replace(), str.split(), str.find('r')
#list - ordered and changeable + dupes
numbers = [1,2,3,4,5]
nums2 = list((1,2,3,4,5))
print(numbers, nums2)
#0-based indexing 
print(numbers[0], nums2[2])
#len(l), l.append(element), l.remove(str), l.insert(pos, value)

#tuples -cannot be changed, but otherwise same as a list
tuple1 = ('1', '2', '3')
tuple2 = ('0',)

#can be indexed via zero based, but you can't change a value
#len(tuple), del tuple

#Set: unordered and unindexed collection, no dupes
num_set = {'1', '2', '3'}

#check if element in set
print('1' in num_set)
#add to set: 
num_set.add('4')

#remove from set
num_set.remove('1')

#set.clear, del set

#Dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

person2 = dict(first_name='Jane', last_name='Doe', age='20')
print(person, type(person), person2)

#Dictionary get
print(person['first_name'])
print(person.get('last_name'))
#Dictionary.keys(), Dictionary.items(), Dictionary.copy()

#functions
def sayHello(name='Todd'): #we've included a default argument
    print(f'Hello {name}')

sayHello('Ryan')
sayHello()
#Return values
def getSum(num1, num2):
    return num1 + num2

# lambda function: can take any number of argumens but can only have one expression

lamSum = lambda num1,num2: num1 + num2
print(lamSum(10,3)) 