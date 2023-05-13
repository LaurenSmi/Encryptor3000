import random
import string

def bigFib (name):
    return fib(name,1,1)


def fib(name, num1, num2):
    if(num2>= len(name)):
        return name
    
    name[num2] = name[num2].upper()
    temp = num2
    num2=num1+num2
    num1=temp
    fib(name,num1,num2)


def special(webChar):
    specials = ['a','s','o','h','v','i']
    toChange = ['@','$','0','#','^','!']
    
    for i in range(0,len(specials)):
        if(specials[i] == webChar):
            return toChange[i]
        return webChar

def flipper(webName):
    return webName[::-1]

def randomizer(length):
    return random.randint(0,length-1)

def muchoPlus(name):
    random.seed(4)
    alpha = string.ascii_lowercase
    for i in range(0,11):
        index = randomizer(len(name))
        alphChar = randomizer(len(alpha))
        name.insert(index,alpha[alphChar])
        return name
        
def do_encrypt(prompt):
    if(prompt==''):
        return 'No prompt entered'
    
    webName = prompt.lower()
    nameList = list(webName)
    muchoPlus(nameList)
    
    for i in range (0,len(nameList)):
        nameList[i] = special(nameList[i])
        
    bigFib(nameList)
    webName = ''.join(nameList)
    webName = flipper(webName)
    return webName
