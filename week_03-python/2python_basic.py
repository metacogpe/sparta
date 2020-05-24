num =10
num2 = num+ 5
print("",(num+num2))

aList = []
aList.append(1)
aList.append([1,2])

aDict = {}
aDict["hello"]="world"
aDict["list"]=[1,2]

def f(x):
    return 2*x + 3 
print(f(2))
print(f(3))

def sumAll(a,b,c):
    return a+b+c
print(sumAll(1,2,3))

def oddeven(num): 
    if num % 2 == 0:
        return True
    else:
        return False
print(oddeven(1))

fruits = ['사과','배','감자','귤']
for fruit in fruits:
    print(fruit)


fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def countFruit(name):
    count = 0 
    for fruit in fruits:
        if name == fruit:
            count +=1
    return count

countFruit('배')
countFruit('귤')
countFruit('사과')



people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person['name'], person['age'])


def getAge(name):
    for person in people:
        if name == person['name']:
            return person['age']
    return "없는 이름입니다. "

print(getAge('jo'))

