# from django.test import TestCase
import random

def ran():
    l = []
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
    ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for i in range(64):
        x = random.randint(0,1)
        if x == 0:
            x = random.randint(0,9)
            l.append(x)
        else:
            x = random.choice(a)
            l.append(x)
    r = ''.join(map(str, l))
    return r

print(ran())
