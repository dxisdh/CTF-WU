from random import *

def entry(r):
    flag = list(r)
    flag.reverse()
    flag = "".join(x for x in r)
    return flag

def stage1(r):
    r = list(r)
    for i in range(len(r)):
        r[i] = chr(ord(r[i]) ^ i)
    r = "".join(x for x in r)
    return r

def stage2(r):
    seed(10)
    inp = ""
    for i in range(len(r)):
        inp += chr(ord(r[i]) + randint(0,5))
    return inp

def finalstage(r):
    flag = ""
    i = 0
    while i < len(r):
        try:
            flag += r[i+1] + r[i]
        except:
            flag += r[i]
        i += 2
    flag = list(flag)
    flag.reverse()
    flag = "".join(x for x in flag)
    return flag

def rev(r):
    r = finalstage(r)
    r = stage2(r)
    r = stage1(r)
    r = entry(r)
    print(r)

flag = open('output.txt', 'r').readlines()[0]
rev(flag)
